class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkDuplicates(arr):
            newArr = []
            for i in range(len(arr)):
                if arr[i] != ".":
                    newArr.append(arr[i])
                    
            # print('[checkDuplicates]', newArr)
            return len(set(newArr)) == len(newArr) if newArr else True
        
        def checkRowOrCol(arr):
            return checkDuplicates(arr)
        
        def checkBlock(arr):
            hashmap = defaultdict(list)    
            # print('block', arr)
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    if arr[i][j] != "." and arr[i][j] not in hashmap:
                        hashmap[arr[i][j]] = [arr[i][j]]
                    elif arr[i][j] !="." and arr[i][j] in hashmap:
                        hashmap[arr[i][j]].append(arr[i][j])            
            vals = [len(hashmap[key]) == 1 for key in hashmap]
            # print('vals', vals)
            return all(vals) if vals else True
        
        final = []
        
        # row checks
        rowChecks = []
        for i in range(len(board)):
            rowChecks.append(checkRowOrCol(board[i]))
        final.append(all(rowChecks))
        
        # col checks
        colChecks = []
        cols = [[row[i] for row in board] for i in range(len(board))]
        for j in range(len(board[0])):
            colChecks.append(checkRowOrCol(cols[j]))
        final.append(all(colChecks))
        
        # block checks
        blockChecks = []
        for i in range(0,len(board),3):
            for j in range(0,len(board[0]),3):
                blockChecks.append(checkBlock([row[i:i+3] for row in board[j:j+3]]))
        final.append(all(blockChecks))
        
        # print(rowChecks)
        # print(colChecks)
        # print(blockChecks)
        # print(final)
        
        return all(final)