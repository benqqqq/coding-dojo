class TrieNode:
    def __init__(self, letter: str | None = None, is_end_of_word: bool = False) -> None:
        super().__init__()

        self.letter = letter
        self.links_map = {}
        self.is_end_of_word = is_end_of_word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        word_length = len(word)
        node = self.root
        for i in range(word_length):
            is_end_of_word = i == word_length - 1
            letter = word[i]

            if letter in node.links_map:
                node.links_map[letter].is_end_of_word = node.links_map[letter].is_end_of_word or is_end_of_word
            else:
                node.links_map[letter] = TrieNode(letter, is_end_of_word)

            node = node.links_map[letter]

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.links_map:
                return False
            node = node.links_map[letter]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter not in node.links_map:
                return False
            node = node.links_map[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
