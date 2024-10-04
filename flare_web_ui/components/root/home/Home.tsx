import React from "react";

export default function Home() {
  return (
    <div className=" w-full">
      <div className="min-h-screen relative w-full bg-sky-50">
        <div className="bg-gradient-to-l from-sky-50 via-sky-100 to-sky-50 h-[70%] w-[40%] absolute top-11 blur-md rounded-full right-0"></div>
        <div className="bg-gradient-to-l from-sky-50 via-sky-100 to-sky-50 h-[70%] w-[40%] absolute top-11 blur-md rounded-full left-0"></div>
        <div className="bg-gradient-to-l from-sky-50 via-sky-100 to-sky-50 h-[40%] w-[20%] absolute left-[20%] blur-md rounded-full bottom-0"></div>
      </div>
      <div className="bg-gray-200 min-h-screen w-full"></div>
      <div className="bg-gray-200 min-h-screen w-full"></div>
    </div>
  );
}
