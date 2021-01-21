# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedListToBST(self, head):
        """
        https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/
        :type head: ListNode
        :rtype: TreeNode
        给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
        """

        inOrder = []
        if not head: return None

        while head:
            inOrder.append(head.val)
            head = head.next
        return self.generateTreeByInOrder(inOrder)

    def generateTreeByInOrder(self, inOrder):
        if len(inOrder) == 0: return

        midInx = len(inOrder) // 2
        rootVal = inOrder[midInx]
        root = TreeNode(rootVal)
        root.left = self.generateTreeByInOrder(inOrder[0:midInx])  # [-10, -3, 0, 5, 9]
        root.right = self.generateTreeByInOrder(inOrder[midInx + 1:])
        return root


if __name__ == '__main__':
    li = [-10, -3, 0, 5, 9]
    print(li[2 + 1:])
