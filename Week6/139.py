# 139. Word Break
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c)-ord('a')
            if cur.children[idx] is None:
                new_node = TrieNode()
                cur.children[idx] = new_node
            
            cur = cur.children[idx]

        cur.isEnd = True

    def getRoot(self) -> TrieNode:
        return self.root

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            if not dp[i]:
                continue
            
            node = trie.getRoot()
            for j in range(i, n):
                idx = ord(s[j])-ord('a')
                if node.children[idx] is None:
                    break
                
                node = node.children[idx]
                if node.isEnd:
                    dp[j+1] = True
        
        return dp[n]