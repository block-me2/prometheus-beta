import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Implement the Hungarian algorithm for solving the assignment problem.
    
    The algorithm finds the optimal assignment that minimizes the total cost.
    
    Args:
        cost_matrix (list or numpy.ndarray): A 2D matrix of assignment costs 
                                             where each element represents 
                                             the cost of assigning a worker 
                                             to a job.
    
    Returns:
        tuple: A tuple containing:
            - Optimal total cost (float)
            - List of assignments [(worker_index, job_index), ...]
    
    Raises:
        ValueError: If the input is not a valid 2D matrix
    """
    # Convert input to numpy array for consistent processing
    if not isinstance(cost_matrix, (list, np.ndarray)):
        raise ValueError("Input must be a 2D list or numpy array")
    
    cost_matrix = np.array(cost_matrix, dtype=float)
    orig_matrix = cost_matrix.copy()
    
    # Validate matrix dimensions
    if cost_matrix.ndim != 2:
        raise ValueError("Input must be a 2D matrix")
    
    # If not square matrix, pad with zeros
    rows, cols = cost_matrix.shape
    is_square = rows == cols
    
    if not is_square:
        # Pad the matrix to make it square
        max_dim = max(rows, cols)
        padded_matrix = np.zeros((max_dim, max_dim))
        padded_matrix[:rows, :cols] = cost_matrix
        cost_matrix = padded_matrix
        rows = cols = max_dim
    
    # Step 1: Subtract row minimums
    for i in range(rows):
        row_min = np.min(cost_matrix[i, :])
        cost_matrix[i, :] -= row_min
    
    # Step 2: Subtract column minimums
    for j in range(cols):
        col_min = np.min(cost_matrix[:, j])
        cost_matrix[:, j] -= col_min
    
    # Step 4: Create optimal assignment
    def find_assignment(matrix):
        assignment = []
        assigned_rows = set()
        assigned_cols = set()
        
        for i in range(rows):
            zero_cols = np.where(matrix[i, :] == 0)[0]
            for col in zero_cols:
                if col not in assigned_cols and i not in assigned_rows:
                    assignment.append((i, col))
                    assigned_rows.add(i)
                    assigned_cols.add(col)
        
        return assignment
    
    # Find the assignment
    assignments = find_assignment(cost_matrix)
    
    # Calculate total cost (using original matrix)
    total_cost = sum(orig_matrix[worker, job] for worker, job in assignments)
    
    # If not originally a square matrix, filter out padded assignments
    if not is_square:
        assignments = [(w, j) for w, j in assignments if w < rows and j < cols]
    
    return total_cost, assignments

def solve_assignment_problem(cost_matrix):
    """
    Wrapper function to solve the assignment problem.
    
    Args:
        cost_matrix (list or numpy.ndarray): Cost matrix for assignments
    
    Returns:
        tuple: Total optimal cost and list of assignments
    """
    return hungarian_algorithm(cost_matrix)