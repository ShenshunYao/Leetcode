#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -nums[idx] if nums[idx] > 0 else nums[idx]
        
        for i in range(0, len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
                
        return res
# @lc code=end

