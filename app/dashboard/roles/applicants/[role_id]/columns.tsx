import type { TRoleApplicantDetails } from "@/types";
import type { ColumnDef } from "@tanstack/react-table";

import { Button } from "@/components/ui";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
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
  {
    accessorKey: "skills",
    id: "skills",
    header: () => <div className="">Skills</div>,
    cell: ({ row }) => (
      <div>
        <Dialog>
          <DialogTrigger asChild>
            <Button variant={`outline`}>Skill Match</Button>
          </DialogTrigger>
          <DialogContent className="sm:max-w-[425px]">
            <DialogHeader>
              <DialogTitle>Applicant Skill Match</DialogTitle>
              <DialogDescription>Missing and Matched skills</DialogDescription>
            </DialogHeader>
            <div className="flex-col gap-x-2">
              Missing:{" "}
              <div className="space-x-2">
                {row.original.skills?.missing[0].skill_name === null
                  ? "None"
                  : row.original.skills?.missing.map((skill, idx) => (
                      <span
                        key={idx}
                        className="rounded-md border bg-red-300 px-1.5 py-0.5"
                      >
                        {skill.skill_name}
                      </span>
                    ))}
              </div>
              Obtained:{" "}
              <div className="space-x-2">
                {row.original.skills?.match.active.concat(
                  row.original.skills?.match.in_progress,
                ) === null ? (
                  <span>None</span>
                ) : (
                  row.original.skills?.match.active
                    .concat(row.original.skills?.match.in_progress)
                    .map((skill, idx) => (
                      <span
                        key={idx}
                        className="rounded-md border bg-red-300 px-1.5 py-0.5"
                      >
                        {skill}
                      </span>
                    ))
                )}
              </div>
            </div>
          </DialogContent>
        </Dialog>
      </div>
    ),
  },
];
