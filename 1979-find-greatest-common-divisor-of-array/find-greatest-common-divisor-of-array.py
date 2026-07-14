class Solution:
    def findGCD(self, nums: List[int]) -> int:
        import math

        l_num = max(nums)
        s_num = min(nums)
        
        gcd = math.gcd(s_num, l_num)

        return gcd
        
