import type { Metadata } from "next";

import "./globals.scss";
import { ClerkProvider } from "@clerk/nextjs";

import { AuthProvider } from "@/components/AuthProvider";
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
          colorPrimary: "#2563eb",
        },
      }}
    >
      <AuthProvider>
        <html lang="en">
          <body
            className={cn(
              inter.className,
              "h-screen bg-background text-foreground",
            )}
          >
            <main>{children}</main>
          </body>
        </html>
      </AuthProvider>
    </ClerkProvider>
  );
}
