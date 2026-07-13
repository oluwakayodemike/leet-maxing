class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        master = "123456789"
        result = []

        for length in range(2, 10):
            for i in range(10 - length):
                num = int(master[i: i + length])

                if low <= num <= high:
                    result.append(num)

        return result