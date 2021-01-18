# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees/
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        中序搞起来，再合并
        """
        li1, li2 = [], []

        def inOrder(node, li):
            if not node: return li
            inOrder(node.left, li)
            li.append(node.val)
            inOrder(node.right, li)
            return li

        li1 = inOrder(root1, li1)
        li2 = inOrder(root2, li2)
        return sorted(li1 + li2)

if __name__ == '__main__':
    root1=TreeNode(val= 2, left= TreeNode(val= 1, left= None, right= None), right= TreeNode(val= 4, left= None, right= None))
    root2=TreeNode(val= 1, left= TreeNode(val= 0, left= None, right= None), right= TreeNode(val= 3, left= None, right= None))
    solution=Solution()
    print(solution.getAllElements(root1,root2))
