export type User = {
  email: string;
  full_name: string;
  token: string;
  created: string;
};

export type UserAuthPayload = {
  username: string;
  password: string;
};
