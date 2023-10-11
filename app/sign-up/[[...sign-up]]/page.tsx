import { SignInButton } from "@clerk/nextjs";

import { Button } from "@/components/ui";

/**
 * signup page not in used
 */
export default function Page() {
  return (
    <div className="flex h-screen w-screen flex-col items-center justify-center gap-y-2">
      Sign Up page not in used.
      <SignInButton>
        <Button variant={"outline"}> Sign in</Button>
      </SignInButton>
    </div>
  );
}
