class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1

        if s[:1] == '-':
            sign = -1
            s = s[1:]
        elif s[:1] == '+':
            sign = 1
            s = s[1:]

        result = 0
        for char in s:
            if char.isdigit():
                result = (result * 10) + int(char)
            else:
                break

        result = result * sign

        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        
        if result < MIN_INT:
            return MIN_INT
        elif result > MAX_INT:
            return MAX_INT
        else:
            return result