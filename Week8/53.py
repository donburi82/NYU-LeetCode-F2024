# 53. Maximum Subarray
def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [0]*n  # the maximum subarray that ends at index i
    largest = dp[0] = nums[0]
    
    for i in range(1, n):
        dp[i] = dp[i-1]+nums[i]
        if dp[i]<nums[i]:
            dp[i] = nums[i]
        if dp[i]>largest:
            largest = dp[i]

    return largest