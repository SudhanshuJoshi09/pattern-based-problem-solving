class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def dfs(graph, start, path):
            if start == len(graph) - 1:
                res.append(path + [start])
            
            for curr in graph[start]:
                dfs(graph, curr, path + [start])
        
        dfs(graph, 0, [])
        return res
