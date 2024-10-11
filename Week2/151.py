# 151. Reverse Words in a String
def reverseWords(self, s: str) -> str:
    res = []
    for word in s.strip().split(" ")[::-1]:
        if word:
            res.append(word)

    return " ".join(res)

def reverseWords(self, s: str) -> str:
    return " ".join(s.split()[::-1])