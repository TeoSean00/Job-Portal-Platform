"use client";

import type { RoleItem } from "@/types";

import { useSession } from "@clerk/nextjs";
import React, { useEffect, useState } from "react";

import { DataTable } from "@/components/data-table/DataTable";
import { columns } from "@/components/ui/";

type RoleAPIResponse = {
  [role_id: number]: RoleItem;
};
type ProcessedRole = {
  roleId: number;
  roleName: string;
  roleDescription: string;
  roleStatus: string;
  skillRequired: string[];
};

const RolesPage = () => {
  const { session } = useSession();
  const user = session?.user;
  // if (!user?.id || !user?.publicMetadata?.role) {
  //   throw new Error("User token or role is not defined!");
  // }
  const userToken = user?.id;
  const userRole = user?.publicMetadata?.role;

  const [data, setData] = useState<ProcessedRole[]>([]);
  const fetchRoles = () => {
    fetch(`/api/role/role_info`, {
      method: "GET",
      headers: {
        "user-token": userToken || "", // Make sure it's not undefined
        role: String(userRole || ""),
      },
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network error");
        }
        return res.json();
      })
      .then((apiData: RoleAPIResponse) => {
        console.log(apiData);
        const processedRoles: ProcessedRole[] = [];
        Object.keys(apiData).forEach((item: string) => {
          const role = apiData[Number(item)];
          const processedRole = {
            roleId: role.role_id,
            roleName: role.role_name,
            roleDescription: role.role_desc,
            roleStatus: role.role_status,
            skillRequired: role.skills.map((skill) => skill.skill_name),
          };
          processedRoles.push(processedRole);
        });
        console.log(processedRoles);
        setData(processedRoles);
      })
      .catch((err) => {
        console.log("Error fetching role details:", err);
      });
  };
  const tempSkills = [
    { label: "Skill 1", value: "skill 1" },
    { label: "Skill 2", value: "skill 2" },
    { label: "Skill 3", value: "skill 3" },
    { label: "Skill 4", value: "skill 4" },
  ];
  // const data: ProcessedRole[] = [
  // {
  //   roleId: 1,
  //   roleName: "Temp Role 1",
  //   roleDescription: "This is a temporary role 1",
  //   roleStatus: "active",
  //   skillRequired: ["skill 1", "skill 2"],
  // },
  // {
  //   roleId: 2,
  //   roleName: "Temp Role 2",
  //   roleDescription:
  //     "This is a temporary long description 2 This is a temporary long description 2 This is a temporary long description 2 This is a temporary long description 2 This is a temporary long description 2",
  //   roleStatus: "active",
  //   skillRequired: ["skill 2", "skill 3"],
  // },
  // {
  //   roleId: 3,
  //   roleName: "Temp Inactive Role",
  //   roleDescription: "This is a temporary inactive role",
  //   roleStatus: "inactive",
  //   skillRequired: ["skill 3", "skill 4"],
  // },
  // ];
  useEffect(() => {
    fetchRoles();
  }, []);
  return (
    <>
      <div className="">
        Roles
        <DataTable
          columns={columns}
          data={data}
          filterableColumns={[
            {
              id: "skillRequired",
              title: "Required Skills",
              options: tempSkills,
            },
          ]}
          searchableColumns={[
            {
              id: "roleName",
              title: "Role Name",
            },
          ]}
        />
      </div>
    </>
  );
};

export default RolesPage;
