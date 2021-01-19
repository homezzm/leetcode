# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import Counter


class Solution(object):
    def pseudoPalindromicPaths(self, root):
        """
        https://leetcode-cn.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
        :type root: TreeNode
        :rtype: int
        给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，
        当它满足：路径经过的所有节点值的排列中，存在一个回文序列。
        thinking:如果集合中所有元素的某种排列是回文串，那么集合中最多有一种元素出现了奇数次。
        根据这条进行判断即可，收集所有路径，找到符合条件的路径
        """
        res =  0

        def dfs(node, li):
            if not node: return
            nonlocal res

            li.append(node.val)
            if not node.left and not node.right:
                dicts, oddCount = Counter(li), 0
                for k in dicts.keys():
                    if dicts[k] % 2 == 1:
                        oddCount += 1
                if oddCount <= 1:
                    res += 1
            dfs(node.left, li)
            dfs(node.right, li)
            li.pop()  # 回溯一下

        dfs(root, [])
        return res


if __name__ == '__main__':
    # root = TreeNode(val=2, left=TreeNode(val=3, left=TreeNode(val=3, left=None, right=None),
    #                                      right=TreeNode(val=1, left=None, right=None)),
    #                 right=TreeNode(val=1, left=None, right=TreeNode(val=1, left=None, right=None)))

    # root = TreeNode(val=2, left=TreeNode(val=1, left=TreeNode(val=1, left=None, right=None),
    #                                      right=TreeNode(val=3, left=None,
    #                                                     right=TreeNode(val=1, left=None, right=None))),
    #                 right=TreeNode(val=1, left=None, right=None))

    solution = Solution()
    print(solution.pseudoPalindromicPaths(root))
