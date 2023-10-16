"use client";

import type { PageData } from "../../app/dashboard/roles/[roleid]/page";
import type { SkillInfo } from "@/components/role-page/skillMatch";

import * as React from "react";

import { QuickInfo } from "@/components/role-page/quickInfo";
import { SkillMatch } from "@/components/role-page/skillMatch";

interface RoleData {
  data: PageData;
}
const RoleListing = (props: RoleData) => {
  const [roleInfo, setRoleInfo] = React.useState(props.data);
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
