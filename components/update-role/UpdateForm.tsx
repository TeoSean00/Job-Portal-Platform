"use client";

import type {
  RoleFormValues,
  RoleSkillAPIResponse,
  SkillAPIResponse,
  StaffIdAPIResponse,
  UpdateFormProps,
} from "@/types";

import { useSession } from "@clerk/nextjs";
import { zodResolver } from "@hookform/resolvers/zod";
import { useContext, useEffect, useState } from "react";
import { Controller, useForm } from "react-hook-form";
import useSWR from "swr";

import { AuthContext } from "@/components/AuthProvider";
import {
  Button,
  Combobox,
  DatePickerWithPresets,
  SelectComponent,
  Textarea,
  toast,
  ToastAction,
  Input,
} from "@/components/ui";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import {
  departmentPlaceholder,
  locationPlaceholder,
  Locations,
} from "@/lib/constants";
import { roleFormSchema } from "@/lib/schema";
import { fetcher, fetcherWithHeaders, longDateTime } from "@/lib/utils";

const currentDate = new Date();
const formattedDate = longDateTime.format(currentDate);
const UpdateForm: React.FC<UpdateFormProps> = ({
  departments,
  roles,
  allSkills,
  roleToUpdateData,
}) => {
  const { isLoaded, session } = useSession();
  const user = session?.user;
  const staffId = useContext(AuthContext);
  const userRole = user?.publicMetadata?.role;
  const [skillIdList, setSkillId] = useState<SkillAPIResponse[]>([]);
  const [managerDetails, setManagerDetails] = useState<StaffIdAPIResponse[]>(
    [],
  );

  const defaultValues: Partial<RoleFormValues> = {
    roleName: roleToUpdateData.role_id.toString(),
    roleDescription: roleToUpdateData.role_listing_desc,
    roleManager: roleToUpdateData.role_listing_source.toString(),
    location: roleToUpdateData.role_location,
    departments: roleToUpdateData.role_department,
    startDate: new Date(roleToUpdateData.role_listing_open) || undefined,
    listingId: roleToUpdateData.role_listing_id.toString(),
  };

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
      role_listing_id: data.listingId,
      role_id: parseInt(data.roleName, 10),
      role_listing_desc: data.roleDescription,
      role_listing_source: parseInt(data.roleManager, 10),
      role_listing_open: formatDateToISOWithoutZ(data.startDate),
      role_listing_close: roleToUpdateData.role_listing_close,
      role_listing_hide: roleToUpdateData.role_listing_hide,
      role_listing_creator: roleToUpdateData.role_listing_creator,
      role_listing_ts_create: roleToUpdateData.role_listing_ts_create,
      role_department: data.departments,
      role_location: data.location,
    };
    if (staffId) {
      fetch(`/api/role/role_listing`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          role: String(userRole),
          "updater-staff-id": String(staffId),
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
          console.log(err);
          toast({
            variant: "destructive",
            title: "Error creating role!",
            description: err.message,
            action: <ToastAction altText="Dismiss">Dismiss</ToastAction>,
          });
        });
    }
  }

  const { data: managerData } = useSWR<StaffIdAPIResponse[]>(
    "/api/staff/manager",
    fetcher,
  );
  const { data: roleSkillsData } = useSWR<RoleSkillAPIResponse>(
    `/api/role/role_skills?role_id=${form.getValues().roleName}`,
    (url: string) =>
      fetcherWithHeaders(url, {
        headers: {
          role: String(userRole),
        },
      }),
  );

  useEffect(() => {
    if (managerData) {
      setManagerDetails(managerData);
    }
  }, [user?.id, managerData]);

  useEffect(() => {
    if (roleSkillsData && allSkills) {
      const associatedSkillIds = roleSkillsData.role_skills?.map(
        (rs) => rs.skill_id,
      );
      if (associatedSkillIds) {
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
    }
  }, [roleSkillsData, allSkills]);

  const formattedManagerDetails = managerDetails.map((manager) => ({
    label: `${manager.fname} ${manager.lname}`,
    value: manager.staff_id.toString(),
  }));

  return (
    <>
      {isLoaded && user ? (
        <Form {...form}>
          <form className="space-y-8" onSubmit={form.handleSubmit(onSubmit)}>
            <div className="flex w-full flex-grow space-x-4">
              <FormField
                control={form.control}
                name="roleName"
                render={() => (
                  <FormItem className="w-full">
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
                name="listingId"
                render={() => (
                  <FormItem className="w-full">
                    <FormLabel className="text-base">Listing Id</FormLabel>
                    <Controller
                      control={form.control}
                      name="listingId"
                      render={({ field }) => (
                        <Input placeholder="id" type="number" {...field} />
                      )}
                    />
                    <FormMessage />
                  </FormItem>
                )}
              />
            </div>
            <FormField
              control={form.control}
              name="roleDescription"
              render={({ field }) => (
                <FormItem>
                  <FormLabel className="text-base">
                    Listing Description
                  </FormLabel>
                  <FormDescription>
                    Describe the role in detail.
                  </FormDescription>
                  <FormControl>
                    <Textarea className=" resize-y" placeholder="" {...field} />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />
            <FormField
              control={form.control}
              name="roleManager"
              render={() => (
                <FormItem className="w-full">
                  <FormLabel className="text-base">
                    Role&apos;s Manager
                  </FormLabel>
                  <FormDescription>Select role&apos;s manager.</FormDescription>
                  <Controller
                    control={form.control}
                    name="roleManager"
                    render={({ field }) => (
                      <Combobox
                        items={formattedManagerDetails}
                        placeholder="Select a Manager"
                        value={field.value}
                        onChange={field.onChange}
                      />
                    )}
                  />
                  <FormMessage />
                </FormItem>
              )}
            />
            <div className="flex w-full flex-grow space-x-4">
              <FormField
                control={form.control}
                name="location"
                render={() => (
                  <FormItem className="w-full">
                    <FormLabel className=" text-base">Location</FormLabel>
                    <FormDescription>
                      Select the location of role.
                    </FormDescription>
                    <Controller
                      control={form.control}
                      name="location"
                      render={({ field }) => (
                        <Combobox
                          items={Locations.map((location) => ({
                            value: location,
                            label: location,
                          }))}
                          placeholder={locationPlaceholder}
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
                name="departments"
                render={() => (
                  <FormItem className="w-full">
                    <FormLabel className="text-base">Department</FormLabel>
                    <FormDescription>
                      Select the department the role.
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
            </div>
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
              name="startDate"
              render={({ fieldState }) => (
                <FormItem>
                  <FormLabel className="text-base">Start Date</FormLabel>
                  <FormDescription>
                    Select the date for this listing to be shown.
                  </FormDescription>
                  <Controller
                    control={form.control}
                    name="startDate"
                    render={({ field: { onChange, value } }) => (
                      <DatePickerWithPresets
                        className="w-full"
                        value={value}
                        onChange={(date) => {
                          onChange(date);
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
            <Button type="submit">Update Role</Button>
          </form>
        </Form>
      ) : (
        <div className="px-4 py-5 text-gray-700 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
          Loading data...
        </div>
      )}
    </>
  );
};

export default UpdateForm;
