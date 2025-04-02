class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        itemset = {}
        i=0
        while (i+10) <= len(s):
            st = s[i:i+10] 
            if st in itemset:
                itemset[st] += 1
                if itemset[st]==2:
                    ans.append(st)
            else:
                itemset[st] = 1
            i+=1
        return ans