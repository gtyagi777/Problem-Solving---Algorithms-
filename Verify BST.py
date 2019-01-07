<<<<<<< HEAD
class Node:
    def __init__(self,key,val):
        self.key = key
        self.value = val
        self.left = None
        self.right = None

def tree_max(node):
    if not node:
        return float("-inf")
    maxLeft = tree_max(node.left)
    maxRight = tree_max(node.right)
    return max(node.key, maxLeft, maxRight)


def tree_min(node):
    if not node:
        return float("inf")
    minLeft = tree_min(node.left)
    minRight = tree_min(node.right)
    return min(node.key, minLeft, minRight)

def verify(node):
    if not node:
        return True
    if (tree_max(node.left) <= node.key <= tree_min(node.right) and
        verify(node.left) and verify(node.right)):
        return True
    else:
        return False

=======
class Node:
    def __init__(self,key,val):
        self.key = key
        self.value = val
        self.left = None
        self.right = None

def tree_max(node):
    if not node:
        return float("-inf")
    maxLeft = tree_max(node.left)
    maxRight = tree_max(node.right)
    return max(node.key, maxLeft, maxRight)


def tree_min(node):
    if not node:
        return float("inf")
    minLeft = tree_min(node.left)
    minRight = tree_min(node.right)
    return min(node.key, minLeft, minRight)

def verify(node):
    if not node:
        return True
    if (tree_max(node.left) <= node.key <= tree_min(node.right) and
        verify(node.left) and verify(node.right)):
        return True
    else:
        return False

>>>>>>> 34dcdbaf7606329ea73cdb976296a4aeaa79cb79
