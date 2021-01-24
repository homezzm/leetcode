# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBiNode(self, root):
        """
        https://leetcode-cn.com/problems/binode-lcci/
        :type root: TreeNode
        :rtype: TreeNode
        二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。
        实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉搜索树的性质，转换操作应是原址的，
        也就是在原始的二叉搜索树上直接修改。
        """
        if not root: return root
        prev, dummy = None, TreeNode(-1)

        def inOrder(node):
            nonlocal prev
            if not node: return
            inOrder(node.left)

            if not prev:  # 第一个节点
                prev = node  # 记录第一个节点
                dummy.right = node  # 记录它，它将作为单链表的表头
            else:  # 第一个节点之后的节点
                prev.right = node  # 前一个节点的右指针指向当前节点
                prev = node  # 更新perv指向
            node.left = None

            inOrder(node.right)

        inOrder(root)

        return dummy.right

if __name__ == '__main__':
    li=[1,2,3]
    tt=li
    print(id(li),'--',id(tt))
