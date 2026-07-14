class TrieNode():
    def __init__(self):
        self.childs = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.childs:
                curr.childs[c] = TrieNode()
            curr = curr.childs[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(node, ptr):
            for i in range(ptr, len(word)):
                c = word[i]
                if c == ".":
                    for child in node.childs.values():
                        if dfs(child, i+1):
                            return True
                if c not in node.childs:
                    return False
                node = node.childs[c]
            return node.word
        return dfs(self.root, 0)            

