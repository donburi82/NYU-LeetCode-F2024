# 238. Product of Array Except Self
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1 for _ in range(n)]

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(n-1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
    
    return result