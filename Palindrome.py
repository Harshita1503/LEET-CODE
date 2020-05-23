class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        if x < 0:
            return False

        reverse = 0

        while x > 0:
            reverse = (10*reverse) + x % 10
            x //= 10

        return reverse == original
