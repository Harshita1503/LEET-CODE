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
        dic={}
        for i in trust:
            if i[0] in dic:
                dic[i[0]].append(i[1])
            else:
                dic[i[0]]=[i[1]]
        missing=0
        for i in range(1,N+1):
            if(missing>1):
                break
			#because there has to be only one judge in the town, 
		    #so more than one missing key means there's no judge, so just break from loop
            if(i not in dic):
                missing+=1
                ans=i
        if(missing!=1):
            return -1
		#to verify that the missing key is the judge
        if(missing==1):
            for i in range(1,N+1):
                if(i==ans):
                    continue
                if(ans not in dic[i]):
                    return -1
            return ans
  
