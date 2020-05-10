'''Check whether a perfect square or not'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a=num**(0.5)
        b=a*10
        c=b%10
        if(c==0):
            return True
        else:
            return False
