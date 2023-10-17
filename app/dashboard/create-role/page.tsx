"use client";

import { useSession } from "@clerk/nextjs";
import React, { useEffect, useState } from "react";

import RoleForm from "@/components/create-role/RoleForm";
import { Separator } from "@/components/ui";

const skillList: Skill[] = [
  { value: "Pascal Programming", label: "Pascal Programming" },
  { value: "Python Programming", label: "Python Programming" },
  { value: "Certified Scrum Master", label: "Certified Scrum Master" },
  { value: "Marketing", label: "Marketing" },
  { value: "Scrum", label: "Scrum" },
  { value: "UI/UX", label: "UI/UX" },
  { value: "Product Management", label: "Product Management" },
];

const departments: Department[] = ["HR", "IT", "Sales", "Finance"].map(
  (department) => ({
    value: department,
    label: department,
  }),
);

interface RoleAPIResponse {
  role_details: RoleDetail[];
}

interface SkillAPIResponse {
  skills: SkillDetail[];
}

const CreateRole = () => {
  const { session } = useSession();
  const user = session?.user;
  const [roleDetails, setRoleDetails] = useState<RoleDetail[]>([]);
  const [allSkills, setAllSkills] = useState<SkillDetail[]>([]);

  const fetchRoles = () => {
    fetch(`/api/role/role_details`, {
      method: "GET",
      headers: {
        "user-token": user?.id,
        role: user?.publicMetadata?.role,
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
        // console.log(data.role_details);
      })
      .catch((err) => {
        console.log("Error fetching role details:", err);
      });
  };

  const fetchSkills = () => {
    fetch(`/api/skill/get-all`, {
      method: "GET",
      headers: {
        "user-token": user?.id,
        role: user?.publicMetadata?.role,
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
        // console.log("All Skills from page");
        // console.log(JSON.stringify(data.skills));
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
        <h3 className="text-xl font-medium">Role Creation</h3>
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
