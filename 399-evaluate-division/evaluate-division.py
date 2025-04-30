class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (x, y), value in zip(equations, values):
            graph[x][y] = value
            graph[y][x] = 1 / value

        
        def find_path(start, end, visited=None):
            if visited is None:
                visited = set()
            
            if start not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            visited.add(start)

            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    result = find_path(neighbor, end, visited)
                    if result != -1.0:
                        return weight * result
            
            return -1.0
        
        return [find_path(x,y) if x in graph and y in graph else -1.0 for x, y in queries]

