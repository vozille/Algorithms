import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# this is like BFS for a tree
def get_level_order_traversal():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    node_queue = queue.Queue()
    result = []

    node_queue.put(root)
    while not node_queue.empty():
        row = []
        for i in range(node_queue.qsize()):
            node = node_queue.get()
            row.append(node.val)
            if node.left: 
                node_queue.put(node.left)
            if node.right: 
                node_queue.put(node.right)
        result.append(row)

    return result
