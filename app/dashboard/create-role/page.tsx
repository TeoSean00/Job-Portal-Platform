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

import { fetcherWithHeaders } from "@/components/AuthProvider";
import RoleForm from "@/components/create-role/RoleForm";
import { Separator } from "@/components/ui";
import { departments } from "@/lib/constants";

const CreateRole = () => {
  const { isLoaded, session } = useSession();
  const user = session?.user;
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
    if (roleData) {
      setRoleDetails(roleData.role_details);
    }
    if (roleError) {
      console.log("Error fetching role details:", roleError);
    }
  }, [roleData, roleError]);

  useEffect(() => {
    if (skillData) {
      setAllSkills(skillData.skills);
    }
    if (skillError) {
      console.log("Error fetching all skills:", skillError);
    }
  }, [skillData, skillError]);

  return (
    <div className="flex h-screen flex-col space-y-6">
      <div>
        <h3 className="text-xl font-medium">Add Role Listing</h3>
      </div>
      <Separator />
      {isLoaded && user && roleData && skillData ? (
        <RoleForm
          allSkills={allSkills}
          departments={departments}
          roles={roleDetails}
        />
      ) : (
        <div className="px-4 py-5 text-gray-700 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
          Loading data...
        </div>
      )}
    </div>
  );
};

export default CreateRole;
