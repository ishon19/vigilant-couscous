# class Solution:
#     def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
#         if not edges:
#             count = 0
#             for value in values:
#                 if value % k == 0:
#                     count += 1
#             return count
            
#         graph = defaultdict(list)
#         for u,v in edges:
#             graph[u].append(v)
#             graph[v].append(u)
        

#         # def dfs(node, parent):
#         #     nonlocal res            
#         #     current_sum = values[node]

#         #     for neighbor in graph[node]:
#         #         if neighbor != parent:
#         #             current_sum = (current_sum + dfs(neighbor, node)) % k
            
#         #     if current_sum == 0:
#         #         res += 1
            
#         #     return current_sum
#         def dfs(u, parent):
#             dp_u = { values[u] % k: 0 }
            
#             for v in graph[u]:
#                 if v == parent: 
#                     continue
#                 dp_child = dfs(v, u)
                
#                 new_dp = {}
#                 for rem_u, cnt_u in dp_u.items():
#                     for rem_v, cnt_v in dp_child.items():
#                         total_rem = (rem_u + rem_v) % k
#                         total_cnt = cnt_u + cnt_v

#                         if total_rem == 0:
#                             total_cnt += 1
                        
#                         if total_rem not in new_dp:
#                             new_dp[total_rem] = total_cnt
#                         else:
#                             new_dp[total_rem] = max(new_dp[total_rem], total_cnt)
                
#                 dp_u = new_dp
            
#             return dp_u

        
#         res = 0
#         dfs(0, -1)
#         return res

class Solution:          
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Create adjacency list representation of the tree
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # This will store our answer
        components = 0
        
        def dfs(node: int, parent: int) -> int:
            nonlocal components
            
            # Start with current node's value
            subtree_sum = values[node]
            
            # Visit all children (neighbors except parent)
            for neighbor in graph[node]:
                if neighbor != parent:
                    # Add the sum returned from child subtree
                    subtree_sum += dfs(neighbor, node)
            
            # If this subtree's sum is divisible by k, we can make it a component
            if subtree_sum % k == 0:
                components += 1
                # Return 0 as this subtree is now a separate component
                return 0
                
            # Otherwise, return the sum to be added to parent's sum
            return subtree_sum
        
        # Start DFS from node 0 (could start from any node)
        dfs(0, -1)
        return components