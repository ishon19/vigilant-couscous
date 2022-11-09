# three types of moves allowed:
# 1. move from location (x,y) to (x+y,y)
# 2. move from location (x,y) to (x,y+x)
# 3. for some constant c, move from location (x,y) to (x+c,y+c)
# if the sum of coordinates is perfect square, then the path is not valid

def canReach(c, x1,y1,x2,y2):
    def isPerfectSquare(n):
        return int(n**0.5)**2 == n
    
    if x1 == x2 and y1 == y2:
        return True
    
    def helper(x,y):
        print(x,y)
        if x == x2 and y == y2:
            return True
        if isPerfectSquare(x+y):    
            print('perf')        
            return False
        if x<0 or y<0 or x>x2 or y>y2:            
            return False                
        return helper(x+y,y) or helper(x,x+y) or helper(x+c,y+c)

    return 'Yes' if helper(x1,y1) else 'No'
        

if __name__ == '__main__':    
    print(canReach(3, 0, 0, 6, 6))