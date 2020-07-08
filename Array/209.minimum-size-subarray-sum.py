#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i, j, res = 0, 0, len(nums) + 1
        sums = []

        for num in nums:
            if not sums: sums.append(num)
            else: sums.append(sums[-1] + num)

        while i < len(nums) and j < len(nums):
            if sums[j] - sums[i] + nums[i] < s: j += 1
            else:
                if j + 1 - i < res: 
                    res = j + 1 - i
                i += 1
        if res != len(nums) + 1:
            return res
        else: return 0
# @lc code=end

