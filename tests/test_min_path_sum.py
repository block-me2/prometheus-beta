import pytest
from src.min_path_sum import TreeNode, min_path_sum

class TestMinPathSum:
    def test_empty_tree(self):
        """Test that None is returned for an empty tree"""
        assert min_path_sum(None) is None
    
    def test_single_node_tree(self):
        """Test a tree with only a root node"""
        root = TreeNode(5)
        assert min_path_sum(root) == 5
    
    def test_simple_tree_with_left_path(self):
        """Test a simple tree with a left path"""
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        assert min_path_sum(root) == 15  # 10 + 5
    
    def test_simple_tree_with_right_path(self):
        """Test a simple tree with a right path"""
        root = TreeNode(10)
        root.left = TreeNode(15)
        root.right = TreeNode(5)
        assert min_path_sum(root) == 15  # 10 + 5
    
    def test_complex_tree(self):
        """Test a more complex tree with multiple paths"""
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(7)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(8)
        assert min_path_sum(root) == 13  # 10 + 3
    
    def test_unbalanced_tree(self):
        """Test an unbalanced tree"""
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(1)
        assert min_path_sum(root) == 16  # 10 + 5 + 1
    
    def test_negative_values(self):
        """Test a tree with negative values"""
        root = TreeNode(-10)
        root.left = TreeNode(5)
        root.right = TreeNode(-15)
        assert min_path_sum(root) == -20  # -10 + -10
    
    def test_invalid_input(self):
        """Test that TypeError is raised for invalid input"""
        with pytest.raises(TypeError):
            min_path_sum("not a tree")
        with pytest.raises(TypeError):
            min_path_sum(5)