#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(candidates, temp, remainder, index):
            if remainder == 0:
                res.append(temp[:])
                return
            
            if remainder < 0:
                return 
            
            for i in range(index, len(candidates)):
                temp.append(candidates[i])
                dfs(candidates, temp, remainder - candidates[i], i)
                temp.pop()
        
        dfs(candidates, [], target, 0)
        return res
# @lc code=end

