import React from "react";

import { ModeToggle } from "@/components/ui/theme-toggle";

import { useShallow } from "zustand/react/shallow";
import { useStore } from "@/store/store";

export default function UserNavbar() {
  const { email, full_name, fetchUser } = useStore(
    useShallow((state) => ({
      email: state.email,
      full_name: state.full_name,
      fetchUser: state.fetchUser,
    }))
  );

  React.useEffect(() => {
    fetchUser();
  }, [fetchUser]);

  return (
    <div className="flex items-center gap-5">
      <div className="flex flex-row items-center">
        {email && <div className="text-base">{full_name}</div>}
      </div>
      <ModeToggle />
    </div>
  );
}
