class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stoneCount = 0
        for j in J: 
            for s in S: 
                if(s == j):
                    stoneCount +=1
        return stoneCount