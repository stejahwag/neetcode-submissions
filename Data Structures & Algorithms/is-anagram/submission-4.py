class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # My solution

        # if sorted(s)==sorted(t):
        #     return True
        # else:
        #     return False
        
        # if len(s)!= len(t):
        #     return False

        ###################
        # ideal solution 1

        countS, countT = {}, {}

        if len(s) != len(t):
            return False

        else:
            for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i],0)
                countT[t[i]] = 1 + countT.get(t[i],0)

        # for c in countS:
        #     if countS[c] != countT.get(c,0):
        #         return False
        # return True

            return countS == countT



        ###################
        # ideal solution 2