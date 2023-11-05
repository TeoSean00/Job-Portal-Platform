"use client";

import type { PageData } from "../../app/dashboard/roles/[roleid]/page";
import type { SkillInfo } from "@/components/role-page/skillMatch";
import type { SkillMatchType, RoleSkill } from "@/types";

import React, { useEffect, useContext } from "react";

import { AuthContext } from "@/components/AuthProvider";
import { QuickInfo } from "@/components/role-page/quickInfo";
import { SkillMatch } from "@/components/role-page/skillMatch";

interface RoleData {
  data: PageData;
}
interface SkillMatchAPIResponse {
  match: SkillMatchType;
  missing: RoleSkill[];
}
const RoleListing = (props: RoleData) => {
  const staffId = useContext(AuthContext);
  const [roleInfo, setRoleInfo] = React.useState(props.data);
  const [skillInfo, setSkillInfo] = React.useState<SkillInfo>();
  const fetchRoleSkillMatch = () => {
    fetch(`/api/staff/role-skills-match/${staffId}/${roleInfo.roleid}`, {
      method: "GET",
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network error");
        }
        return res.json();
      })
      .then((apiData: SkillMatchAPIResponse) => {
        const obtained = apiData.match.active.concat(apiData.match.in_progress);
        const temp = {
          skillObtained: obtained.map((skill) => skill.skill_name),
          skillMissing: apiData.missing.map((skill) => skill.skill_name),
        };
        setSkillInfo(temp);
      })
      .catch((err) => {
        console.log("Error fetching role details:", err);
      });
  };
  useEffect(() => {
    fetchRoleSkillMatch();
  }, []);
  return (
    <>
      <div className="flex w-full flex-col space-y-10">
        <QuickInfo data={roleInfo} />
        {skillInfo === undefined ? (
          <div>Loading...</div>
        ) : (
          <SkillMatch data={skillInfo} />
        )}
      </div>
    </>
  );
};
export default RoleListing;
