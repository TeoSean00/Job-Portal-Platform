"use client";

import type {
  AllSkillAPIResponse,
  RoleAPIResponse,
  RoleDetail,
  RoleListing,
  SkillDetail,
  RoleToUpdateData,
} from "@/types";

import { useSession } from "@clerk/nextjs";
import React, { useEffect, useState } from "react";
import useSWR from "swr";

import { Separator } from "@/components/ui";
import UpdateForm from "@/components/update-role/UpdateForm";
import { departments } from "@/lib/constants";
import { fetcherWithHeaders } from "@/lib/utils";

const fetcherHR = (url: string) =>
  fetch(url, { headers: { role: "hr" } }).then((res) => res.json());

const CreateRole = ({ params }: { params: { role_id: string } }) => {
  const id = params.role_id;
  const { isLoaded, session } = useSession();
  const user = session?.user;
  const userRole = user?.publicMetadata?.role;
  const [roleDetails, setRoleDetails] = useState<RoleDetail[]>([]);
  const [allSkills, setAllSkills] = useState<SkillDetail[]>([]);
  const [roleListingData, setRoleListingData] = useState<RoleListing>();

  const { data: roleData, error: roleError } = useSWR<RoleAPIResponse>(
    `/api/role/role_details`,
    (url: string) =>
      fetcherWithHeaders(url, {
        headers: {
          role: String(userRole),
        },
      }),
  );

  const { data: roleToUpdateData, error: roleToUpdateError } =
    useSWR<RoleToUpdateData>(
      `/api/role/role_listing?role_listing_id=${id}`,
      fetcherHR,
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
    if (roleToUpdateData) {
      setRoleListingData(roleToUpdateData.role_listing.role_listing);
    }
    if (roleToUpdateError) {
      console.log("Error fetching role listing:", roleToUpdateError);
    }
  }, [roleData, roleError, roleToUpdateData, roleToUpdateError]);

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
        <h3 className="text-xl font-medium">Update Role Listing</h3>
      </div>
      <Separator />
      {isLoaded && roleDetails && roleListingData && (
        <UpdateForm
          allSkills={allSkills}
          departments={departments}
          roles={roleDetails}
          roleToUpdateData={roleListingData}
        />
      )}
    </div>
  );
};

export default CreateRole;
