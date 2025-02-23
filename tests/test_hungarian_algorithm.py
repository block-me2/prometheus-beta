import pytest
import numpy as np
from src.hungarian_algorithm import solve_assignment_problem, hungarian_algorithm

def test_basic_square_matrix():
    """Test a basic square cost matrix."""
    cost_matrix = [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
    ]
    total_cost, assignments = solve_assignment_problem(cost_matrix)
    
    # Verify total cost and assignments
    assert total_cost == 6  # Minimum possible cost
    assert len(assignments) == 3
    assert set(assignments) == {(0, 0), (1, 1), (2, 2)}

def test_rectangular_matrix():
    """Test a rectangular cost matrix."""
    cost_matrix = [
        [1, 2, 3],
        [2, 4, 6]
    ]
    total_cost, assignments = solve_assignment_problem(cost_matrix)
    
    # Verify assignments and length
    assert len(assignments) == 2
    assert total_cost is not None

def test_single_element_matrix():
    """Test a single element matrix."""
    cost_matrix = [[5]]
    total_cost, assignments = solve_assignment_problem(cost_matrix)
    
    assert total_cost == 5
    assert assignments == [(0, 0)]

def test_zero_cost_matrix():
    """Test a matrix with all zero costs."""
    cost_matrix = [
        [0, 0],
        [0, 0]
    ]
    total_cost, assignments = solve_assignment_problem(cost_matrix)
    
    assert total_cost == 0
    assert len(assignments) == 2

def test_invalid_input_types():
    """Test invalid input types raise ValueError."""
    with pytest.raises(ValueError):
        solve_assignment_problem("not a matrix")
    
    with pytest.raises(ValueError):
        solve_assignment_problem([1, 2, 3])  # 1D list

def test_large_matrix():
    """Test a larger matrix to ensure scalability."""
    cost_matrix = np.random.randint(1, 100, size=(5, 5))
    total_cost, assignments = solve_assignment_problem(cost_matrix)
    
    assert len(assignments) == 5
    assert total_cost is not None