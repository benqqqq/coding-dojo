from typing import Dict

from sortedcontainers import SortedDict


class TimeMap:
    def __init__(self):
        self.mapping: Dict[str, SortedDict] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = SortedDict()

        self.mapping[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping:
            return ''

        index = self.mapping[key].bisect_right(timestamp)
        if index == 0:
            return ''
        return self.mapping[key].peekitem(index - 1)[1]
