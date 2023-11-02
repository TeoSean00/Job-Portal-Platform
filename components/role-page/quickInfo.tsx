"use client";

import type { PageData } from "../../app/dashboard/roles/[roleid]/page";

import { useSession } from "@clerk/nextjs";
import Link from "next/link";
import React, { useContext } from "react";

import { AuthContext } from "@/components/AuthProvider";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog";
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
  const { session } = useSession();
  const user = session?.user;
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

  return (
    <Card className="w-full">
      <div className="flex items-center justify-between pr-6">
        <CardHeader>
          <CardTitle>{roleInfo.roleName}</CardTitle>
          <CardDescription>{roleInfo.roleDepartment}</CardDescription>
        </CardHeader>
        {user?.publicMetadata.role === "hr" ? (
          <Link href={`/dashboard/roles/applicants/${roleInfo.roleid}`}>
            <Button>Applicants</Button>{" "}
          </Link>
        ) : (
          ""
        )}
      </div>
      <CardContent>
        <div className="flex flex-col pb-10">
          <h4 className=" font-bold">Role Details</h4>
          <span>Location: {roleInfo.roleLocation}</span>
          <span>Salary Range: $60,000 - $80,000</span>
          <span>
            Skills Required:{" "}
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
        <div className="flex flex-col pb-8">
          <h4 className=" font-bold">Role Description</h4>
          <span> {roleInfo.roleDescription}</span>
        </div>
        <div className="flex flex-col">
          <h4 className=" font-bold">Additional Information</h4>
          <span> {roleInfo.roleListingDesc}</span>
        </div>
      </CardContent>
      <CardFooter className="flex space-x-4">
        <AlertDialog>
          <AlertDialogTrigger className="inline-flex h-10 items-center justify-center rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground ring-offset-background transition-colors hover:bg-primary/90 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50">
            Apply
          </AlertDialogTrigger>
          <AlertDialogContent>
            <AlertDialogHeader>
              <AlertDialogTitle>
                Are you sure you want to apply for this role?
              </AlertDialogTitle>
              <AlertDialogDescription>
                We will send you application to HR to review.
              </AlertDialogDescription>
            </AlertDialogHeader>
            <AlertDialogFooter>
              <AlertDialogCancel>Cancel</AlertDialogCancel>
              <AlertDialogAction onClick={applyRole}>Apply</AlertDialogAction>
            </AlertDialogFooter>
          </AlertDialogContent>
        </AlertDialog>
        <Button variant="outline">Save</Button>
      </CardFooter>
    </Card>
  );
}
