"use client";

import type {
  RoleFormProps,
  RoleFormValues,
  RoleSkillId,
  SkillAPIResponse,
} from "@/types";

import { useSession } from "@clerk/nextjs";
import { zodResolver } from "@hookform/resolvers/zod";
import { useEffect, useState } from "react";
import { Controller, useForm } from "react-hook-form";
import * as z from "zod";

import {
  Button,
  Combobox,
  SelectComponent,
  Textarea,
  toast,
  ToastAction,
} from "@/components/ui";
import DatePickerWithRange from "@/components/ui/datePickerWithRange";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { longDateTime } from "@/lib/utils";

const departmentPlaceholder = "Select a department";

const skillSchema = z.object({
  value: z.string().min(1),
});

const roleFormSchema = z.object({
  roleName: z.string().nonempty("A valid role must be selected"),
  roleDescription: z.string().min(1, "Role Description is required").max(1000),
  departments: z.string(),
  skills: z.array(skillSchema).nonempty("At least one skill is required."),
  dateRange: z.object({
    from: z.date(),
    to: z.date(),
  }),
});

interface RoleSkillAPIResponse {
  role_skills: RoleSkillId[];
}

interface StaffIdAPIResponse {
  staff_id: number;
  fname: string;
  lname: string;
  dept: string;
  email: string;
  phone: string;
  biz_address: string;
  sys_role: string;
}

interface Skill {
  skill_status: "active" | "inactive";
  skill_name: string;
  skill_id: number;
}

interface Role {
  role_id: number;
  role_name: string;
}

// This can come from your database or API.
const defaultValues: Partial<RoleFormValues> = {
  roleDescription: "",
  roleName: "",
};

const currentDate = new Date();
const formattedDate = longDateTime.format(currentDate);
const RoleForm: React.FC<RoleFormProps> = ({
  departments,
  roles,
  allSkills,
}) => {
  const { session } = useSession();
  const user = session?.user;
  if (!user?.id || !user?.publicMetadata?.role) {
    throw new Error("User token or role is not defined!");
  }
  const userToken = user?.id;
  const userRole = user?.publicMetadata?.role;
  const [skillIdList, setSkillId] = useState<SkillAPIResponse[]>([]);
  const [staffId, setStaffId] = useState<number | null>(null);

  const form = useForm<RoleFormValues>({
    resolver: zodResolver(roleFormSchema),
    defaultValues,
    mode: "onChange",
  });

  function formatDateToISOWithoutZ(date: Date): string {
    return `${date.getUTCFullYear()}-${String(date.getUTCMonth() + 1).padStart(
      2,
      "0",
    )}-${String(date.getUTCDate()).padStart(2, "0")}T${String(
      date.getUTCHours(),
    ).padStart(2, "0")}:${String(date.getUTCMinutes()).padStart(
      2,
      "0",
    )}:${String(date.getUTCSeconds()).padStart(2, "0")}`;
  }

  function onSubmit(data: RoleFormValues) {
    const transformedData = {
      role_id: parseInt(data.roleName, 10),
      role_listing_desc: data.roleDescription,
      role_listing_source: staffId,
      role_listing_open: formatDateToISOWithoutZ(data.dateRange.from),
      role_listing_close: formatDateToISOWithoutZ(data.dateRange.to),
      role_listing_hide: formatDateToISOWithoutZ(data.dateRange.to),
      role_listing_creator: staffId,
      role_listing_ts_create: formatDateToISOWithoutZ(new Date()),
      role_listing_updater: staffId,
      role_listing_ts_update: formatDateToISOWithoutZ(new Date()),
    };
    console.log(JSON.stringify(transformedData));
    fetch(`/api/role/role_listing`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "user-token": userToken,
        role: String(userRole),
      },
      body: JSON.stringify(transformedData),
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error(res.statusText);
        }
        return res.json();
      })
      .then(() => {
        toast({
          title: "Role Successfully Created!",
          description: formattedDate,
          action: <ToastAction altText="Dismiss">Dismiss</ToastAction>,
        });
      })
      .catch((err: Error) => {
        toast({
          variant: "destructive",
          title: "Error creating role!",
          description: err.message,
          action: <ToastAction altText="Dismiss">Dismiss</ToastAction>,
        });
      });
  }

  useEffect(() => {
    if (user?.id) {
      fetch(`/api/staff/clerk/${user.id}`, {
        method: "GET",
      })
        .then((res) => {
          if (!res.ok) {
            throw new Error("Network error");
          }
          return res.json();
        })
        .then((data: StaffIdAPIResponse) => {
          setStaffId(data.staff_id);
        })
        .catch((err) => {
          console.log("Error fetching staff_id:", err);
        });
    }
  }, [user?.id]);

  const getRoleSkills = (roleId: string) => {
    fetch(`/api/role/role_skills?role_id=${roleId}`, {
      method: "GET",
      headers: {
        "user-token": userToken,
        role: String(userRole),
      },
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network error");
        }
        return res.json();
      })
      .then((data: RoleSkillAPIResponse) => {
        if (allSkills) {
          const associatedSkillIds = data.role_skills.map((rs) => rs.skill_id);

          const filteredSkills = allSkills.filter((skill) =>
            associatedSkillIds.includes(skill.skill_id),
          );
          setSkillId(filteredSkills);
          form.setValue(
            "skills",
            filteredSkills.map((skill) => ({
              value: skill.skill_id.toString(),
              label: skill.skill_name,
            })),
          );
        }
      })
      .catch((err) => {
        console.log("Error fetching role skills:", err);
      });
  };

  useEffect(() => {
    const roleId: string = form.getValues().roleName;
    if (roleId) {
      getRoleSkills(roleId);
    }
  }, [form.watch("roleName")]);

  return (
    <div className="">
      <Form {...form}>
        <form className="space-y-8" onSubmit={form.handleSubmit(onSubmit)}>
          <FormField
            control={form.control}
            name="roleName"
            render={() => (
              <FormItem>
                <FormLabel className="text-base">Role</FormLabel>
                <Controller
                  control={form.control}
                  name="roleName"
                  render={({ field }) => (
                    <Combobox
                      items={roles.map((role) => ({
                        value: role.role_id.toString(),
                        label: role.role_name,
                      }))}
                      placeholder="Select a Role"
                      value={field.value}
                      onChange={(selectedRoleId) =>
                        field.onChange(selectedRoleId)
                      }
                    />
                  )}
                />
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="roleDescription"
            render={({ field }) => (
              <FormItem>
                <FormLabel className="text-base">Role Description</FormLabel>
                <FormDescription>Describe the role in detail.</FormDescription>
                <FormControl>
                  <Textarea className=" resize-y" placeholder="" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="departments"
            render={() => (
              <FormItem>
                <FormLabel className="text-base">Department</FormLabel>
                <FormDescription>
                  Select the department the role belongs in.
                </FormDescription>
                <Controller
                  control={form.control}
                  name="departments"
                  render={({ field }) => (
                    <Combobox
                      items={departments}
                      placeholder={departmentPlaceholder}
                      value={field.value}
                      onChange={field.onChange}
                    />
                  )}
                />
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="skills"
            render={({ field }) => (
              <FormItem>
                <FormLabel className="text-base">Skills</FormLabel>
                <FormDescription>Skills required for role.</FormDescription>
                <SelectComponent
                  createAble={true}
                  isMulti={true}
                  options={skillIdList.map((skill) => ({
                    value: skill.skill_id.toString(),
                    label: skill.skill_name,
                  }))}
                  placeholder="Select Skills"
                  {...field}
                />
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="dateRange"
            render={({ fieldState }) => (
              <FormItem>
                <FormLabel className="text-base">Date Range</FormLabel>
                <FormDescription>
                  Select the start and end date for this role.
                </FormDescription>
                <Controller
                  control={form.control}
                  name="dateRange"
                  render={({ field: { onChange, value } }) => (
                    <DatePickerWithRange
                      className="w-full"
                      value={value}
                      onChange={(selectedDateRange) => {
                        if (selectedDateRange) {
                          if (selectedDateRange.from && selectedDateRange.to) {
                            onChange({
                              from: selectedDateRange.from,
                              to: selectedDateRange.to,
                            });
                            form.clearErrors("dateRange");
                          } else {
                            form.setError("dateRange", {
                              type: "manual",
                              message:
                                "Both start and end dates must be selected",
                            });
                          }
                        } else {
                          onChange(undefined);
                        }
                      }}
                    />
                  )}
                />
                <FormMessage>
                  {fieldState.error && fieldState.error.message}
                </FormMessage>
              </FormItem>
            )}
          />
          <Button type="submit">Create Role</Button>
        </form>
      </Form>
    </div>
  );
};

export default RoleForm;
