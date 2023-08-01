"use client";

import { useState } from "react";

export function CartItem({ item }: any) {
  const [count, setCount] = useState(item.count);
  return (
    <div>
      <h1>{item.name}</h1>
      <p>가격: {item.price}</p>
      <p>수량: {count}</p>
      <button onClick={() => setCount(count + 1)}>버튼</button>
    </div>
  );
}
