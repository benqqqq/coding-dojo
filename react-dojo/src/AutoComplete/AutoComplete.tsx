import React, { useCallback, useEffect, useRef, useState } from "react";
import { useSearchData } from "./hooks";

export const AutoComplete = () => {
  const [focus, setFocus] = useState<boolean>(false);
  const [focusIndex, setFocusIndex] = useState<number>(0);
  const [query, result, search] = useSearchData();

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
        search(result[focusIndex].name);
        setFocus(false);
      }
    },
    [focus, focusIndex, result]
  );

  useEffect(() => {
    ulRef.current
      ?.querySelector(`li:nth-child(${focusIndex})`)
      ?.scrollIntoView();
  }, [focusIndex]);

  useEffect(() => {
    if (focus) {
      search(query);
    }
  }, [focus]);

  const ulRef = useRef<HTMLUListElement>(null);

  return (
    <div className="flex flex-col items-center justify-center w-screen">
      <h1>AutoComplete</h1>
      <br />
      <div>
        DEBUG
        <ul>
          <li>{`focus: ${focus ? "true" : "false"}`}</li>
          <li>{`query: ${query}`}</li>
          <li>{`result.length: ${result.length}`}</li>
        </ul>
      </div>
      <div className="relative">
        <input
          value={query}
          onChange={(e) => search(e.target.value)}
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
