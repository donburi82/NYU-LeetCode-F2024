# 438. Find All Anagrams in a String
def findAnagrams(self, s: str, p: str) -> List[int]:
    size = len(p)
    target = ''.join(sorted(p))
    res = []
    for i in range(len(s)-size+1):
        cur = ''.join(sorted(s[i:i+size]))
        if cur==target:
            res.append(i)

    return res

def findAnagrams(self, s: str, p: str) -> List[int]:
    size = len(p)
    res = []

    targetFreq = {}
    for c in p:
        if c not in targetFreq:
            targetFreq[c] = 0
        targetFreq[c] += 1

    curFreq = {}
    for c in s[0:size]:
        if c not in curFreq:
            curFreq[c] = 0
        curFreq[c] += 1

    if curFreq==targetFreq:
        res.append(0)

    for i in range(size, len(s)):
        curFreq[s[i]] = curFreq.get(s[i], 0)+1

        curFreq[s[i-size]] -= 1
        if curFreq[s[i-size]]==0:
            del curFreq[s[i-size]]

        if curFreq==targetFreq:
            res.append(i-size+1)

    return res

def findAnagrams(self, s: str, p: str) -> List[int]:
    size = len(p)
    res = []

    targetFreq = [0]*26
    for c in p:
        targetFreq[ord(c)-ord('a')] += 1
    
    curFreq = [0]*26
    for c in s[0:size]:
        curFreq[ord(c)-ord('a')] += 1

    if curFreq==targetFreq:
        res.append(0)
    
    for i in range(size, len(s)):
        curFreq[ord(s[i])-ord('a')] += 1
        curFreq[ord(s[i-size])-ord('a')] -= 1

        if curFreq==targetFreq:
            res.append(i-size+1)

    return res