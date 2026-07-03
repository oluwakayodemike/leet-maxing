class Solution:
    def romanToInt(self, s: str) -> int:
        roman_sym = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0

        for i in range(len(s)):
            current_val = roman_sym[s[i]]

            if i + 1 < len(s) and current_val < roman_sym[s[i + 1]]:
                total -= current_val
            else:
                total += current_val

        return total
