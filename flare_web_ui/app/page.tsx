import Footer from "@/components/common/footer/Footer";
import { NavigationMenuComp } from "@/components/common/nav/NaviagationMenu";
import Home from "@/components/root/home/Home";

export default function HomePage() {
  return (
    <div className="w-full font-[family-name:var(--font-geist-sans)] h-screen overflow-auto">
      <header>
        <NavigationMenuComp />
      </header>
      <main className="flex flex-col items-center sm:items-start">
        <Home />
      </main>
      <Footer />
    </div>
  );
}
