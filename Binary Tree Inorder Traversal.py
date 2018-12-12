# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 18:40:56 2018

@author: tyagi
"""

class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        final = []
        if root == None:
            return []
        
        stack.append(root)
        while len(stack) != 0:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            final.append(root.val)
            root = root.right
        return final[:-1]
    