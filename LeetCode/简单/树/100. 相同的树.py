# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    """
    https://leetcode-cn.com/problems/same-tree/
    """
    def isSameTree(self, p, q):
        if not p and not q: return True  # 两树都空
        if not p or not q: return False  # 一个树是空
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


if __name__ == '__main__':
    solution = Solution()

    qa1 = TreeNode(1)
    qa2 = TreeNode(2)
    qaNone = TreeNode(None)
    qa1.left = qa2
    qa1.right = qaNone

    pa1 = TreeNode(1)
    pa2 = TreeNode(2)
    paNone = TreeNode(None)
    pa1.left = pa2
    pa1.right = paNone

    print(solution.isSameTree(pa1, qa1))
