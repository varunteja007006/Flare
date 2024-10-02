import { getUser } from "@/api/user/user.api";
import { StateCreator } from "zustand";

type UserState = {
  full_name: string;
  email: string;
};

type UserActions = {
  fetchUser: () => Promise<void>;
};

export type UserSlice = UserState & UserActions;

export const createUserSlice: StateCreator<
  UserSlice,
  [],
  //   [["zustand/immer", never]],
  [],
  UserSlice
> = (set) => ({
  email: "",
  full_name: "",
  fetchUser: async () => {
    const data = await getUser();
    set({
      full_name: data?.full_name ?? "",
      email: data?.email ?? "",
    });
  },
});
