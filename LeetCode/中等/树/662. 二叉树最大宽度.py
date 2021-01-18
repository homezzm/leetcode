# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        https://leetcode-cn.com/problems/maximum-width-of-binary-tree/
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        root.val = ans = 0
        q=deque()
        q.append(root)
        while q:
            n = len(q)
            ans = max(q[-1].val - q[0].val + 1, ans)
            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    node.left.val = node.val * 2 + 1
                if node.right:
                    q.append(node.right)
                    node.right.val = node.val * 2 + 2
        return ans

        # queue = [(root, 0, 0)]
        # cur_depth = left = ans = 0
        # for node, depth, pos in queue:
        #     if node:
        #         queue.append((node.left, depth + 1, pos * 2))
        #         queue.append((node.right, depth + 1, pos * 2 + 1))
        #         if cur_depth != depth:
        #             cur_depth = depth
        #             left = pos
        #         ans = max(pos - left + 1, ans)
        #
        # return ans


if __name__ == '__main__':
    root = TreeNode(val=1, left=TreeNode(val=3, left=TreeNode(val=5, left=None, right=None),
                                         right=TreeNode(val=3, left=None, right=None)),
                    right=TreeNode(val=2, left=None, right=TreeNode(val=9, left=None, right=None)))
    solution = Solution()
    print(solution.widthOfBinaryTree(root))
