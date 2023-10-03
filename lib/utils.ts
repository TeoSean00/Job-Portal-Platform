import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export const longDateTime = new Intl.DateTimeFormat("en-sg", {
  weekday: "long",
  year: "numeric",
  month: "short",
  day: "2-digit",
  hour: "2-digit",
  minute: "numeric",
  hour12: true,
  timeZone: "Asia/Singapore",
});
