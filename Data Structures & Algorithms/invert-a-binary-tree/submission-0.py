# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # create a queue/list
        # Do a BFS
        # at each level we swap the left and right child 
        # return the new list
        if not root: 
            return root
            
        tree = []
        result = root
        tree.append(root)
        while tree:
            currNode = tree.pop(0)
            if currNode and currNode.left:
                tree.append(currNode.left)
            if currNode and currNode.right:
                tree.append(currNode.right)
            temp = currNode.left
            currNode.left = currNode.right
            currNode.right = temp
        return result
        