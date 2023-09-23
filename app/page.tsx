import { SignedOut, SignInButton } from "@clerk/nextjs";

import { Button } from "@/components/ui";

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
    </main>
  );
}
