# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        q, res, isReverse = deque(), [], False
        q.append(root)
        while q:
            size = len(q)
            if isReverse:
                res.append([q[i].val for i in range(len(q) - 1, -1, -1)])
            else:
                res.append([i.val for i in q])
            for _ in range(size):
                node = q.popleft()
                if node.left:   q.append(node.left)
                if node.right:  q.append(node.right)
            isReverse = isReverse is False
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    n9 = TreeNode(9)
    n20 = TreeNode(20)
    n15 = TreeNode(15)
    n7 = TreeNode(7)

    root.left = n9
    root.right = n20
    n20.left = n15
    n20.right = n7

    solution = Solution()
    print(solution.zigzagLevelOrder(root))
