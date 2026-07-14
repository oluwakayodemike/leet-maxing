class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        
        if b == 0:
            return 0 

        while b != 0:
            rem = a % b
            a, b = b, rem
        
        return a