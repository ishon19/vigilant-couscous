'''
You are given a binary tree as a sequence of parent-child pairs. 
For example, the tree represented by the node pairs below:
(A,B) (A,C) (B,G) (C,H) (E,F) (B,D) (C,E)
Below is the recursive definition for the S-expression of a tree:
S-exp(node) = ( node->val 
(S-exp(node->first_child))(S-exp(node->second_child))), if node != NULL
                         = "", node == NULL 
   where, first_child->val < second_child->val (lexicographically smaller)
This tree can be represented in a S-expression in multiple ways. 
The lexicographically smallest way of expressing this is as follows:
(A(B(D)(G))(C(E(F))(H)))
We need to translate the node-pair representation into an S-expression 
(lexicographically smallest one), and report any errors that do not conform to the definition of a binary tree.
The list of errors with their codes is as follows:
Error Code          Type of error
E1                 More than 2 children
E2                 Duplicate Edges
E3                 Cycle present
E4                 Multiple roots
E5                 Any other error
'''

# testing the branch changes


def checkError(inputStr):
    if not inputStr or inputStr.strip() != inputStr or '\n' in inputStr or '\t' in inputStr:
        return 'E5'

    inputStrSplit = inputStr.split(' ')
    print(inputStrSplit[0][1])
    inputStrList = [(i.split(',')[0][1], i.split(',')[1][0])
                    for i in inputStrSplit]
    print('inputList', inputStrList)

    # Duplicate edges
    temp = list(filter(lambda x: x[0] == x[1], inputStrList))
    print('temp - duplicate edges', temp)
    if len(temp):
        return 'E2'

    #  more than 2 children
    # temp = sorted(inputStrList, key=lambda)
    print('temp - more than 2 children', temp)


if __name__ == '__main__':
    # roots = '(A,B) (A,C) (A,G) (C,H) (E,F) (B,D) (C,E)'
    roots = input()
    print(checkError(roots))
