import React from "react";

import RoleForm from "@/components/create-role/RoleForm";
import { Separator } from "@/components/ui/separator";

const skillList: Skill[] = [
  { value: "Pascal Programming", label: "Pascal Programming" },
  { value: "Python Programming", label: "Python Programming" },
  { value: "Certified Scrum Master", label: "Certified Scrum Master" },
  { value: "Marketing", label: "Marketing" },
  { value: "Scrum", label: "Scrum" },
  { value: "UI/UX", label: "UI/UX" },
  { value: "Product Management", label: "Product Management" },
];

const departments: Department[] = ["HR", "IT", "Sales", "Finance"].map(
  (department) => ({
    value: department,
    label: department,
  }),
);

const createRole = () => (
  <div className="flex h-screen flex-col space-y-6">
    <div>
      <h3 className="text-xl font-medium">Role Creation</h3>
    </div>
    <Separator />
    <RoleForm departments={departments} skillList={skillList} />
  </div>
);

export default createRole;
