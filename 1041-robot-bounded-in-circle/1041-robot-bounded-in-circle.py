class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        initial = (0,0,'N')
        dirMap = {'N':['W','E'], 'W':['S','N'], 'S':['E','W'],'E':['N','S']}
        pos = initial
        
        def nextPosition(instruction):
            nonlocal pos 
            if instruction == 'G':
                if pos[2] == 'N':
                    pos = (pos[0], pos[1]+1, pos[2])
                elif pos[2] == 'S':
                    pos = (pos[0], pos[1]-1, pos[2])
                elif pos[2] == 'W':
                    pos = (pos[0]-1,  pos[1], pos[2])
                else:
                    pos = (pos[0]+1, pos[1], pos[2])
            elif instruction == 'L':
                    pos = (pos[0], pos[1], dirMap[pos[2]][0])
            elif instruction == 'R':                
                    pos = (pos[0], pos[1], dirMap[pos[2]][1])
        
        for i in range(4):
            for instruction in instructions:
                nextPosition(instruction)
            if pos == initial:
                break
            # print('position after cycle', pos)        
            
        return pos == initial