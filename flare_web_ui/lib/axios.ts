import axios from "axios";

const Axios = axios.create({
  baseURL: `${process.env.NEXT_PUBLIC_BACKEND_API}`,
  timeout: 1000,
});

Axios.defaults.headers.common["Authorization"] = "";

// Add a request interceptor
Axios.interceptors.request.use(
  function (config) {
    return config;
  },
  function (error) {
    return error;
  }
);

// Add a response interceptor
Axios.interceptors.response.use(
  function (response) {
    return response;
  },
  function (error: Error) {
    return error;
  }
);

export { Axios };
