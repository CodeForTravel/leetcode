# class TrieNode:
#     def __init__(self):
#         # self.children = [None] * 26
#         # with dictionary 
#         self.children = {}
#         self.isEndOfWord = False

# class Trie(object):

#     def __init__(self):
#         self.root = TrieNode()
        

#     def insert(self, word):
#         cur = self.root
#         for ch in word:
#             if ch not in cur.children:
#                 cur.children[ch] = TrieNode()
#             cur = cur.children[ch]
#         cur.isEndOfWord = True
        

#     def search(self, word):
#         cur = self.root
#         for ch in word:
#             if not ch in cur.children:
#                 return False
#             cur = cur.children[ch]
#         return cur.isEndOfWord
        

#     def startsWith(self, prefix):
#         cur = self.root
#         for ch in prefix:
#             if not ch in cur.children:
#                 return False
#             cur = cur.children[ch]
#         return True


class TrieNode:
    def __init__(self):
        # with list
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word):
        cur = self.root
        for ch in word:
            i = ord(ch) - ord('a')
            if cur.children[i] == None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.isEndOfWord = True
        

    def search(self, word):
        cur = self.root
        for ch in word:
            i = ord(ch) - ord('a')
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return cur.isEndOfWord
        

    def startsWith(self, prefix):
        cur = self.root
        for ch in prefix:
            i = ord(ch) - ord('a')
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return True
        


# Your Trie object will be instantiated and called as such:
word = "my word"
prefix = "my"
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
print(param_2)
param_3 = obj.startsWith(prefix)
print(param_3)
