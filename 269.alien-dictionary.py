#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#

# @lc code=start
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        in_degree = defaultdict(int)

        for word in words:
            for c in word:
                in_degree[c] = 0
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break
        
        res = []
        q = deque([c for c in in_degree if in_degree[c] == 0])

        while q:
            c = q.popleft()
            res.append(c)

            for next_char in adj[c]:
                in_degree[next_char] -= 1
                if in_degree[next_char] == 0:
                    q.append(next_char)
        
        if len(res) != len(in_degree):
            return ""
        
        return "".join(res)

# @lc code=end

