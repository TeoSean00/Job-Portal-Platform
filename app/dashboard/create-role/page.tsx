"use client";

import type { RoleDetail, SkillDetail } from "@/types";

import { useSession } from "@clerk/nextjs";
import React, { useEffect, useState } from "react";

import RoleForm from "@/components/create-role/RoleForm";
import { Separator } from "@/components/ui";
import { departments } from "@/lib/constants";

interface RoleAPIResponse {
  role_details: RoleDetail[];
}

interface SkillAPIResponse {
  skills: SkillDetail[];
}

const CreateRole = () => {
  const { session } = useSession();
  const user = session?.user;
  if (!user?.id || !user?.publicMetadata?.role) {
    throw new Error("User token or role is not defined!");
  }
  const userToken = user?.id;
  const userRole = user?.publicMetadata?.role;
  const [roleDetails, setRoleDetails] = useState<RoleDetail[]>([]);
  const [allSkills, setAllSkills] = useState<SkillDetail[]>([]);

  const fetchRoles = () => {
    fetch(`/api/role/role_details`, {
      method: "GET",
      headers: {
        "user-token": userToken,
        role: String(userRole),
      },
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network error");
        }
        return res.json();
      })
      .then((data: RoleAPIResponse) => {
        setRoleDetails(data.role_details);
      })
      .catch((err) => {
        console.log("Error fetching role details:", err);
      });
  };

  const fetchSkills = () => {
    fetch(`/api/skill/get-all`, {
      method: "GET",
      headers: {
        "user-token": userToken,
        role: String(userRole),
      },
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network error");
        }
        return res.json();
      })
      .then((data: SkillAPIResponse) => {
        setAllSkills(data.skills);
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
    <div className="flex h-screen flex-col space-y-6">
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
