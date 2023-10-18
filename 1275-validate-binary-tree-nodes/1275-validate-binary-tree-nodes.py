class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # the tree should satisfy the tree properties
        # 1. exactly one root
        # 2. children should not have multiple parents

        # check if root is repeated in unique children List
        # if not get the one which is not in children set
        children = set(leftChild) | set(rightChild)

        # finding the root
        root = -1
        for i in range(n):
            if i not in children:
                root = i
        
        if root == -1:
            return False
        
        # perform dfs to check the validity of the tree
        # start from the root
        seen = set([root])
        stack = [root]

        while stack:
            node = stack.pop()
            
            # check all the child nodes of the above node
            for child in [leftChild[node], rightChild[node]]:
                if child!=-1:
                    if child in seen:
                        return False
                    
                    stack.append(child)
                    seen.add(child)
        
        return len(seen) == n
