import React, { useCallback, useEffect, useRef, useState, } from "react";

export const AutoComplete = () => {
  const [result, setResult] = useState<any[]>([]);
  const [search, setSearch] = useState<string>("");
  const [focus, setFocus] = useState<boolean>(false);
  const [focusIndex, setFocusIndex] = useState<number>(0);

  const debounce = (fn: any, delay: number) => {
    let timer: any;
    return (...args: any) => {
      if (timer) {
        clearTimeout(timer);
      }
      timer = setTimeout(() => {
        fn(...args);
      }, delay);
    };
  }

  useEffect(() => {
    setResult([]);

    if (!focus) {
      return;
    }

    const fetchData = async () => {
      const resp = await fetch("https://jsonplaceholder.typicode.com/users");
      const data: any[] = await resp.json();
      const filteredData = data.filter((item) =>
        item.name.toLowerCase().includes(search.toLowerCase())
      );
      setResult(filteredData);
      console.log(`fetch data caused by query change: ${search}`);
    };

    debounce(fetchData, 200)()
  }, [search, focus]);

  const handleKeyDown = useCallback(
    (key: string) => {
      if (!focus) {
        setFocus(true);
      }

      if (key === "ArrowDown") {
        setFocusIndex((focusIndex + 1) % result.length);
      } else if (key === "ArrowUp") {
        setFocusIndex((focusIndex - 1 + result.length) % result.length);
      } else if (key === "Enter") {
        setSearch(result[focusIndex].name);
        setFocus(false);
      }
    },
    [focusIndex, result, focus]
  );

  useEffect(() => {
    ulRef.current
      ?.querySelector(`li:nth-child(${focusIndex})`)
      ?.scrollIntoView();
  }, [focusIndex]);


  const ulRef = useRef<HTMLUListElement>(null);

  return (
    <div className="flex flex-col items-center justify-center w-screen">
      <h1>AutoComplete</h1>
      <br />
      <div className="relative">
        <input
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          type="text"
          placeholder="Search"
          onFocus={() => setFocus(true)}
          onBlur={() => setFocus(false)}
          className="border-2 border-gray-900 rounded-xl p-2"
          onKeyDown={(e) => {
            handleKeyDown(e.key);
          }}
        />
        {focus && (
          <ul
            className="absolute bg-gray-900 w-96 p-2 m-1 rounded-xl h-48 overflow-y-auto"
            ref={ulRef}
          >
            {result.map((item, index) => {
              return (
                <li
                  className={`
                    m-1 
                    ${focusIndex === index ? " bg-gray-700" : ""}
                  `}
                  key={item.id}
                >
                  {item.name}
                </li>
              );
            })}
          </ul>
        )}
      </div>
    </div>
  );
};
