# 394. Decode String
def decodeString(self, s: str) -> str:
    stack = []
    for c in s:
        if c=="]":
            encoded = ""
            while stack and stack[-1]!="[":
                encoded = stack.pop()+encoded
            stack.pop()  # pop "["
            k, i = 0, 0
            while stack and stack[-1].isdigit():  # k [1, 300]
                k += int(stack.pop())*(10**i)
                i += 1
            stack.append(encoded*int(k))  # push back to stack
        else:
            stack.append(c)

    return "".join(stack)