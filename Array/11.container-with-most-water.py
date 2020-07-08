#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # first (left) pointer
        p1 = 0  
        # second (right) pointer
        p2 = len(height) - 1  
        max_area = 0
        while p1 != p2:
            if height[p1] > height[p2]:
                # height of smaller edge multiplies on length
                area = height[p2] * (p2 - p1)  
                # changing smaller edge
                p2 -= 1  
            else:
                area = height[p1] * (p2 - p1)
                p1 += 1
            if area > max_area: 
                # increasing max area if possible
                max_area = area  
        return max_area
        
# @lc code=end

