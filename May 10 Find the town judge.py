'''In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
'''
 
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        n=1
        count=0
        a=[0]*N
        for i in range (0,N):
            a[i]=n
            n=n+1
        for i in range (0,len(trust)):
            t=trust[i][0]
            a[t-1]=-1
        for i in range (0,len(a)):
            if(a[i]!=-1):
                val=a[i]
                count=count+1
        if(count!=1):
            return -1
        else:
            count=0
            for i in range (0,len(trust)):
                if(trust[i][1]==val):
                    count=count+1
            if(count==N-1):
                return val
            else:
                return -1
