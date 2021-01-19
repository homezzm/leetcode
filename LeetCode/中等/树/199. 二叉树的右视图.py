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
        thinking:深度优先，只搜索右侧节点，至顶向下，
        特判是，如果这个节点有左节点，但没有右节点，那就要放容器中添加左节点，然后在继续判断是否有右节点
        if 有右节点：添加
        elif 没有右节点，但有左节点，添加

        bfs进队列，每一层队列中最后一个元素就是右边看到的节点
        """

        if not root: return []
        q, res = deque(), []
        q.append(root)
        while q:
            length = len(q)
            res.append(q[-1].val)
            for _ in range(length):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res

        # res = []
        #
        # def dfs(node):
        #     if not node: return
        #     res.append(node.val)
        #     if node.right:
        #         dfs(node.right)
        #     else:
        #         dfs(node.left)
        #
        # dfs(root)
        # return res


if __name__ == '__main__':
    root = TreeNode(val=1, left=TreeNode(val=2, left=None, right=TreeNode(val=5, left=None, right=None)),
                    right=TreeNode(val=3, left=None, right=TreeNode(val=4, left=None, right=None)))
    solution = Solution()
    print(solution.rightSideView(root))
