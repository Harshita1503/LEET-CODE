'''Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k==len(num):
            return '0'
        digit=len(num)-k
        output=[]
        output.append(num[0])
        for i in num[1:]:
            while output and int(i)<int(output[-1]) and k>0:
                output.pop()
                k-=1
            output.append(i)
        
        return str(int(''.join(output)[0:digit]))
        
