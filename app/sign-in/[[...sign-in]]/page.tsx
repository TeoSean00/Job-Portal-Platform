import { SignIn } from "@clerk/nextjs";

const SignInPage = () => (
  <div className="flex h-screen w-screen items-center justify-center">
    <SignIn redirectUrl={`/Dashboard`} />
  </div>
);

export default SignInPage;
