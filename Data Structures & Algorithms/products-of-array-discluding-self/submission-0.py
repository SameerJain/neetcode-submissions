#from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # get list of prefixes
        # get list of suffixes
        # multiply them into a new array and return it
        n = len(nums)
        result =  [1 for _ in range(n)]
        prefixes = [1 for _ in range(n)]
        suffixes = [1 for _ in range(n)]

        for i in range(1,n):
            prefixes[i] *= nums[i-1] * prefixes[i-1]
        for i in range(n-2,-1,-1):
            suffixes[i] *= nums[i+1] * suffixes[i+1]
        for i in range(n):
            result[i] *= suffixes[i] * prefixes[i]
        return result