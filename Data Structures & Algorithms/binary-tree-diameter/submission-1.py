# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # helper function
    def maxDepth(self, root):
        if not root:
            return 0
        height = max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
        return height

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # make helper function to calculate depth of left and right children
        # we traverse the orignal BFS or DFS
        # we have a temp variable that stores the max path seen 
        # when we are done traversing we return variable
        q = [root]
        maxPath = 0
        while q: 
            currNode = q.pop(0)
            if currNode and currNode.left:
                q.append(currNode.left)
            if currNode and currNode.right:
                q.append(currNode.right)
            # calc current path length 
            currPath = self.maxDepth(currNode.left) + self.maxDepth(currNode.right)
            if currPath > maxPath:
                maxPath = currPath
        return maxPath


        