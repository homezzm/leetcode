#!/usr/bin/env Python
# coding=utf-8
from LeetCode.Helpers import helperLiCreateTree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from LeetCode.GenBTreeByList import GenBiTreeByList


class Solution(object):
    def isCousins(self, root, x, y):
        """
        https://leetcode-cn.com/problems/cousins-in-binary-tree/
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        通过dfs把所有节点都搞一遍
        需要两个容器来记录每个节点的深度，与该节点的父节点
        """
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


        #print(depth)
        #print(parNode)


if __name__ == '__main__':
    root = helperLiCreateTree([1, 2, 3, 4])

    solution = Solution()
    print(solution.isCousins(root, 4, 3))
