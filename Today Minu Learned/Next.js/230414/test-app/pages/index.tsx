import Image from "next/image";
import { Inter } from "next/font/google";
import Header from "@/src/components/Top";
import Link from "next/link";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  return (
    <div>
      <Header></Header>
      <Link href={"/view/3"}>View</Link>
    </div>
  );
}
