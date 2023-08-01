import { CartItem } from "./components/CartItem";

export default function Cart() {
  const products = [
    {
      name: "ㅁㄴㅇㄹ",
      price: 500,
      count: 1,
    },
    {
      name: "qwer",
      price: 1300,
      count: 2,
    },
    {
      name: "szsf sad",
      price: 2500,
      count: 1,
    },
  ];
  return (
    <div>
      {products.map((value, idx) => (
        <CartItem key={`${idx}`} item={value} />
      ))}
    </div>
  );
}
