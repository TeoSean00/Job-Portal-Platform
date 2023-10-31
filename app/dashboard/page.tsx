"use client";

import type { User } from "@/types";

import { useSession } from "@clerk/nextjs";
import Link from "next/link";
import React, { useContext } from "react";
import useSWR from "swr";

import { AuthContext } from "@/components/AuthProvider";
import { Icons } from "@/components/icons/icons";
import { Button } from "@/components/ui";
import { fetcher } from "@/lib/utils";

const DashboardPage = () => {
  const { isLoaded, session } = useSession();
  const user = session?.user;
  const staffId = useContext(AuthContext);
  const { data } = useSWR<User>(`/api/staff/${staffId}`, fetcher);
  return (
    <div className="pt-10">
      <div className="mx-auto flex h-full w-full max-w-md flex-col ">
        {isLoaded && user && data ? (
          <div className="space-y-10 text-center">
            <div className="text-3xl font-semibold tracking-wide [text-wrap:balance]">
              Hi{" "}
              <span className=" text-primary underline decoration-wavy underline-offset-4">
                {data.fname} {data.lname}
              </span>
              !
            </div>
            <div className="mx-auto flex justify-between text-start text-sm">
              <div>
                <div>Welcome to your Role Application Portal</div>
                <div>Start applying to different roles now!</div>
              </div>
              <Link href={`/dashboard/roles`}>
                <Button>Available Roles</Button>
              </Link>
            </div>
          </div>
        ) : (
          <Icons.spinner className="mx-auto my-10 animate-spin text-primary" />
        )}
      </div>
    </div>
  );
};
export default DashboardPage;
