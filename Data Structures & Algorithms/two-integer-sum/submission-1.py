class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenSet = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in seenSet:
                return[seenSet[compliment],i]
            seenSet[nums[i]] = i
            
        return []
# brute force solution
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[i] + nums[j] == target and i != j:
#                     return [i,j]
#         return []
        