import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

const LOGIN_ROUTES = ["/login", "/sign-in"];

// This function can be marked `async` if using `await` inside
export function middleware(request: NextRequest) {
  let token = request.cookies.get("token");
  let access_token = request.cookies.get("access_token");
  let refresh_token = request.cookies.get("refresh_token");
  if (!!token?.value && LOGIN_ROUTES.includes(request.nextUrl.pathname)) {
    return NextResponse.redirect(new URL("/", request.url));
  }
  console.log("pathname:", request.nextUrl.pathname);
  //   const allCookies = request.cookies.getAll();
  //   console.log(allCookies); // => [{ name: 'nextjs', value: 'fast' }]

  //   request.cookies.has("token"); // => true
  //   request.cookies.delete("token");
  //   request.cookies.has("token"); // => false

  // Setting cookies on the response using the `ResponseCookies` API
  //   const response = NextResponse.next();
  //   response.cookies.set({
  //     name: "company",
  //     value: "flare",
  //     path: "/",
  //   });
  //   const cookie = response.cookies.get("company");
  //   console.log(cookie); // => { name: 'vercel', value: 'fast', Path: '/' }
  // The outgoing response will have a `Set-Cookie:vercel=fast;path=/` header.

  // proceed to the requested url
  return NextResponse.next();
}

// See "Matching Paths" below to learn more
// matcher allows you to filter Middleware to run on specific paths.
// filter multiple paths
export const config = {
  matcher: [
    "/about/:path*",
    "/dashboard/:path*",
    /*
     * Match all request paths except for the ones starting with:
     * - api (API routes)
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico, sitemap.xml, robots.txt (metadata files)
     */
    "/((?!api|_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)",
  ],
};
