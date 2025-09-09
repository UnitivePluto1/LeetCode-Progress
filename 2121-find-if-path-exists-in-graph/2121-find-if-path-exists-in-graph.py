class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, vis):
            if node == destination:
                return True
            vis.add(node)
            for i in graph[node]:
                if i not in vis:
                    if dfs(i,vis):
                        return True
            return False
        
        vis = set()
        return dfs(source, vis)
