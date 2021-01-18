# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution(object):
    def isEvenOddTree(self, root):
        """
        https://leetcode-cn.com/problems/even-odd-tree/
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return False
        q, level = deque(), 0
        q.append(root)

        while q:
            n, preVal = len(q), 0

            for _ in range(n):
                node = q.popleft()

                if level % 2 == 0:  # 偶数下标 层上的所有节点的值都是 奇 整数，从左到右按顺序 严格递增
                    if node.val % 2 == 0 or preVal != 0 and preVal >= node.val:
                        return False
                else:
                    if node.val % 2 == 1 or preVal != 0 and preVal <= node.val:# 层上的所有节点的值都是 偶 整数
                        return False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                preVal = node.val

            level += 1
        return True


if __name__ == '__main__':
    # root = TreeNode(val=1, left=TreeNode(val=10, left=TreeNode(val=3, left=TreeNode(val=12, left=None, right=None),
    #                                                            right=TreeNode(val=8, left=None, right=None)),
    #                                      right=None),
    #                 right=TreeNode(val=4, left=TreeNode(val=7, left=TreeNode(val=6, left=None, right=None), right=None),
    #                                right=TreeNode(val=9, left=None, right=TreeNode(val=2, left=None, right=None))))
    root = TreeNode(val= 5, left= TreeNode(val= 4, left= TreeNode(val= 3, left= None, right= None), right= TreeNode(val= 3, left= None, right= None)), right= TreeNode(val= 2, left= TreeNode(val= 7, left= None, right= None), right= None))
    #root = TreeNode(val= 11, left= TreeNode(val= 8, left= TreeNode(val= 1, left= TreeNode(val= 30, left= TreeNode(val= 17, left= None, right= None), right= None), right= TreeNode(val= 20, left= None, right= None)), right= TreeNode(val= 3, left= TreeNode(val= 18, left= None, right= None), right= TreeNode(val= 16, left= None, right= None))), right= TreeNode(val= 6, left= TreeNode(val= 9, left= TreeNode(val= 12, left= None, right= None), right= TreeNode(val= 10, left= None, right= None)), right= TreeNode(val= 11, left= TreeNode(val= 4, left= None, right= None), right= TreeNode(val= 2, left= None, right= None))))
    #root =TreeNode(val=1)
    solution = Solution()
    print(solution.isEvenOddTree(root))
