# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            print("Elim null")
            return(root)
        
        #when nodes ARE descendants of themselves
        if root in (p,q):
            print("LCA is a selected descendant node",root.val)
            return(root)        
        
        right=(self.lowestCommonAncestor(root.right, p, q))
        left=(self.lowestCommonAncestor(root.left, p, q))
        
        #when nodes are not descendants of themselves
        if(left and right):
            print("LCA is not a selected descendant node",root.val)
            return(root)
        if left:
            print("Elim Left",root.val)
            return(left)
        else:
            print("Elim Right",root.val)
            return(right)