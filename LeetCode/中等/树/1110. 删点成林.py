# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def delNodes(self, root, to_delete):
        """
        https://leetcode-cn.com/problems/delete-nodes-and-return-forest/
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        判断断开的节点：
            如果左节点为待删除节点，断开左节点连接
            如果右节点为待删除节点，断开右节点连接
        判断需要添加的节点：
            如果当前节点为待删除节点
                如果如果左节点不删除，添加左节点
                如果如果右节点不删除，添加右节点
        """

        toDel, res = set(to_delete), []
        if root.val not in toDel:
            res.append(root)

        def dfs(node):
            if node is None: return
            left, right = node.left, node.right

            if node.val in toDel:
                if left and left.val not in toDel:
                    res.append(left)
                if right and right.val not in toDel:
                    res.append(right)

            if left and left.val in toDel:
                node.left = None
            if right and right.val in toDel:
                node.right = None
            dfs(left)
            dfs(right)

        dfs(root)
        return res


if __name__ == '__main__':
    root = TreeNode(x=1, left=TreeNode(x=2, left=TreeNode(x=4, left=None, right=None),
                                       right=TreeNode(x=5, left=None, right=None)),
                    right=TreeNode(x=3, left=TreeNode(x=6, left=None, right=None),
                                   right=TreeNode(x=7, left=None, right=None)))
    solution = Solution()
    print(solution.delNodes(root, [3, 5]))
