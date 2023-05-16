import { getJson } from './apiUtils';

export const getUsers = async () => {
  console.log("getUsers api called");
  return await getJson("https://jsonplaceholder.typicode.com/users")
}