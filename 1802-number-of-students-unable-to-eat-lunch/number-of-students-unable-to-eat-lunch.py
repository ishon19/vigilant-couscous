class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = deque(students)  # Queue of students
        sandwiches_stack = deque(sandwiches)  # Stack of sandwiches
        
        while sandwiches_stack:
            # If the student at the front of the queue wants the sandwich on top of the stack
            if students_queue[0] == sandwiches_stack[0]:
                students_queue.popleft()  # Student leaves the queue
                sandwiches_stack.popleft()  # Sandwich is removed from the stack
            else:
                # If we've gone through the entire queue without finding a match,
                # it means no further matches are possible
                if students_queue.count(students_queue[0]) == len(students_queue):
                    break
                
                students_queue.rotate(-1)  # Move the front student to the end of the queue
        
        return len(students_queue)