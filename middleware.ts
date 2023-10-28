import { authMiddleware } from "@clerk/nextjs";

/**
 * This middleware will redirect the user to the login page if they are not authenticated.
 * Public routes are not redirected.
 */
export default authMiddleware({
  publicRoutes: ["/"],
});

// regex to exclude static files and api routes
export const config = {
  matcher: ["/((?!.+\\.[\\w]+$|_next).*)", "/", "/(api|trpc)(.*)"],
};
