"use client";

import type { SidebarNavItem } from "@/types";

import { ChevronRight, List, UserCircle, UserPlus } from "lucide-react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import React, { useState } from "react";

import { HamburgerToggle } from "./HamburgerToggle";

import { poppins } from "@/fonts";
import { cn } from "@/lib/utils";

const sidebarLinks: SidebarNavItem[] = [
  {
    title: "Profile",
    href: "/dashboard/profile",
    icon: <UserCircle />,
  },
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

const Sidebar = () => {
  const [open, setOpen] = useState(true);
  const [mobileMenu, setMobileMenu] = useState(false);

  const location = usePathname();
  return (
    <div>
      <div
        className={`${
          open ? "w-52" : "w-fit"
        }  relative hidden h-screen border-r border-border px-3 pt-4 sm:block`}
      >
        <div
          className="absolute -right-6 top-7 z-10 flex h-10 w-10 cursor-pointer items-center justify-center rounded-full border-2 border-border bg-border p-2"
          onClick={() => setOpen(!open)}
        >
          <ChevronRight className={cn({ "rotate-180": open })} />
        </div>

        <ul className="flex flex-col gap-y-3 px-2">
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
                  className={cn({ hidden: !open }, "origin-left duration-300")}
                >
                  {link.title}
                </span>
              </li>
            </Link>
          ))}
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
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
