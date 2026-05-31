from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Step 1: Initialize the graph and indegree array
        adj_list = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        
        # Step 2: Build the graph
        # [a, b] means b -> a (To take 'a', you must first take 'b')
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] += 1
            
        # Step 3: Add all courses with 0 prerequisites to the queue
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        completed_courses = 0
        
        # Step 4: Process the queue
        while queue:
            current = queue.popleft()
            completed_courses += 1
            
            # Reduce the indegree for all neighboring courses
            for next_course in adj_list[current]:
                indegree[next_course] -= 1
                # If all prerequisites are cleared, add it to the queue
                if indegree[next_course] == 0:
                    queue.append(next_course)
                    
        # Step 5: If we processed all courses, no cycle exists
        return completed_courses == numCourses