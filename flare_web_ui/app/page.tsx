import { Navbar } from "@/components/common/nav/Navbar";

export default function Home() {
  return (
    <div className="min-h-screen w-full font-[family-name:var(--font-geist-sans)]">
      <header>
        <Navbar />
      </header>
      <main className="flex flex-col items-center sm:items-start px-8 pt-6 pb-20 ">
        Home
      </main>
      <footer className="flex flex-col items-center sm:items-start px-8 py-6">
        Footer
      </footer>
    </div>
  );
}
