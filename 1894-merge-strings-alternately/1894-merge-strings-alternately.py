class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans=''
        i=0
        if len(word1)>len(word2):
            i=len(word1)
        else:
            i=len(word2)
        for j in range(0,i):
            if j<len(word1):
                ans+=word1[j]
            if j<len(word2):
                ans+=word2[j]
        return ans
