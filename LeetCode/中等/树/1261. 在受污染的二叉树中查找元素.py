# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class FindElements(object):
    """
    给出一个满足下述规则的二叉树：
    root.val == 0
        如果 treeNode.val == x 且treeNode.left != null，那么treeNode.left.val == 2 * x + 1
        如果 treeNode.val == x 且 treeNode.right != null，那么treeNode.right.val == 2 * x + 2
    现在这个二叉树受到「污染」，所有的treeNode.val都变成了-1。
    请你先还原二叉树，然后实现FindElements类：
        FindElements(TreeNode* root)用受污染的二叉树初始化对象，你需要先把它还原。
        bool find(int target)判断目标值target是否存在于还原后的二叉树中并返回结果。
    """

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if not root: return
        self.treeVals = set()
        def dfs(node, val):
            if not node: return
            node.val = val
            self.treeVals.add(val)
            dfs(node.left, 2 * node.val + 1)
            dfs(node.right, 2 * node.val + 2)

        dfs(root, 0)
        # 自己写的递归
        # root.val = 0
        # self.treeVals = [root.val]
        #
        # def dfs(node):
        #     if not node: return
        #
        #     if node.left:
        #         node.left.val = 2 * node.val + 1
        #         self.treeVals.append(node.left.val)
        #     if node.right:
        #         node.right.val = 2 * node.val + 2
        #         self.treeVals.append(node.right.val)
        #     dfs(node.left)
        #     dfs(node.right)
        #
        # dfs(root)

        # 层次遍历搞定
        # root.val = 0
        #
        # q = deque()
        # q.append(root)
        #
        # self.treeVals = [root.val]
        #
        # while q:
        #     node = q.popleft()
        #     if node.left:
        #         node.left.val = 2 * node.val + 1
        #         q.append(node.left)
        #         self.treeVals.append(node.left.val)
        #     if node.right:
        #         node.right.val = 2 * node.val + 2
        #         q.append(node.right)
        #         self.treeVals.append(node.right.val)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.treeVals


if __name__ == '__main__':
    # root = TreeNode(val=-1, left=None, right=TreeNode(val=-1, left=TreeNode(val=-1, left=TreeNode(val=-1, left=None,
    #                                                                                               right=None),
    #                                                                         right=None), right=None))
    root = TreeNode(val=0, left=TreeNode(val=1, left=None, right=None),
                    right=TreeNode(val=-1, left=TreeNode(val=-1, left=None, right=None),
                                   right=TreeNode(val=-1, left=None, right=TreeNode(val=0, left=None, right=None))))

    obj = FindElements(root)
    print(obj.treeVals)
    # print(obj.find(2))  # return True
    # print(obj.find(3))  # return False
    # print(obj.find(4))  # return False
    # print(obj.find(5))  # return True
