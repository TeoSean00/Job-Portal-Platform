import type { Dispatch, SetStateAction } from "react";

import { Menu } from "lucide-react";

import { cn } from "@/lib/utils";

export const HamburgerToggle = ({
  setMobileMenu,
  mobileMenu,
}: {
  setMobileMenu: Dispatch<SetStateAction<boolean>>;
  mobileMenu: boolean;
}) => (
  <button
    className={cn("hamburger block focus:outline-none sm:hidden", {
      open: mobileMenu,
    })}
    onClick={() => setMobileMenu(!mobileMenu)}
  >
    <Menu className="h-fit w-10 rounded-lg border border-border p-2 hover:bg-secondary" />
  </button>
);
