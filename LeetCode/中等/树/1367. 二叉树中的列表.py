# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        https://leetcode-cn.com/problems/linked-list-in-binary-tree/
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return False

        def dfs(headLink, node):
            #特判：链表走完了，返回true
            if not headLink: return True

            #特判：链表没走完，树走完了，这肯定不行，返回false 如果值不同，必定不是啊
            if not node or node.val != headLink.val: return False

            #如果值相同，继续看，左边和右边有一个满足即可
            return dfs(headLink.next, node.left) or dfs(headLink.next, node.right)

        #先判断当前的节点，如果不对，再看左子树和右子树呗
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
