import "./globals.css";
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import Link from "next/link";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Link href={"/"}>홈으로꼬</Link>
        <Link href={"list"}>리스트로꼬</Link>
        <Link href={"cart"}>카트로꼬</Link>
        {children}
      </body>
    </html>
  );
}
