import { Navbar } from "@/components/common/nav/Navbar";
import { NavigationMenuComp } from "@/components/common/nav/NaviagationMenu";

export default function Home() {
  return (
    <div className="w-full font-[family-name:var(--font-geist-sans)] h-screen overflow-auto">
      <header>
        {/* <Navbar /> */}
        <NavigationMenuComp />
      </header>
      <main className="flex flex-col items-center sm:items-start px-8 pt-6 pb-20"></main>
      <footer className="flex flex-col items-center sm:items-start px-8 py-6">
        Footer
      </footer>
    </div>
  );
}
