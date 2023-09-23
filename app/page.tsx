import Link from "next/link";

export default function Home() {
  return (
    <main className="flex h-full items-center justify-center">
      Get started by editing&nbsp;
      <Link href={`/api/python`}>
        <code className="rounded-lg border border-border p-2 font-bold">
          /api/index
        </code>
      </Link>
    </main>
  );
}
