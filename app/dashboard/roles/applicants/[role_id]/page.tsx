"use client";

import type { TRoleApplicantDetails, TRoleDetails } from "@/types";

import useSWR from "swr";

import { ApplicantsColumns } from "./columns";

import { DataTable } from "@/components/data-table/DataTable";
import { Icons } from "@/components/icons/icons";
import { fetcher } from "@/lib/utils";

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
          columns={ApplicantsColumns}
          data={roleApplicantsData.role_applicants_details}
        />
      )}
    </>
  );
};
export default RoleApplicants;
