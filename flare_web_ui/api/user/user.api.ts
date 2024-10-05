import axios from "@/lib/axios";
import { User, UserAuthPayload } from "@/types/user";

const loginUser = async (data: UserAuthPayload) => {
  try {
    const response = await axios.post<User>("/api/v1/auth/login", data);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export { loginUser };
