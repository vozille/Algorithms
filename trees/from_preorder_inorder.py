def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder) and len(preorder):
            idx = inorder.index(preorder.pop(0)) # could be queue
            root = TreeNode(inorder[idx])
            left_values = inorder[:idx]
            right_values = inorder[idx + 1:]
            root.left = self.buildTree(preorder, left_values)
            root.right = self.buildTree(preorder, right_values)
            return root
