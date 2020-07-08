#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
from typing import List


# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i, j, ans = 0, 0, len(nums) + 1
        sums = []

        for num in nums:
            if not sums:
                sums.append(num)
            else:
                sums.append(sums[-1] + num)

        while i < len(nums) and j < len(nums):
            if sums[j] - sums[i] + nums[i] < s:
                j += 1
            else:
                if j + 1 - i < ans:
                    ans = j + 1 - i
                i += 1
        if ans != len(nums) + 1:
            return ans
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
# @lc code=end
