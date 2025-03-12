import pytest
import sys
import math
from src.floyd_warshall import floyd_warshall

def test_basic_graph():
    """Test a basic graph with known shortest paths."""
    graph = [
        [0, 5, float('inf'), 10],
        [float('inf'), 0, 3, float('inf')],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]
    expected = [
        [0, 5, 8, 9],
        [float('inf'), 0, 3, 4],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected

def test_empty_graph():
    """Test that an empty graph raises a ValueError."""
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        floyd_warshall([])

def test_non_square_matrix():
    """Test that a non-square matrix raises a ValueError."""
    graph = [
        [0, 1, 2],
        [3, 4]  # Mismatched row length
    ]
    with pytest.raises(ValueError, match="Graph must be a square matrix"):
        floyd_warshall(graph)

def test_single_vertex_graph():
    """Test a graph with a single vertex."""
    graph = [[0]]
    result = floyd_warshall(graph)
    assert result == [[0]]

def test_graph_with_negative_edges():
    """Test a graph with negative edge weights."""
    graph = [
        [0, -1, 4],
        [float('inf'), 0, 3],
        [float('inf'), float('inf'), 0]
    ]
    expected = [
        [0, -1, 2],
        [float('inf'), 0, 3],
        [float('inf'), float('inf'), 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected