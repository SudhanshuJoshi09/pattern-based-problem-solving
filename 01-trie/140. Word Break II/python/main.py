class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_eow = False


class Trie:
    def __init__(self):
        self.trie = TrieNode()
        self.memo = {}

    def insert_impl(self, node: TrieNode, key: str, idx: int):
        """
        Questions: Is there a possibility that node is none ?
        -> The first node of the trie is always initializied by us while the
        Trie is being declared, and with every subsequent iteration the child
        node is fetched or Created if not present, which means that there
        would never be a possiblity where node would be null
        """

        if idx == len(key):
            node.is_eow = True
            return

        child = node.children.get(key[idx], TrieNode())
        node.children[key[idx]] = child

        self.insert_impl(child, key, idx+1)

    def search_impl(self, node: TrieNode, key: str, idx: int) -> bool:
        if node is None:
            return False
        if idx == len(key):
            return node.is_eow

        child = node.children.get(key[idx], None)

        return self.search_impl(child, key, idx + 1)

    def word_break_impl(self, node: TrieNode, key: str, idx: int) -> List[str]:
        if (node, idx) in self.memo.keys():
            return self.memo[(node, idx)]
        if node is None:
            self.memo[(node, idx)] = []
            return []
        if idx == len(key):
            # missed this condition, we only return a word if the node is eow.
            result = [""] if node.is_eow else []
            self.memo[(node, idx)] = result
            return result

        child = node.children.get(key[idx], None)
        res1 = [key[idx] + x for x in self.word_break_impl(child, key, idx+1)]

        # Consider this word seperately, add space after the eow.
        if node.is_eow:
            # Look for the next word, consider this word as done .
            res2 = self.word_break_impl(self.trie, key, idx)
            res2 = [" " + x for x in res2]
            self.memo[(node, idx)] = res1 + res2
            return res1 + res2

        self.memo[(node, idx)] = res1
        return res1

    def insert(self, key: str):
        self.insert_impl(self.trie, key, 0)

    def search(self, key: str):
        return self.search_impl(self.trie, key, 0)

    def word_break(self, key: str):
        return self.word_break_impl(self.trie, key, 0)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        return trie.word_break(s)
