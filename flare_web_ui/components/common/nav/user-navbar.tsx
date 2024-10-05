import React from "react";

import { ModeToggle } from "@/components/ui/theme-toggle";

import { useShallow } from "zustand/react/shallow";
import { useStore } from "@/store/store";

import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function UserNavbar() {
  const { email, full_name } = useStore(
    useShallow((state) => ({
      email: state.email,
      full_name: state.full_name,
    }))
  );

  return (
    <div className="flex items-center gap-5">
      <div className="flex flex-row items-center">
        {email ? (
          <div className="text-base">{full_name}</div>
        ) : (
          <Button variant={"default"} asChild>
            <Link href="/login">Login</Link>
          </Button>
        )}
      </div>
      <ModeToggle />
    </div>
  );
}
