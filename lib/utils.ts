import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
// e.g.: Wednesday, 04 Oct 2023, 11:59 PM
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

export const fetcher = (url: string) => fetch(url).then((res) => res.json());
