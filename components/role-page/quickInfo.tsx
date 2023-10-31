"use client";

import type { PageData } from "../../app/dashboard/roles/[roleid]/page";

import React, { useEffect, useContext } from "react";

import { AuthContext } from "@/components/AuthProvider";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { ToastAction } from "@/components/ui/toast";
import { toast } from "@/components/ui/use-toast";

interface RoleData {
  data: PageData;
}
export function QuickInfo(props: RoleData) {
  const staffId = useContext(AuthContext);
  const [roleInfo, setRoleInfo] = React.useState(props.data);
  const applyRole = () => {
    fetch(`/api/staff/role/${staffId}/${roleInfo.roleid}`, {
      method: "POST",
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
      .then((apiData) => {
        toast({
          title: "Successful Appllication!",
          description: "Please wait for HR to process your application.",
          action: <ToastAction altText="Dismiss">Dismiss</ToastAction>,
        });
      })
      .catch((err) => {
        toast({
          title: "Role Already Applied for!",
          description: "Please apply for a different role",
          action: <ToastAction altText="Dismiss">Dismiss</ToastAction>,
        });
        console.log("Error fetching role details:", err);
      });
  };
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
        <Button onClick={applyRole}>Apply</Button>
        <Button variant="outline">Save</Button>
      </CardFooter>
    </Card>
  );
}
