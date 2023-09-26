import type { Metadata } from "next";
import "./globals.scss";

import { ClerkProvider } from "@clerk/nextjs";

import { inter } from "@/fonts";
import { cn } from "@/lib/utils";

export const metadata: Metadata = {
  title: "Portal",
  description: "Internal Skill-based Role Portal",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <ClerkProvider
      appearance={{
        variables: {
          colorPrimary: "#16a34a",
        },
      }}
    >
      <html lang="en">
        <body
          className={cn(
            inter.className,
            "dark h-screen bg-background text-foreground",
          )}
        >
          <main>{children}</main>
        </body>
      </html>
    </ClerkProvider>
  );
}
