class Solution:
    def isPalindrome(self, x: int) -> bool:
        forward_list = list(str(x))
        backward_list = list(reversed(str(x)))

        if forward_list == backward_list:
            return True
        else:
            return False