"use client";

import type { PageData } from "../../app/dashboard/roles/[roleid]/page";

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

interface RoleData {
  data: PageData;
}
export function QuickInfo(props: RoleData) {
  const [roleInfo, setRoleInfo] = React.useState(props.data);
  // console.log(roleInfo);
  return (
    <Card className="w-full">
      <CardHeader>
        <CardTitle>{roleInfo.roleName}</CardTitle>
        <CardDescription>{roleInfo.roleDepartment}</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="flex flex-col pb-10">
          <h4 className=" font-bold">Role Details</h4>
          <span>Location:{roleInfo.roleLocation}</span>
          <span>Salary Range:$60,000 - $80,000</span>
          <span>
            Skills Required:
            <ul className="inline-block">
              {roleInfo.skillsRequired.map((skill, index) => (
                <li key={index} className="inline-block pr-2">
                  {index !== roleInfo.skillsRequired.length - 1
                    ? `${skill},`
                    : `${skill}`}
                </li>
              ))}
            </ul>
          </span>
        </div>
        <div className="flex flex-col">
          <h4 className=" font-bold">Role Description</h4>
          <span> {roleInfo.roleDescription}</span>
        </div>
      </CardContent>
      <CardFooter className="flex space-x-4">
        <Button>Apply</Button>
        <Button variant="outline">Save</Button>
      </CardFooter>
    </Card>
  );
}
