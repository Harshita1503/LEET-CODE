'''Check whether a perfect square or not'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num + 1):
            sq = i * i
            if sq == num:
                print(f"{i} squared is exactly {num}")
                break
            if sq  > num:
                print(f"{num} is not a perfect square")
                break
