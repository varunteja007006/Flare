"use client";
import React from "react";

import GlossyCard from "@/components/common/cards/glossy-card";

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";

import { useToast } from "@/hooks/use-toast";

import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { LoginFormSchema } from "@/schema/auth/login";
import { useMutation } from "react-query";
import { loginUser } from "@/api/user/user.api";
import { User } from "@/types/user";
import { useStore } from "@/store/store";
import { useShallow } from "zustand/react/shallow";

export default function LoginMain() {
  const { toast } = useToast();

  const { updateUser } = useStore(
    useShallow((state) => ({
      updateUser: state.updateUser,
    }))
  );

  const form = useForm<z.infer<typeof LoginFormSchema>>({
    resolver: zodResolver(LoginFormSchema),
  });

  function onSuccess(response: any) {
    updateUser("full_name", response.full_name);
    updateUser("email", response.email);
    toast({
      title: "Login Successful",
      description: `Welcome ${response.full_name}!`,
      variant: "success",
    });
  }

  function onError(error: Error) {
    console.error(error);
  }

  const login = useMutation({
    mutationFn: loginUser,
    onSuccess,
    onError,
  });

  function onSubmit(data: z.infer<typeof LoginFormSchema>) {
    login.mutate(data);
  }

  return (
    <div className="flex flex-col md:items-center h-[calc(100vh-10rem)] justify-center items-start">
      <GlossyCard className="flex flex-col items-start justify-start gap-2 h-fit max-w-[280px]">
        <div className="text-lg font-semibold">Login</div>
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
            <FormField
              control={form.control}
              name="username"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Username</FormLabel>
                  <FormControl>
                    <Input placeholder="username" {...field} />
                  </FormControl>
                  <FormDescription>
                    This is your public display name.
                  </FormDescription>
                  <FormMessage />
                </FormItem>
              )}
            />
            <FormField
              control={form.control}
              name="password"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Password</FormLabel>
                  <FormControl>
                    <Input type="password" placeholder="password" {...field} />
                  </FormControl>
                  <FormDescription>
                    This is your public display name.
                  </FormDescription>
                  <FormMessage />
                </FormItem>
              )}
            />
            <Button type="submit" variant="success">
              Submit
            </Button>
          </form>
        </Form>
      </GlossyCard>
    </div>
  );
}
