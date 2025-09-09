class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        pref_L = len(pref)

        for s in strs[1:]:
            while pref != s[0:pref_L]:
                pref_L -= 1
                if pref_L == 0:
                    return ""
                pref = pref[0:pref_L]

        return pref