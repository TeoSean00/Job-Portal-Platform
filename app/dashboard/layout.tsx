import "../globals.scss";

import Sidebar from "@/components/Sidebar";
import { Toaster } from "@/components/ui/toaster";
import { inter } from "@/fonts";
import { cn } from "@/lib/utils";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className={cn(inter.className, "dark bg-background text-foreground")}>
      <div className="flex flex-auto">
        <aside>
          <Sidebar />
          <Toaster />
        </aside>
        <main className="grow p-10">{children}</main>
      </div>
    </div>
  );
}
