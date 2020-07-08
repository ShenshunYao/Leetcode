#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity: O(n), traverse the list containing n elements once. 
        # Each look up in the dictionary costs O(1) time.
        # Space Complexity: The extra space required depends on the number of items stored in the dictionary, 
        # which stores at most n elements.
        dict = {}
        for i, n in enumerate(nums):
            if target - n not in dict:
                dict[n] = i
            else:
                return [dict[target - n], i]
# @lc code=end

