"use client";

import type { PageData } from "../../app/dashboard/roles/[roleid]/page";
import type { SkillInfo } from "@/components/role-page/skillMatch";

import { useSession } from "@clerk/nextjs";
import React, { useEffect, useContext } from "react";

import { AuthContext } from "@/components/AuthProvider";
import { QuickInfo } from "@/components/role-page/quickInfo";
import { SkillMatch } from "@/components/role-page/skillMatch";

interface RoleData {
  data: PageData;
}
const RoleListing = (props: RoleData) => {
  const staffId = useContext(AuthContext);
  const [roleInfo, setRoleInfo] = React.useState(props.data);
  const fetchRoleSkillMatch = () => {
    console.log(staffId, roleInfo.roleid);
    fetch(`/api/staff/role-skills-match/${staffId}/312513332`, {
      method: "GET",
      // headers: {
      //   "user-token": userToken || "", // Make sure it's not undefined
      //   role: String(userRole || ""),
      // },
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network error");
        }
        return res.json();
      })
      .then((apiData: RoleAPIResponse) => {
        console.log("ROLESKILL");
        console.log(apiData);
        // Object.keys(apiData).forEach((item: string) => {
        //   const role = apiData[Number(item)];
        //   const temp = {
        //     roleid: props.params.roleid,
        //     roleName: role.role_name,
        //     roleDescription: role.role_desc,
        //     skillsRequired: role.skills.map((skill) => skill.skill_name),
        //   };
        //   setData(temp);
        // });
      })
      .catch((err) => {
        console.log("Error fetching role details:", err);
      });
  };
  useEffect(() => {
    fetchRoleSkillMatch();
  }, []);
  console.log(roleInfo.roleid);
  const skillInfo: SkillInfo = {
    skillObtained: ["Python", "React", "Javascript"],
    skillMissing: ["Java", "C++", "C#"],
  };
  return (
    <>
      <div className="flex w-full flex-col space-y-10">
        <QuickInfo data={roleInfo} />
        <SkillMatch data={skillInfo} />
      </div>
    </>
  );
};
export default RoleListing;
