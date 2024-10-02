import axios from "axios";

axios.defaults.baseURL = `${process.env.NEXT_PUBLIC_BACKEND_API}`;
axios.defaults.timeout = 1000;

export default axios;
