# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution(object):
    def largestValues(self, root):
        """
        https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/
        :type root: TreeNode
        :rtype: List[int]
        广度优先搜索
        """
        res = []
        if not root: return res

        # DFS
        dicts = {}  # k层数 v这一层最大值

        def dfs(node, level):
            if not node: return

            if level not in dicts:  # 新的一层
                dicts[level] = node.val
            else:
                dicts[level] = max(node.val, dicts[level])
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)
        return [dicts[key] for key in dicts]

        # BFS
        # q = deque()
        # q.append(root)
        #
        # while q:
        #     n = len(q)
        #
        #     maxCount = float("-inf")
        #     for _ in range(n):  # 每一个循环都是一行
        #         node = q.popleft()
        #         maxCount = max(maxCount, node.val)
        #
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     res.append(maxCount)
        # return res


if __name__ == '__main__':
    root = TreeNode(val=0, left=TreeNode(val=-1, left=None, right=None), right=None)
    solution = Solution()
    print(solution.largestValues(root))

    print(float("-inf"))
