# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


from collections import deque


class Solution(object):
    def listOfDepth(self, tree):
        """
        https://leetcode-cn.com/problems/list-of-depth-lcci/
        :type tree: TreeNode
        :rtype: List[ListNode]
        给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。
        返回一个包含所有深度的链表的数组。
        """
        if not tree: return []
        # # dfs
        # ans = []  # k是层号 v是节点值从左到右 #前序遍历
        #
        # def dfs(node, level):
        #     if not node: return
        #
        #     if len(ans) == level:  # 新的一层
        #         ans.append(ListNode(node.val))
        #     else:
        #         head = ListNode(node.val)  # 头插法
        #         head.next = ans[level]
        #         ans[level] = head
        #
        #     dfs(node.right, level + 1)
        #     dfs(node.left, level + 1)
        #
        # dfs(tree, 0)
        # return ans

        # bfs
        q, res = deque(), []
        q.append(tree)
        while q:
            dummy, length = ListNode(0), len(q)
            listTableHead = dummy
            for _ in range(length):
                treeNode = q.popleft()

                listNode = ListNode(treeNode.val)
                dummy.next = listNode
                dummy = listNode

                if treeNode.left:
                    q.append(treeNode.left)
                if treeNode.right:
                    q.append(treeNode.right)
            res.append(listTableHead.next)
        return res
