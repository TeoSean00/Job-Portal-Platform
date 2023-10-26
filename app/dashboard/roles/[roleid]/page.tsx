"use client";

import type { SpecificRoleInfo } from "@/types";

import { useSession } from "@clerk/nextjs";
import React, { useEffect, useState } from "react";

import RoleListing from "@/components/role-page/role-page";

interface PageProps {
  params: { roleid: number };
}
export interface PageData {
  roleid: number;
  roleName: string;
  roleDescription: string;
  skillsRequired: string[];
}

interface RoleAPIResponse {
  [role_id: number]: SpecificRoleInfo;
}

const RolePage = (props: PageProps) => {
  const { session } = useSession();
  const user = session?.user;
  // if (!user?.id || !user?.publicMetadata?.role) {
  //   throw new Error("User token or role is not defined!");
  // }
  const userToken = user?.id;
  const userRole = user?.publicMetadata?.role;
  const [data, setData] = useState<PageData>();
  const fetchRoleDetail = () => {
    fetch(`/api/role/role_info?role_id=${props.params.roleid}`, {
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
        Object.keys(apiData).forEach((item: string) => {
          const role = apiData[Number(item)];
          const temp = {
            roleid: props.params.roleid,
            roleName: role.role_name,
            roleDescription: role.role_desc,
            skillsRequired: role.skills.map((skill) => skill.skill_name),
          };
          setData(temp);
        });
      })
      .catch((err) => {
        console.log("Error fetching role details:", err);
      });
  };
  // const data: PageData = {
  //   roleid: props.params.roleid,
  //   roleName: "Software Engineer",
  //   roleDescription: "Software Engineer",
  //   skillsRequired: ["Python", "React", "Javascript", "Java", "C++", "C#"],
  // };
  useEffect(() => {
    fetchRoleDetail();
  }, []);
  return (
    <>
      {data === undefined ? (
        <div>Loading...</div>
      ) : (
        <RoleListing data={data} />
      )}
      </>
  );
};
export default RolePage;
