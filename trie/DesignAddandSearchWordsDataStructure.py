class WordNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary(object):

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = WordNode()
            cur = cur.children[ch]
        cur.end = True

        
        

    def search(self, word):
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.end
        
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad"))
print(obj.search("bad"))
print(obj.search(".ad") )
print(obj.search("b.."))

# word = ""
# obj.addWord(word)
# param_2 = obj.search(word)