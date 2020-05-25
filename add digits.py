'''Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.'''
class Solution:
    def addDigits(self, num: int) -> int:
       
    
        a=str(num)
        s=0
        for i in a:
            s=s+int(i)
        if s>9:
            return self.addDigits(s)
        else:
            return s
            
