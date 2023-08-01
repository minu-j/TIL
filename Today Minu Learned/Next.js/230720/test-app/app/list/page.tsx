import Image from "next/image";

export default function List() {
  const products = ["토마토", "스파게티", "로제파스타", "무슨무슨파스타"];
  return (
    <div>
      {products.map((value, idx) => (
        <>
          <div key={`shop-list-${idx}`}>{value}</div>
          <Image
            width={100}
            height={100}
            src={"https://picsum.photos/200/300?blur"}
            alt="sdf"
          ></Image>
        </>
      ))}
    </div>
  );
}
