"use client";

import { zodResolver } from "@hookform/resolvers/zod";
import { Controller, useFieldArray, useForm } from "react-hook-form";
import * as z from "zod";

import { Button } from "@/components/ui/button";
import { Combobox } from "@/components/ui/comboBox";
import DatePickerWithRange from "@/components/ui/datePicker";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { SelectComponent } from "@/components/ui/selectComponent";
import { Textarea } from "@/components/ui/textarea";
import { toast } from "@/components/ui/use-toast";

const jobTypeList = [
  { value: "Pascal Programming", label: "Pascal Programming" },
  { value: "Python Programming", label: "Python Programming" },
  { value: "Certified Scrum Master", label: "Certified Scrum Master" },
  { value: "Marketing", label: "Marketing" },
  { value: "Scrum", label: "Scrum" },
  { value: "UI/UX", label: "UI/UX" },
  { value: "Product Management", label: "Product Management" },
];

const departments = ["HR", "IT", "Sales", "Finance"].map((department) => ({
  value: department,
  label: department,
}));

const departmentPlaceholder = "Select a department";

const skillSchema = z.object({
  value: z.string().min(1), // Assuming each skill is represented as a string
});

const roleFormSchema = z.object({
  roleName: z.string().max(100, {
    message: "Role Name must not be longer than 100 characters.",
  }),
  roleDescription: z.string().min(1, "Role Description is required").max(1000),
  departments: z.string(),
  skills: z.array(skillSchema).nonempty("At least one skill is required."),
  dateRange: z.object({
    from: z.date(),
    to: z.date(),
  }),
});

type RoleFormValues = z.infer<typeof roleFormSchema>;

// This can come from your database or API.
const defaultValues: Partial<RoleFormValues> = {
  roleDescription: "",
};

const RoleForm = () => {
  const form = useForm<RoleFormValues>({
    resolver: zodResolver(roleFormSchema),
    defaultValues,
    mode: "onChange",
  });

  const { fields, append } = useFieldArray({
    name: "skills",
    control: form.control,
  });

  function onSubmit(data: RoleFormValues) {
    toast({
      title: "You submitted the following values:",
      description: (
        <pre className="mt-2 w-[340px] rounded-md bg-slate-950 p-4">
          <code className="text-white">{JSON.stringify(data, null, 2)}</code>
        </pre>
      ),
    });
  }

  return (
    <div className="">
      <Form {...form}>
        <form className="space-y-8" onSubmit={form.handleSubmit(onSubmit)}>
          <FormField
            control={form.control}
            name="roleName"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Role Name</FormLabel>
                <FormControl>
                  <Input placeholder="" {...field} />
                </FormControl>
                <FormDescription></FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="roleDescription"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Role Description</FormLabel>
                <FormDescription>Describe the role in detail.</FormDescription>
                <FormControl>
                  <Textarea className="resize-none" placeholder="" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="departments"
            render={({ field: departmentField }) => (
              <FormItem>
                <FormLabel>Department</FormLabel>
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
                <FormLabel>Skills</FormLabel>
                <FormDescription>Skills required for role.</FormDescription>
                <SelectComponent
                  createAble={true}
                  isMulti={true}
                  options={jobTypeList}
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
            render={({ field, fieldState }) => (
              <FormItem>
                <FormLabel>Date Range</FormLabel>
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
