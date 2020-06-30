class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root: TreeNode, left_node: TreeNode, right_node: TreeNode):

    if root is None:
        return None

    if root.val == left_node.val or root.val == right_node.val: # found one of the child nodes
        return root

    left = lowest_common_ancestor(root.left, left_node, right_node)
    right = lowest_common_ancestor(root.right, left_node, right_node)

    if left is None: return right
    if right is None: return left

    if left is not None and right is not None: # common ancestor
        return root
