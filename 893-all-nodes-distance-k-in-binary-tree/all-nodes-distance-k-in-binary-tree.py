# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # # make the tree bidirectional
        # def addParent(node, parent):
        #     if node:
        #         node.parent = parent
        #         addParent(node.left, node)
        #         addParent(node.right, node)
        
        # # create the refs
        # addParent(root, None)

        # res = []
        # seen = set()

        # def dfs(node, dist):
        #     if node:
        #         if node in seen:
        #             return
        #         seen.add(node)

        #         if dist == 0:
        #             res.append(node.val)
        #             return
        #         dfs(node.parent, dist - 1)
        #         dfs(node.left, dist - 1)
        #         dfs(node.right, dist - 1)
        
        # dfs(target,  k)
        # return res

        # approach 2
        graph = collections.defaultdict(list)

        def build_graph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left: build_graph(cur.left, cur)
            if cur.right: build_graph(cur.right, cur)
        
        build_graph(root, None)

        res = []
        seen = set([target.val])

        def dfs(cur, distance):
            if distance == k:
                res.append(cur)
                return
            for neighbor in graph[cur]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor, distance + 1)
        dfs(target.val, 0)

        return res 
                  
                    
