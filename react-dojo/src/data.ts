
// define product type
export type Product = {
  title: string;
  id: number;
}

export const products: Product[] = [
  { title: 'Cabbage', id: 1 },
  { title: 'Garlic', id: 2 },
  { title: 'Apple', id: 3 },
];


// define user type
export type User = {
  name: string;
}

export const user: User = {
  name: "John",
};
