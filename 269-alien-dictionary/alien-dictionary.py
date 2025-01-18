class Solution:
    def findIndegree(self, graph):
        indegree = {node: 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        return indegree
    
    def topological(self, graph):
        seq = []
        pq = []

        # find and enqueue the nodes with 0 indegree
        indegrees = self.findIndegree(graph)
        for node, indegree in indegrees.items():
            if indegree == 0:
                heappush(pq, node)
        
        while pq:
            node = heappop(pq)
            seq.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    heappush(pq, neighbor)
        
        for indeg in indegrees.values():
            if indeg != 0:
                return None
        
        return seq

    def alienOrder(self, words: List[str]) -> str:
        graph = {c: set() for word in words for c in word}

        # construct the graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                # early termination
                return ""
            
            for j in range(minlen):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        
        s = self.topological(graph)
        if s is None:
            return ""
        
        return "".join(s)

