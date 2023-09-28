"use client";

import type { ColumnDef } from "@tanstack/react-table";

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type Payment = {
  roleId: number;
  roleName: string;
  roleDescription: string;
};

export const columns: ColumnDef<Payment>[] = [
  {
    accessorKey: "roleId",
    header: "Role ID",
  },
  {
    accessorKey: "roleName",
  },
  {
    accessorKey: "roleDescription",
    header: "Description",
  },
];
