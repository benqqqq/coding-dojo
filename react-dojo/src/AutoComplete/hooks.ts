import { useCallback, useState } from "react";
import { getUsers } from "./apis";
import { User } from "./Definitions";
import { debounce } from "./behaviorUtil";

const filterQueryData = (query: string, data: User[]) => {
  return data.filter((user) =>
    user.name.toLowerCase().includes(query.toLowerCase())
  );
};

export const useSearchData = (): [string, User[], (q: string) => void] => {
  const [result, setResult] = useState<User[]>([]);
  const [query, setQuery] = useState<string>("");

  const search = useCallback(
    async (q: string) => {
      setQuery(q);
      const users = await getUsers();
      setResult(filterQueryData(query, users));
    },
    [query]
  );

  return [query, result, search];
};
