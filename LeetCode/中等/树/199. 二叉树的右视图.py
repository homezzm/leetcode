# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution(object):
    def rightSideView(self, root):
        """
        https://leetcode-cn.com/problems/binary-tree-right-side-view/
        :type root: TreeNode
        :rtype: List[int]
        给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
        thinking:1.bfs进队列，每一层队列中最后一个元素就是右边看到的节点O(n) O(n)
        2.dfs记录深度，使用根->右->左遍历 就可以保证每层都是最先访问最右边的节点的。
        """
        # bfs
        # if not root: return []
        # q, res = deque(), []
        # q.append(root)
        # while q:
        #     length = len(q)
        #     res.append(q[-1].val)
        #     for _ in range(length):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return res

        # dfs
        res = []

        def dfs(node, depth):
            if not node: return
            # 如果当前节点所在深度还没有出现在res里，
            # 说明在该深度下当前节点是第一个被访问的节点，因此将当前节点加入res中。
            if depth == len(res):  # 其实就是一层只加一个元素，就是最右边的那个
                res.append(node.val)
            depth += 1
            dfs(node.right, depth)
            dfs(node.left, depth)

        dfs(root, 0)
        return res


if __name__ == '__main__':
    root = TreeNode(val=1, left=TreeNode(val=2, left=None, right=TreeNode(val=5, left=None, right=None)),
                    right=TreeNode(val=3, left=None, right=TreeNode(val=4, left=None, right=None)))
    solution = Solution()
    print(solution.rightSideView(root))
