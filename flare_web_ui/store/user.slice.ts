import { StateCreator } from "zustand";

type UserState = {
  full_name: string;
  email: string;
};

type UserActions = {
  fetchUser: () => Promise<void>;
  updateUser: (name: keyof UserState, value: string) => void;
};

export type UserSlice = UserState & UserActions;

export const createUserSlice: StateCreator<
  UserSlice,
  [["zustand/immer", never]],
  [],
  UserSlice
> = (set) => ({
  email: "",
  full_name: "",
  fetchUser: async () => {},
  updateUser: (name, value) => {
    set((state) => {
      state[name] = value;
    });
  },
});
