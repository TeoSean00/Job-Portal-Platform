import { SignedIn, SignedOut, SignIn, SignInButton } from "@clerk/nextjs";
import Link from "next/link";

import { Button } from "@/components/ui/Button";

export default function Home() {
  return (
    <main className="flex h-screen flex-col items-center justify-center gap-y-5">
      <h1 className="text-4xl font-bold">
        Welcome to <span className=" text-primary">Portal</span>
      </h1>
      <SignedOut>
        <SignInButton>
          <Button variant={"outline"}> Sign in</Button>
        </SignInButton>
      </SignedOut>
      <SignedIn>
        <Link href="/dashboard">
          <Button variant={"outline"}>Dashboard </Button>
        </Link>
      </SignedIn>
    </main>
  );
}
