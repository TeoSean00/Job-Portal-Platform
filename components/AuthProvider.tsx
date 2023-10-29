"use client";

import type { FetcherOptions, User } from "@/types";

import { useSession } from "@clerk/nextjs";
import { createContext } from "react";
import useSWR from "swr";

import { fetcher } from "@/lib/utils";

export const AuthContext = createContext<number | undefined>(undefined);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const { session } = useSession();
  const user = session?.user;

  const userId = user?.id;

  const { data } = useSWR<User, Error>(
    // eslint-disable-next-line @typescript-eslint/restrict-template-expressions
    `/api/staff/clerk/${userId}`,
    fetcher,
  );

  const staffId = data?.staff_id;

  return (
    <AuthContext.Provider value={staffId}>{children}</AuthContext.Provider>
  );
}
