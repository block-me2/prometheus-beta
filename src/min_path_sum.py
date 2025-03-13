class TreeNode:
    """
    A class representing a node in a binary tree.
    
    Attributes:
        val (int): The value stored in the node.
        left (TreeNode, optional): Left child node. Defaults to None.
        right (TreeNode, optional): Right child node. Defaults to None.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_path_sum(root):
    """
    Find the minimum path sum from root to any leaf in a binary tree.
    
    Args:
        root (TreeNode): The root of the binary tree.
    
    Returns:
        int: The minimum path sum from root to a leaf.
        None: If the tree is empty (root is None).
    
    Raises:
        TypeError: If the input is not a TreeNode or None.
    
    Time Complexity: O(n), where n is the number of nodes in the tree
    Space Complexity: O(h), where h is the height of the tree (recursion stack)
    """
    # Check for invalid input
    if root is None:
        return None
    
    # Validate input type
    if not isinstance(root, TreeNode):
        raise TypeError("Input must be a TreeNode or None")
    
    # If leaf node, return its value
    if root.left is None and root.right is None:
        return root.val
    
    # Recursively get min path sums of left and right subtrees
    left_min = min_path_sum(root.left) if root.left else float('inf')
    right_min = min_path_sum(root.right) if root.right else float('inf')
    
    # Return the minimum of left and right path sums plus current node's value
    return root.val + min(left_min, right_min)