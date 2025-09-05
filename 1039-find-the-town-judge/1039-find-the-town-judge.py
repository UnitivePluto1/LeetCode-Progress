class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outgoing= defaultdict(int)
        incoming = defaultdict(int)

        for u,v in trust:
            outgoing[u] += 1
            incoming[v] += 1

        for i in range(1, n+1):
            if outgoing[i] == 0 and incoming[i] == n-1:
                return i
        return -1
        