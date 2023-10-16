"use client";

import * as React from "react";

import { Button } from "@/components/ui/button";
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
export function SkillMatch(props: SkillInfo) {
  const [obtainedSkills, setObtainedSkills] = React.useState(
    props.skillObtained,
  );
  const [missingSkills, setMissingSkills] = React.useState(props.skillMissing);
  return (
    <Card className="w-full">
      <CardHeader>
        <CardTitle>Skill Match</CardTitle>
        {/* <CardDescription>Department Name</CardDescription> */}
      </CardHeader>
      <CardContent></CardContent>
    </Card>
  );
}
