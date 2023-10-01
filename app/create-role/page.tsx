import React from "react";

// import CreateRoleCard from "@/components/create-role/createRoleCard";
// import DatePickerWithRange from "@/components/ui/datePicker";
import RoleForm from "@/components/create-role/RoleForm";
import { Separator } from "@/components/ui/separator";

const createRole = () => (
  <div className="flex h-screen flex-col space-y-6">
    <div>
      <h3 className="text-xl font-medium">Role Creation</h3>
    </div>
    <Separator />
    <RoleForm />
  </div>
);

export default createRole;
