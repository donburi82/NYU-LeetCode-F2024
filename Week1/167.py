# 167. Two Sum II - Input Array Is Sorted
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers)-1
    while r>l:
        add = numbers[l]+numbers[r]
        if add==target:
            break
        elif add<target:
            l += 1
        elif add>target:
            r -= 1
    return [l+1, r+1] # 1-indexed