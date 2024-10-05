import React from "react";

import { Card } from "@/components/ui/card";
import { cn } from "@/lib/utils";

export default function GlossyCard({
  children,
  className,
  ...props
}: Readonly<{ children: React.ReactNode; className?: string }>) {
  return (
    <Card
      className={cn(
        "h-full w-full bg-blue-300 rounded-md bg-clip-padding backdrop-filter backdrop-blur-lg bg-opacity-10 border border-gray-100 p-5",
        className
      )}
    >
      {children}
    </Card>
  );
}
