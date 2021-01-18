# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        搜集出所有的路径，放到列表中
        """
        paths = []
        if not root: return paths

        def dfs(node, li, sumVal):
            if not node: return

            sumVal -= node.val
            li.append(node.val)  # 收集节点 根左右

            if not node.left and not node.right:
                if sumVal == 0:
                    paths.append(li[:])

            dfs(node.left, li, sumVal)
            dfs(node.right, li, sumVal)
            li.pop()  # 回溯 因为li不能一直加入节点，它还要删节点，然后才能加入新的节点。

        dfs(root, [], sum)
        return paths


if __name__ == '__main__':
    root = TreeNode(val=5, left=TreeNode(val=4, left=TreeNode(val=11, left=TreeNode(val=7, left=None, right=None),
                                                              right=TreeNode(val=2, left=None, right=None)),
                                         right=None),
                    right=TreeNode(val=8, left=TreeNode(val=13, left=None, right=None),
                                   right=TreeNode(val=4, left=TreeNode(val=5, left=None, right=None),
                                                  right=TreeNode(val=1, left=None, right=None))))

    solution = Solution()
    print(solution.pathSum(root, 22))

    # ll=[1,2,3,4,5]
    # print(ll[:])
