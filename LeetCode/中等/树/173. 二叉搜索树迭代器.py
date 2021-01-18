# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


# https://leetcode-cn.com/problems/binary-search-tree-iterator/
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodeQueue = deque()
        self.inOrder(root)
        print('队列中的内容：', self.nodeQueue)

    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        self.nodeQueue.append(root.val)
        self.inOrder(root.right)

    def next(self):
        """
        :rtype: int
        """
        return self.nodeQueue.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.nodeQueue) > 0


# Your BSTIterator object will be instantiated and called as such:
if __name__ == '__main__':
    root = TreeNode(val=7, left=TreeNode(val=3, left=None, right=None),
                    right=TreeNode(val=15, left=TreeNode(val=9, left=None, right=None),
                                   right=TreeNode(val=20, left=None, right=None)))
    obj = BSTIterator(root)
    param_1 = obj.next()
    param_2 = obj.hasNext()
    print(param_1)
    print(param_2)
