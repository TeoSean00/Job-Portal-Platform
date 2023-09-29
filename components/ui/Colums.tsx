"use client";

import type { ColumnDef } from "@tanstack/react-table";

import { ArrowUpDown, MoreHorizontal } from "lucide-react";

import { Button } from "@/components/ui/Button";

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type Payment = {
  roleId: number;
  roleName: string;
  roleDescription: string;
  skillRequired: string[];
};

export const columns: ColumnDef<Payment>[] = [
  {
    accessorKey: "roleId",
    header: ({ column }) => (
      <Button
        variant="ghost"
        onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
      >
        Role ID
        <ArrowUpDown className="ml-2 h-4 w-4" />
      </Button>
    ),
  },
  {
    accessorKey: "roleName",
    header: ({ column }) => (
      <Button
        variant="ghost"
        onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
      >
        Role Name
        <ArrowUpDown className="ml-2 h-4 w-4" />
      </Button>
    ),
  },
  {
    accessorKey: "roleDescription",
    header: "Description",
  },
  {
    accessorKey: "skillRequired",
    header: "Required Skills",
  },
];
