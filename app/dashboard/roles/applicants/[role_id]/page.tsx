"use client";

import type { TRoleApplicantDetails, TRoleDetails } from "@/types";

import { useContext } from "react";
import useSWR from "swr";

import { ApplicantsColumns } from "./columns";

import { AuthContext } from "@/components/AuthProvider";
import { DataTable } from "@/components/data-table/DataTable";
import { Icons } from "@/components/icons/icons";
import { fetcher } from "@/lib/utils";

const fetcherWithHeaders = (url: string) =>
  fetch(url, { headers: { role: "hr" } }).then((res) => res.json());

const RoleApplicants = ({ params }: { params: { role_id: string } }) => {
  const staffId = useContext(AuthContext);

  const {
    data: roleApplicantsData,
    error: roleApplicantsError,
    isLoading: roleApplicantsLoading,
  } = useSWR<{
    role_applicants_details: TRoleApplicantDetails[];
  }>(`/api/role/applicants/${params.role_id}`, fetcher);

  const { data: roleDetailsData, error: roleDetailsError } = useSWR<{
    role_details: TRoleDetails[];
  }>(`/api/role/role_details`, fetcherWithHeaders);
  const { data: skillsData, error: skillsError } = useSWR(
    `/api/staff/role-skills-match/${staffId}/${params.role_id}`,
    fetcher,
  );
  if (roleApplicantsData) {
    roleApplicantsData.role_applicants_details[0].skills = skillsData;
  }
  return (
    <>
      {(roleApplicantsError || roleDetailsError) && (
        <div>Something went wrong loading applicants for the role</div>
      )}
      {roleDetailsData && <h1 className="text-xl">Applicants</h1>}
      {roleApplicantsLoading && (
        <Icons.spinner className="mx-auto my-10 animate-spin text-primary" />
      )}
      {roleApplicantsData && (
        <DataTable
          applicants={true}
          columns={ApplicantsColumns}
          data={roleApplicantsData.role_applicants_details}
        />
      )}
    </>
  );
};
export default RoleApplicants;
