"use client";

import type { ColumnDef } from "@tanstack/react-table";

import useSWR from "swr";

import { DataTable } from "@/components/data-table/DataTable";
import { Icons } from "@/components/icons/icons";
import { cn, fetcher, longDateTime } from "@/lib/utils";

type TRoleApplicantDetails = {
  biz_address: string;
  dept: string;
  email: string;
  fname: string;
  lname: string;
  phone: string;
  role_app_id: number;
  role_app_status: string;
  role_app_ts_create: string;
  role_listing_id: number;
  staff_id: number;
  sys_role: string;
};

const columns: ColumnDef<TRoleApplicantDetails>[] = [
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

type TRoleDetails = {
  role_id: number;
  role_name: string;
  role_description: string;
  role_status: string;
};

const fetcherWithHeaders = (url: string) =>
  fetch(url, { headers: { role: "hr" } }).then((res) => res.json());

const RoleApplicants = ({ params }: { params: { role_id: string } }) => {
  const id = parseInt(params.role_id, 2);
  const {
    data: roleApplicantsData,
    error: roleApplicantsError,
    isLoading: roleApplicantsLoading,
  } = useSWR<{
    role_applicants_details: TRoleApplicantDetails[];
  }>(`/api/role/applicants/${id}`, fetcher);

  const { data: roleDetailsData, error: roleDetailsError } = useSWR<{
    role_details: TRoleDetails[];
  }>(`/api/role/role_details`, fetcherWithHeaders);
  const roleName = roleDetailsData?.role_details[id].role_name;

  return (
    <>
      {(roleApplicantsError || roleDetailsError) && (
        <div>Something went wrong loading applicants for the role</div>
      )}
      {roleDetailsData && (
        <h1 className="text-xl">
          Applicants for {` `}
          <span className="font-semibold text-primary">{roleName}</span>
        </h1>
      )}
      {roleApplicantsLoading && (
        <Icons.spinner className="mx-auto my-10 animate-spin text-primary" />
      )}
      {roleApplicantsData && (
        <DataTable
          columns={columns}
          data={roleApplicantsData.role_applicants_details}
        />
      )}
    </>
  );
};
export default RoleApplicants;
