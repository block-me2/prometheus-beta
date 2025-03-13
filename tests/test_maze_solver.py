import pytest
from src.maze_solver import MazeSolver

def test_simple_maze_path():
    """Test a simple maze with a direct path"""
    maze = [
        ['S', '0', '0', '0'],
        ['1', '1', '0', '1'],
        ['0', '0', '0', 'E']
    ]
    path = MazeSolver.find_shortest_path(maze)
    assert path is not None
    assert path[0] == (0, 0)  # Start point
    assert path[-1] == (2, 3)  # End point
    assert len(path) == 6  # Correct path length

def test_maze_with_obstacles():
    """Test a maze with multiple obstacles and one valid path"""
    maze = [
        ['S', '0', '1', '0'],
        ['1', '0', '1', '0'],
        ['0', '0', '1', 'E']
    ]
    path = MazeSolver.find_shortest_path(maze)
    assert path is not None
    assert path[0] == (0, 0)  # Start point
    assert path[-1] == (2, 3)  # End point

def test_no_path_exists():
    """Test a maze where no path exists"""
    maze = [
        ['S', '1', '1', '1'],
        ['1', '1', '1', '1'],
        ['1', '1', '1', 'E']
    ]
    path = MazeSolver.find_shortest_path(maze)
    assert path is None

def test_start_and_end_adjacent():
    """Test a maze where start and end are adjacent"""
    maze = [
        ['S', 'E', '0'],
        ['0', '0', '0']
    ]
    path = MazeSolver.find_shortest_path(maze)
    assert path is not None
    assert len(path) == 2

def test_empty_maze_raises_error():
    """Test that an empty maze raises a ValueError"""
    with pytest.raises(ValueError):
        MazeSolver.find_shortest_path([])

def test_maze_without_start_or_end():
    """Test that a maze without start or end point raises a ValueError"""
    maze = [
        ['0', '0', '0'],
        ['0', '0', '0']
    ]
    with pytest.raises(ValueError):
        MazeSolver.find_shortest_path(maze)

def test_single_cell_maze():
    """Test a single-cell maze with start and end"""
    maze = [['S']]
    with pytest.raises(ValueError):
        MazeSolver.find_shortest_path(maze)