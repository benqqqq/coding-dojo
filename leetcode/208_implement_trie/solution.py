from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    val: str
    left: Node | None = None
    right: Node | None = None


class Trie:
    def __init__(self):
        self.root: Node | None = None

    def insert(self, word: str) -> None:
        if not self.root:
            self.root = Node(val=word)
            return

        node = self.root
        while node:
            left_or_right = 'left' if node.val <= word else 'right'
            if next_node := getattr(node, left_or_right):
                node = next_node
            else:
                setattr(node, left_or_right, Node(val=word))
                break

    def search(self, word: str) -> bool:
        node = self.root
        while node:
            if node.val == word:
                return True
            if node.val <= word:
                node = node.left
            else:
                node = node.right
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        while node:
            if node.val.startswith(prefix):
                return True
            if node.val <= prefix:
                node = node.left
            else:
                node = node.right
        return False


if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')
    assert trie.search('apple') is True
    assert trie.search('app') is False
    assert trie.startsWith('app') is True
    trie.insert('app')
    assert trie.search('app') is True

