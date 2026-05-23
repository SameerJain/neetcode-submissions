class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = float('-inf')
        for i in range(0,len(heights)):
            for j in range(1,len(heights)):
                result = max(result,min(heights[i],heights[j]) *(j-i))
        return result