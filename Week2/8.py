# 8. String to Integer (atoi)
def myAtoi(self, s: str) -> int:
    # 1. Whitespace
    s = s.strip()
    if not s:
        return 0

    # 2. Signedness
    sign = 1
    i = 0
    if s[0]=="-":
        sign = -1
        i += 1
    elif s[0]=="+":
        i += 1

    # 3. Conversion
    while i<len(s) and s[i]=="0":
        i += 1
    if i==len(s) or not s[i].isnumeric():
        return 0
    
    start = i
    while i<len(s) and s[i].isnumeric():
        i += 1
    
    # 4. Rounding
    num = sign*int(s[start:i])
    if num<-2**31:
        return -2**31
    elif num>2**31-1:
        return 2**31-1
    else:
        return num