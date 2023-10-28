import type { Department } from "@/types";

export const departmentPlaceholder = "Select department";
export const locationPlaceholder = "Select location";
export const Locations = [
  "Singapore",
  "Malaysia",
  "Indonesia",
  "Thailand",
  "Hong Kong",
  "Philippines",
  "United States, San Francisco",
  "United States, New York",
  "United States, Los Angeles",
  "United Kingdom, London",
];
export const departments: Department[] = ["HR", "IT", "Sales", "Finance"].map(
  (department) => ({
    value: department,
    label: department,
  }),
);
