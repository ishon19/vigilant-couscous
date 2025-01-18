class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # perform bfs to find the min moves
        moves = 0
        dirs = [[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]

        def _swap(state, i, j):
            state_list = list(state)
            state_list[i], state_list[j] = state_list[j], state_list[i]
            return "".join(state_list)
        
        target_state = "123450"
        start_state = "".join(str(val) for row in board for val in row)
        visited = set()
        queue = deque([start_state])

        while queue:
            for _ in range(len(queue)):
                current_state = queue.popleft()

                if current_state == target_state:
                    return moves
                
                zero_pos = current_state.index("0")
                for new_pos in dirs[zero_pos]:
                    next_state = _swap(current_state, zero_pos, new_pos)

                    if next_state in visited:
                        continue
                    
                    visited.add(next_state)
                    queue.append(next_state)
            moves += 1
        
        return -1