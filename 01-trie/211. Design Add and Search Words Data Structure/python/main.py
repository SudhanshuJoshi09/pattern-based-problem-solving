class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_eow = False

class Trie:
    def __init__(self):
        self.trie = TrieNode()
    
    def str_impl(self, node):
        children = "".join([x for x in node.children.keys()])
        levels = [children]
        for val in node.children.values():
            levels.append(self.str_impl(val))
        return "\n".join([x for x in levels])
    
    def __str__(self):
        return self.str_impl(self.trie)
    
    def insert_impl(self, node: TrieNode, key: str, idx: int) -> None:
        if len(key) == idx:
            node.is_eow = True
            return
        child = node.children.get(key[idx], TrieNode())
        node.children[key[idx]] = child

        self.insert_impl(child, key, idx + 1)
    
    def search_impl(self, node: TrieNode, key: str, idx: int) -> bool:
        if node is None:
            return False
        if len(key) == idx:
            return node.is_eow
        
        if key[idx] == ".":
            for child in node.children.values():
                result = self.search_impl(child, key, idx+1)
                if result:
                    return True
            return False

        child = node.children.get(key[idx], None)
        return self.search_impl(child, key, idx+1)
    
    def insert(self, key: str) -> None:
        self.insert_impl(self.trie, key, 0)
    
    
    def search(self, key: str) -> bool:
        return self.search_impl(self.trie, key, 0)

class WordDictionary:

    def __init__(self):
        self.word_dict = Trie()
        self.lookup = {}

    def addWord(self, word: str) -> None:
        self.word_dict.insert(word)

    def search(self, word: str) -> bool:
        if word in self.lookup.keys() and self.lookup[word] == True:
            return True
        result = self.word_dict.search(word)
        self.lookup[word] = result
        return result


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
