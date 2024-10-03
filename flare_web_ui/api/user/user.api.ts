import axios from "@/lib/axios";
import { User } from "@/types/user";

const getUser = async () => {
  try {
    const response = await axios.post<User>("/api/v1/auth/login", {
      username: "varun",
      password: "varun123",
    });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export { getUser };
