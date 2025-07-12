class Solution:
    def isValid(self, s: str) -> bool:
        
        val = []
        bmap = {')' : '(',']' : '[','}' : '{'}
        for _ in s:
            if _ in bmap:
                if not val or val[-1] != bmap[_]:
                    return False
                val.pop()
            else:
                val.append(_)
        
        return len(val) == 0
