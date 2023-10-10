"use client";

import { useSession, SignOutButton } from "@clerk/nextjs";
import React from "react";

import { Button } from "@/components/ui/Button";

const DashboardPage = () => {
  const { isLoaded, session } = useSession();
  const user = session?.user;

  /* Just to show how we can access user/session data (role, name, image etc) from clerk. */

  return (
    <div className="pt-10">
      <div className="mx-auto flex h-full w-full max-w-md flex-col gap-y-4">
        {session && (
          <div>
            <h2 className="text-primary">Role:</h2>
            <span>{session.user.publicMetadata.role as string}</span>
          </div>
        )}

        {isLoaded && user ? (
          <>
            <div>
              <h2 className="text-primary">User ID:</h2>
              <span>{user.id}</span>
            </div>
          </>
        ) : (
          <div className="px-4 py-5 text-gray-700 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
            Loading user data...
          </div>
        )}

        <SignOutButton>
          <Button variant={"destructive"}>Sign Out</Button>
        </SignOutButton>
      </div>
    </div>
  );
};
export default DashboardPage;
