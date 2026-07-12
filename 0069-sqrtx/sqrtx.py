class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        guess = x / 2

        while True:
            better_guess = 0.5 * (guess + x / guess)
            if abs(guess - better_guess) < 0.000001:
                return int(better_guess)
            guess = better_guess
