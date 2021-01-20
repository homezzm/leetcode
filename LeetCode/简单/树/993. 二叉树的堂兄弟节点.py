#!/usr/bin/env Python
# coding=utf-8
from LeetCode.Helpers import helperLiCreateTree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from LeetCode.GenBTreeByList import GenBiTreeByList

from collections import deque


class Solution(object):
    def isCousins(self, root, x, y):
        """
        https://leetcode-cn.com/problems/cousins-in-binary-tree/
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        如果二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。
        媳妇思路：

        我的思路：通过dfs把所有节点都搞一遍
        需要两个容器来记录每个节点的深度，与该节点的父节点
        """

        # if not root: return False
        # q = deque()
        # q.append(root)
        # while q:
        #     length = len(q)
        #
        #     if x in q and y in q:  # 如果xy在同一层
        #         xInx = q.index(x)
        #         yInx = q.index(y)
        #         if (xInx // 2) == (yInx // 2):  # 如果相同则表示两个节点是同一个爹，造孽啊!
        #             return True
        #
        #     for _ in range(length):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return False

        # 我的思路
        depth, parNode = dict(), dict()

        def dfs(node, par):
            if not node: return

            if not par:
                depth[node.val] = 1
            else:
                depth[node.val] = depth.get(par.val) + 1

            par = node

            if node.left:
                parNode[node.left.val] = par.val
            if node.right:
                parNode[node.right.val] = par.val
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        return depth[x]==depth[y] and parNode[x] != parNode[y] #深度相同 但父节点不同


if __name__ == '__main__':
    # root = helperLiCreateTree([1, 2, 3, 4])
    #
    # solution = Solution()
    # print(solution.isCousins(root, 4, 3))
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    qq = deque()
    qq.append(t1)
    qq.append(t2)
    f = lambda val: [i.val == val for i in enumerate(qq)]
    print(f(2))
