import React from "react";

import CreateRoleCard from "@/components/create-role/createRoleCard";
import DatePickerWithRange from "@/components/ui/datePicker";

const createRole = () => (
  <div className="flex h-screen items-center justify-center">
    <CreateRoleCard
      selectOptions={[
        { value: "finance", label: "Finance" },
        { value: "HR", label: "Human Resource and Admin" },
        { value: "IT", label: "Information Technology" },
        { value: "sales", label: "Sales" },
      ]}
    >
      <DatePickerWithRange />
    </CreateRoleCard>
  </div>
);

export default createRole;
