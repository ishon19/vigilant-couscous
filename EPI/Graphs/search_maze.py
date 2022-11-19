import collections
from typing import List

white, black = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze: List[List[int]], s: Coordinate, e: Coordinate):
    # dfs for path search
    def helper(cur):
        # check if cur in within the maze and is a white pixel
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x]) and maze[cur.x][cur.y] == white):
            return False

        path.append(cur)
        maze[cur.x][cur.y] = black
        if cur == e:
            return True

        if(any(map(helper, map(Coordinate, cur.x-1, cur.x+1, cur.x, cur.x), (cur.y, cur.y, cur.y-1, cur.y+1)))):
            return True
        
        # remove entry as can not find path
        del path[-1]
        return False

    path: List[Coordinate] = []
    helper(s)
    return path
