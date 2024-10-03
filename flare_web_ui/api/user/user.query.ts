import { useQuery } from "react-query";
import { getUser } from "./user.api";

function useGetUser() {
  return useQuery({
    queryKey: ["user"],
    queryFn: getUser,
    refetchOnWindowFocus: false,
  });
}

export { useGetUser };
