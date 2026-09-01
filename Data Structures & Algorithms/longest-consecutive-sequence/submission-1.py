class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        print(nums)
        curr_count = 1
        max_count = 1
        for i in range(len(nums)- 1):
            next_num = nums[i+1]
            if nums[i] == next_num - 1:
                curr_count += 1
            elif nums[i] == next_num:
                continue
            else:
                max_count = max(max_count,curr_count)
                curr_count = 1 
        max_count = max(max_count, curr_count)
        return max_count