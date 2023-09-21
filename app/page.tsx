import Link from "next/link";

export default function Home() {
  return (
    <main>
      Get started by editing&nbsp;
      <Link href={`/api/python`}>
        <code className="font-mono font-bold">/api/index</code>
      </Link>
    </main>
  );
}
