class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = collections.defaultdict(list)

        for a, b, t in meetings:
            graph[a].append((t, b))
            graph[b].append((t, a))
        
        secret_disclosure = [float("inf")] * n

        # person 0 and firstPerson know the secret the earliest
        secret_disclosure[0] = 0
        secret_disclosure[firstPerson] = 0

        q = collections.deque([(0, 0), (firstPerson, 0)])

        while q:
            person, time = q.popleft()
            for t, next_person in graph[person]:
                if t >= time and secret_disclosure[next_person] > t:
                    secret_disclosure[next_person] = t
                    q.append((next_person, t))
        
        return [i for i in range(n) if secret_disclosure[i] != float("inf")]

        


        # sort by the meeting times
        # meetings.sort(key=lambda x: (x[2], x[0]))

        # res = set([0])
        # res.add(firstPerson)

        # dep = collections.defaultdict(list)

        # for i, (a, b, t) in enumerate(meetings):
        #     if i - 1 >= 0 and meetings[i-1][2] == t:
        #         c, d = meetings[i-1][0], meetings[i-1][1]
        #         if c in res or d in res and a in res or b in res:
        #             res.add(a)
        #             res.add(b)                    

        #     if a == firstPerson or b == firstPerson:
        #         dep[a].append(b)
        #         dep[b].append(a)  
        #         res.add(a)
        #         res.add(b)
        #     elif firstPerson in dep[a] or firstPerson in dep[b] or a in res or b in res:
        #         dep[a].append(b)
        #         dep[b].append(a)
        #         res.add(a)
        #         res.add(b)
            
        # # print(dep)

        # return list(res)

