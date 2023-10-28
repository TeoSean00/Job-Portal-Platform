"use client";

import type { ColumnDef, Row } from "@tanstack/react-table";

import { ArrowUpDown, MoreHorizontal } from "lucide-react";

// eslint-disable-next-line import/no-cycle
import { Button } from "@/components/ui";

interface RowObject {
  getValue: (id: string) => string[];
}

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
        className="space-x-2"
        variant="ghost"
        onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
      >
        <span>ID</span>
        <ArrowUpDown className="h-4 w-4" />
      </Button>
    ),
  },
  {
    accessorKey: "roleName",
    header: ({ column }) => (
      <Button
        className="space-x-2"
        variant="ghost"
        onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
      >
        <span>Name</span>
        <ArrowUpDown className="h-4 w-4" />
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
    filterFn: (row: RowObject, id: string, value: string[]) => {
      if (!Array.isArray(value)) {
        return false; // Handle the case where value is not an array
      }
      const hasOverlap = value.every((skill) =>
        row.getValue(id).includes(skill),
      );
      return hasOverlap;
    },
  },
];
