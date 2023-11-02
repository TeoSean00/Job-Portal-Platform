"use client";

import type {
  AllSkillAPIResponse,
  RoleAPIResponse,
  RoleDetail,
  SkillDetail,
} from "@/types";

import { useSession } from "@clerk/nextjs";
import React, { useEffect, useState } from "react";
import useSWR from "swr";

import RoleForm from "@/components/create-role/RoleForm";
import { Separator } from "@/components/ui";
import { departments } from "@/lib/constants";
import { fetcherWithHeaders } from "@/lib/utils";

const CreateRole = () => {
  const { session } = useSession();
  const user = session?.user;
  const userToken = user?.id;
  const userRole = user?.publicMetadata?.role;
  const [roleDetails, setRoleDetails] = useState<RoleDetail[]>([]);
  const [allSkills, setAllSkills] = useState<SkillDetail[]>([]);
  const { data: roleData, error: roleError } = useSWR<RoleAPIResponse>(
    `/api/role/role_details`,
    (url: string) =>
      fetcherWithHeaders(url, {
        headers: {
          role: String(userRole),
        },
      }),
  );

  const { data: skillData, error: skillError } = useSWR<AllSkillAPIResponse>(
    `/api/skill/get-all`,
    (url: string) =>
      fetcherWithHeaders(url, {
        headers: {
          role: String(userRole),
        },
      }),
  );

  useEffect(() => {
    fetch("/api/healthcheck")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.error("Error fetching healthcheck:", error);
      });
  }, []);

  useEffect(() => {
    if (roleData) {
      setRoleDetails(roleData.role_details);
    }
    if (roleError) {
      console.log("Error fetching role details:", roleError);
    }
  }, [roleData, roleError]);
  useEffect(() => {}, [userToken]);
  useEffect(() => {
    if (skillData) {
      setAllSkills(skillData.skills);
    }
    if (skillError) {
      console.log("Error fetching all skills:", skillError);
    }
  }, [skillData, skillError]);

  return (
    <div className="flex h-screen flex-col space-y-3 px-3">
      <div>
        <h3 className="text-xl font-medium">Add Role Listing</h3>
      </div>
      <Separator />
      {roleDetails && (
        <RoleForm
          allSkills={allSkills}
          departments={departments}
          roles={roleDetails}
        />
      )}
    </div>
  );
};

export default CreateRole;
