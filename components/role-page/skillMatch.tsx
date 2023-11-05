"use client";

import * as React from "react";

import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export interface SkillInfo {
  skillObtained: string[];
  skillMissing: string[];
}
interface SkillData {
  data: SkillInfo | undefined;
}
export function SkillMatch(props: SkillData) {
  const [obtainedSkills, setObtainedSkills] = React.useState(
    props.data?.skillObtained || [],
  );
  const [missingSkills, setMissingSkills] = React.useState(
    props.data?.skillMissing || [],
  );
  // console.log(props);
  return (
    <Card className="w-full">
      <CardHeader>
        <CardTitle>Skill Match</CardTitle>
        {/* <CardDescription>Department Name</CardDescription> */}
      </CardHeader>
      <CardContent>
        <div className="my-3">
          <h4 className=" font-bold">Skills Obtained</h4>
          <ul className="flex space-x-2">
            {obtainedSkills.map((skill, index) => (
              <li key={index} className="">
                <Badge className="py-1 text-lg" variant="default">
                  {skill}
                </Badge>{" "}
              </li>
            ))}
          </ul>
        </div>
        <div>
          <h4 className=" font-bold">Skills Missing</h4>
          <ul className="flex space-x-2">
            {missingSkills.map((skill, index) => (
              <li key={index} className="">
                <Badge className="py-1 text-lg" variant="destructive">
                  {skill}
                </Badge>
              </li>
            ))}
          </ul>
        </div>
      </CardContent>
    </Card>
  );
}
