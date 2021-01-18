# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from collections import Counter


class Solution(object):
    def isCompleteTree(self, root):
        """
        https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree/
        :type root: TreeNode
        :rtype: bool
        用层次遍历，把树每一层的节点都放到队列中，
        如果队列中有空值，且空值不是这一层的最后一个元素，这就不是一个完全二叉树
           1
          2，3
        4，5，n. 6
        代码中的pre用的妙
        """
        if not root: return False
        q, pre = deque(), root
        q.append(root)
        while q:
            node = q.popleft()
            if pre is None and node:
                return False
            if node:
                q.append(node.left)
                q.append(node.right)
            pre = node
        return True


if __name__ == '__main__':
    root = TreeNode(val= 1, left= TreeNode(val= 2, left= TreeNode(val= 5, left= None, right= None), right= None), right= TreeNode(val= 3, left= TreeNode(val= 7, left= None, right= None), right= None))


    solution = Solution()
    print(solution.isCompleteTree(root))
# q = deque()
# q.append(1)
# q.append(2)
# q.append(None)
# print(q[-1] is None)
