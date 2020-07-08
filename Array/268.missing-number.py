#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort() 
        n = len(nums)
        # edge case
        if nums[-1] != n: return n
        elif nums[0] != 0: return 0
        # check the missing value on (0,n)
        for i in range(1, len(nums)):
            res = nums[i-1] + 1
            if nums[i] != res:
                return res
# @lc code=end

