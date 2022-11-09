# inputString = '(A,B) (A,C) (B,G) (C,H) (E,F) (B,D) (C,E)'
# inputString = '(A,B) (A,C) (A,D)' #E1
# inputString = '(A,B) (A,B)' #E2
# inputString = '(A,B) (B,C) (A,C)' #E5
# inputString = '(A,B) (C,D)'  #E4
inputString = '(A,B) (B,C) (C,A)' #E3

inputString = inputString.split(' ')
pairs = []
parentMap = {}
childMap = {}


# def printPreorder(root):
#     if root:
#         # First print the data of node
#         print('(')
#         print(root.val),
#         # Then recur on left child
#         print('(')
#         printPreorder(root.left)
#         # Finally recur on right child
#         print('(')
#         printPreorder(root.right)
#     else:
#         print(')')


def findError(inputStringList):
    for string in inputStringList:
        pair = [string[1], string[3]]

        # E1
        parent = pair[0]
        child = pair[1]
        if parent in parentMap:
            if len(parentMap[parent]) >= 2:
                return 'More than 2 Children, E1'
            parentMap[parent].append(child)
        else:
            parentMap[parent] = [child]

        # E2
        if pair in pairs:
            return 'Duplicate, E2'
        pairs.append(pair)

        # E3
        if child in parentMap and parent in childMap and childMap[parent] in parentMap[child]:
            return 'Cycle Present, E3'

        # E5
        if child in childMap:
            if childMap[child] != parent:
                return 'Multiple Parent, E4'
        else:
            childMap[child] = parent

    for k, v in childMap.items():
        if k in parentMap:
            return inputString

    return 'Multiple roots, E5'


print(findError(inputString))
