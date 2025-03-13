from typing import List, Tuple, Optional

class MazeSolver:
    """
    A class to solve mazes by finding the shortest path from entrance to exit.
    
    The maze is represented as a 2D grid where:
    - 0 represents a walkable path
    - 1 represents a wall
    - 'S' represents the start point
    - 'E' represents the exit point
    """
    
    @staticmethod
    def find_shortest_path(maze: List[List[str]]) -> Optional[List[Tuple[int, int]]]:
        """
        Find the shortest path through the maze using Breadth-First Search.
        
        Args:
            maze (List[List[str]]): 2D grid representing the maze
        
        Returns:
            Optional[List[Tuple[int, int]]]: List of coordinates representing the shortest path,
            or None if no path exists
        
        Raises:
            ValueError: If maze is empty or invalid
        """
        # Validate input
        if not maze or not maze[0]:
            raise ValueError("Maze cannot be empty")
        
        # Find start and end positions
        start = None
        end = None
        rows, cols = len(maze), len(maze[0])
        
        for r in range(rows):
            for c in range(cols):
                if maze[r][c] == 'S':
                    start = (r, c)
                elif maze[r][c] == 'E':
                    end = (r, c)
        
        # Validate start and end exist
        if start is None or end is None:
            raise ValueError("Maze must have a start 'S' and an exit 'E'")
        
        # Possible movement directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # Queue for BFS
        queue = [(start, [start])]
        
        # Track visited cells to prevent revisiting
        visited = set([start])
        
        while queue:
            (current_r, current_c), path = queue.pop(0)
            
            # Check if reached exit
            if (current_r, current_c) == end:
                return path
            
            # Try all possible moves
            for dr, dc in directions:
                next_r, next_c = current_r + dr, current_c + dc
                
                # Check if move is valid
                if (0 <= next_r < rows and 
                    0 <= next_c < cols and 
                    maze[next_r][next_c] != '1' and 
                    (next_r, next_c) not in visited):
                    
                    # Additional check to prevent getting stuck
                    neighbors_count = sum(
                        1 for ndr, ndc in directions 
                        if (0 <= next_r + ndr < rows and 
                            0 <= next_c + ndc < cols and 
                            maze[next_r + ndr][next_c + ndc] != '1')
                    )
                    
                    if neighbors_count > 0:  # Ensure at least one valid adjacent cell
                        queue.append(((next_r, next_c), path + [(next_r, next_c)]))
                        visited.add((next_r, next_c))
        
        # No path found
        return None