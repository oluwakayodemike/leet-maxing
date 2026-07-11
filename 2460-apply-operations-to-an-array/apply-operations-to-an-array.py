class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        writer = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[writer] = nums[i]
                writer += 1

        while writer < len(nums):
            nums[writer] = 0
            writer += 1
        
        return nums
