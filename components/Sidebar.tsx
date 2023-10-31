"use client";

import type { SidebarNavItem, User } from "@/types";

import { SignedIn, useSession, UserButton } from "@clerk/nextjs";
import { ChevronRight, List, UserPlus } from "lucide-react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import React, { useContext, useState } from "react";
import useSWR from "swr";

import { AuthContext } from "./AuthProvider";
import { HamburgerToggle } from "./HamburgerToggle";

import { poppins } from "@/fonts";
import { cn, fetcher } from "@/lib/utils";

const adminSidebarLinks: SidebarNavItem[] = [
  {
    title: "Roles",
    href: "/dashboard/roles",
    icon: <List />,
  },
  {
    title: "Add Role",
    href: "/dashboard/create-role",
    icon: <UserPlus />,
  },
];

const staffSidebarLinks: SidebarNavItem[] = [
  {
    title: "Roles",
    href: "/dashboard/roles",
    icon: <List />,
  },
];

const Sidebar = () => {
  const { isLoaded, session } = useSession();
  const [open, setOpen] = useState(true);
  const [mobileMenu, setMobileMenu] = useState(false);
  const role = session?.user.publicMetadata.role as string;
  const sidebarLinks = role === "hr" ? adminSidebarLinks : staffSidebarLinks;
  const staffId = useContext(AuthContext);
  const { data } = useSWR<User>(`/api/staff/${staffId}`, fetcher);

  const location = usePathname();
  return (
    <div>
      <div
        className={`${
          open ? "w-52" : "w-fit"
        }  relative hidden  h-screen border-r border-border px-3 pt-4 sm:block`}
      >
        <div
          className="absolute -right-6 top-7 z-10 flex h-10 w-10 cursor-pointer items-center justify-center rounded-full border-2 border-border bg-border p-2"
          onClick={() => setOpen(!open)}
        >
          <ChevronRight className={cn({ "rotate-180": open })} />
        </div>

        <ul className="flex h-full flex-col justify-between gap-y-3 px-2">
          <div>
            <Link href="/dashboard">
              <h1
                className={cn(
                  poppins.className,
                  "pb-5  text-center text-lg font-bold text-primary",
                )}
              >
                Portal
              </h1>
            </Link>
            <div className="flex flex-col gap-y-3">
              {sidebarLinks.map((link, index) => (
                <Link
                  key={index}
                  className={cn("border-l-4 border-transparent", {
                    " border-l-4 border-primary": location === link.href,
                  })}
                  href={link.href}
                >
                  <li
                    className={cn(
                      "flex cursor-pointer items-center gap-x-6 rounded-lg border border-transparent px-3 py-2 text-base font-normal hover:border-border",
                      { "rounded-l-none": location === link.href },
                    )}
                  >
                    <span className="p-1">{link.icon}</span>
                    <span
                      className={cn(
                        { hidden: !open },
                        "origin-left duration-300",
                      )}
                    >
                      {link.title}
                    </span>
                  </li>
                </Link>
              ))}
            </div>
          </div>
          <div className="ml-1">
            <li className="mb-5 flex cursor-pointer items-center gap-x-2 text-base font-normal ">
              <div className="rounded-lg border border-transparent px-3 py-2 hover:border-border">
                <UserButton afterSignOutUrl="/" />
              </div>
              {open && isLoaded && data && (
                <span className="text-xs">{data.fname}</span>
              )}
            </li>
          </div>
        </ul>
      </div>

      {/* Mobile Menu */}
      <div className="absolute left-2 top-2 h-fit">
        <HamburgerToggle
          mobileMenu={mobileMenu}
          setMobileMenu={setMobileMenu}
        />
      </div>
      <div className="sm:hidden">
        <div
          className={cn(
            mobileMenu ? "flex" : "hidden",
            "absolute left-6 right-6 top-10 z-50 mt-5 flex-col items-center space-y-2 self-end rounded-lg border border-border bg-background px-24 py-8 font-bold sm:w-auto",
          )}
        >
          <Link href="/dashboard">
            <h1
              className={cn(
                poppins.className,
                "p-2 text-center text-lg font-bold text-primary",
              )}
            >
              Portal
            </h1>
          </Link>
          {sidebarLinks.map((link, index) => (
            <Link
              key={index}
              className={cn(
                {
                  "text-primary underline decoration-wavy underline-offset-8":
                    location === link.href,
                },
                "flex w-full items-center justify-center gap-x-1 rounded-lg py-2 pl-1 pr-3 hover:bg-secondary",
              )}
              href={link.href}
              onClick={() => setMobileMenu(false)}
            >
              <span className="p-1.5 text-2xl">{link.icon}</span>
              <span>{link.title}</span>
            </Link>
          ))}
          <UserButton />{" "}
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
