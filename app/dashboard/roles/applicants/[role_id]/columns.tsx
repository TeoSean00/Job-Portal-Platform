import type { TRoleApplicantDetails } from "@/types";
import type { ColumnDef } from "@tanstack/react-table";

import { cn, longDateTime } from "@/lib/utils";

export const ApplicantsColumns: ColumnDef<TRoleApplicantDetails>[] = [
  {
    accessorKey: "role_app_id",
    id: "role_app_id",
    header: () => <div className="">Id</div>,
    cell: ({ row }) => <div className="">{row.getValue("role_app_id")}</div>,
  },
  {
    accessorKey: "fname",
    id: "fname",
    header: () => <div className="">First Name</div>,
    cell: ({ row }) => <div className="">{row.getValue("fname")}</div>,
  },
  {
    accessorKey: "lname",
    id: "lname",
    header: () => <div className="">Last Name</div>,
    cell: ({ row }) => <div className="">{row.getValue("lname")}</div>,
  },

  {
    accessorKey: "dept",
    id: "dept",
    header: () => <div className="">Department</div>,
    cell: ({ row }) => <div className="">{row.getValue("dept")}</div>,
  },
  {
    accessorKey: "role_app_status",
    id: "role_app_status",
    header: () => <div className="">Status</div>,
    cell: ({ row }) => {
      const status = row.getValue("role_app_status");

      return (
        <div className="">
          <div
            className={cn(
              "rounded-md border px-1.5 py-1 text-center",
              status === "withdrawn" ? "bg-accent" : "bg-green-100",
            )}
          >
            {status as string}
          </div>
        </div>
      );
    },
  },
  {
    accessorKey: "role_app_ts_create",
    id: "role_app_ts_create",
    header: () => <div className="">Application Date</div>,
    cell: ({ row }) => {
      const date = Date.parse(row.getValue("role_app_ts_create"));
      const formattedDate = longDateTime.format(date).split(",")[1];
      return <div className="">{formattedDate}</div>;
    },
  },
];
