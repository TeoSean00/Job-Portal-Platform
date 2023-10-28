import * as z from "zod";

export const skillSchema = z.object({
  value: z.string().min(1),
});

export const roleFormSchema = z.object({
  roleName: z.string({ required_error: "A valid role must be selected" }),
  listingId: z
    .string({ required_error: "Listing ID is required" })
    .min(1, "A valid listing ID is required"),
  roleDescription: z
    .string()
    .min(1, "Role Description is required")
    .max(2000, "Role Description is too long, maximum 2000 characters allowed"),
  roleManager: z.string({ required_error: "Role Manager is required" }),
  location: z.string({ required_error: "Location is required" }),
  departments: z.string({ required_error: "Department is required" }),
  skills: z.array(skillSchema).nonempty("At least one skill is required"),
  startDate: z.date({ required_error: "Start Date is required" }),
});
