class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = {i:0 for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        taken = 0

        while q:
            current = q.popleft()

            taken += 1

            for next_course in graph[current]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    q.append(next_course)
        
        return taken == numCourses
