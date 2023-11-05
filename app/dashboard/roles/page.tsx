"use client";

import type { RoleItem, RoleSkill } from "@/types";

import { useSession } from "@clerk/nextjs";
import Link from "next/link";
import React, { useEffect, useState } from "react";

import { DataTable } from "@/components/data-table/DataTable";
import { Separator, Button, columns } from "@/components/ui/";

type SkillAPIResponse = {
  skills: RoleSkill[];
};

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
type SkillLabel = {
  label: string;
  value: string;
};

const RolesPage = () => {
  const { session } = useSession();
  const user = session?.user;
  const userToken = user?.id;
  const userRole = user?.publicMetadata?.role;

  const [data, setData] = useState<ProcessedRole[]>([]);
  const [skills, setSkills] = useState<SkillLabel[]>([]);
  const fetchRoles = () => {
    fetch(`/api/role/role_listings_info`, {
      method: "GET",
      headers: {
        "user-token": userToken || "",
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
        const processedRoles: ProcessedRole[] = [];
        Object.keys(apiData).forEach((item: string) => {
          const role = apiData[Number(item)];
          const processedRole = {
            roleId: Number(item),
            roleName: role.role_name,
            roleDescription: role.role_desc,
            roleStatus: role.role_status,
            skillRequired: role.skills.map((skill) => skill.skill_name),
          };
          processedRoles.push(processedRole);
        });
        setData(processedRoles);
      })
      .catch((err) => {
        console.log("Error fetching role details:", err);
      });
  };

  const fetchSkills = () => {
    fetch(`/api/skill/get-all`, {
      method: "GET",
      headers: {
        "user-token": userToken || "",
        role: String(userRole || ""),
      },
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network error");
        }
        return res.json();
      })
      .then((apiData: SkillAPIResponse) => {
        const temp = apiData.skills.map((skill) => ({
          label: skill.skill_name,
          value: skill.skill_name,
        }));
        setSkills(temp);
      })
      .catch((err) => {
        console.log("Error fetching role details:", err);
      });
  };
  useEffect(() => {
    fetchRoles();
    fetchSkills();
  }, []);
  return (
    <>
      <div className="space-y-3">
        <h3 className="text-xl font-medium">Available Roles</h3>
        <Separator />
        <DataTable
          applicants={false}
          columns={columns}
          data={data}
          filterableColumns={[
            {
              id: "skillRequired",
              title: "Required Skills",
              options: skills,
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
