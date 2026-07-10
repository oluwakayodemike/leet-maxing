class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[writer] = nums[i]
                writer += 1

        return writer