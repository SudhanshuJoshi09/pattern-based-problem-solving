class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_eow = False


class Trie:
    def __init__(self):
        self.trie = TrieNode()
        self.memo = {}

    def str_impl(self, node):
        result = ""
        next_lvl = ""
        for k in node.children.keys():
            result = result + " " + k
            next_lvl += self.str_impl(node.children[k])
        return result + "  EOW  " + str(node.is_eow) + " \n " + next_lvl

    def __str__(self):
        return self.str_impl(self.trie)

    def insert_impl(self, node: TrieNode, key: str):
        if len(key) == 0:
            node.is_eow = True
            return

        child = node.children.get(key[0], TrieNode())
        node.children[key[0]] = child

        self.insert_impl(child, key[1:])

    def search_impl(self, node: TrieNode, key: str) -> bool:
        if node is None:
            return False
        if len(key) == 0:
            return node.is_eow
        child = node.children.get(key[0], None)

        return self.search_impl(child, key[1:])

    # Question: What does this function do ?
    # Answer: Checks weather we can break the string into two parts,
    # where the first part is present in dictionary
    # and the second part which is recursively checked again.
    def check_word_break_impl(self, node: TrieNode, key: str, idx: int) -> bool:
        if (node, idx) in self.memo:
            return self.memo[(node, idx)]

        if node is None:
            self.memo[(node, idx)] = False
            return False
        if len(key) == idx:
            self.memo[(node, idx)] = node.is_eow
            return node.is_eow

        child = node.children.get(key[idx], None)

        if node.is_eow:
            # Just continue like you did not see is_end_of_word or accept the reality and move on with the next word.
            result = self.check_word_break_impl(
                child, key, idx + 1
            ) or self.check_word_break_impl(self.trie, key, idx)
            self.memo[(node, idx)] = result
            return result

        result = self.check_word_break_impl(child, key, idx + 1)
        self.memo[(node, idx)] = result

        return result

    def insert(self, key: str):
        self.insert_impl(self.trie, key)

    def search(self, key: str) -> bool:
        return self.search_impl(self.trie, key)

    def check_word_break(self, key: str) -> bool:
        return self.check_word_break_impl(self.trie, key, 0)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        trie.search("leet")
        return trie.check_word_break(s)


if __name__ == "__main__":
    solution = Solution()
    solution.wordBreak("leetcode", ["leet", "code"])
