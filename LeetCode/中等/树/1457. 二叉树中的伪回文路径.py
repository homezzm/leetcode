# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import Counter
import collections


class Solution(object):
    def pseudoPalindromicPaths(self, root):
        """
        https://leetcode-cn.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
        https://leetcode-cn.com/problems/pseudo-palindromic-paths-in-a-binary-tree/solution/wei-yun-suan-jie-fa-by-dnanki/
        :type root: TreeNode
        :rtype: int
        给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，
        当它满足：路径经过的所有节点值的排列中，存在一个回文序列。

        判定条件即为出现单数次的数最多只能有一个。
        """
        self.res = 0

        def dfs(node, temp):
            temp ^= 1 << node.val  # node节点的val为几就左移几位
            if not node.left and not node.right:
                if temp == 0 or temp & (temp - 1) == 0:
                    self.res += 1

            if node.left: dfs(node.left, temp)
            if node.right: dfs(node.right, temp)

        dfs(root, 0)
        return self.res

        # self.res = 0
        #
        # def dfs(node, dicts):
        #     if not node: return
        #
        #     dictsCopy = dicts.copy()
        #     dictsCopy[node.val] += 1
        #     if not node.left and not node.right:
        #         if sum([i for i in dictsCopy.values() if i % 2 == 1]) <= 1:
        #             self.res += 1
        #             return
        #
        #     dfs(node.left, dictsCopy)
        #     dfs(node.right, dictsCopy)
        #
        # dfs(root, collections.defaultdict(int))
        # return self.res


if __name__ == '__main__':
    root = TreeNode(val=8, left=TreeNode(val=6, left=None, right=None), right=TreeNode(val=9, left=None,
                                                                                       right=TreeNode(val=4,
                                                                                                      left=TreeNode(
                                                                                                          val=4,
                                                                                                          left=TreeNode(
                                                                                                              val=5,
                                                                                                              left=None,
                                                                                                              right=None),
                                                                                                          right=TreeNode(
                                                                                                              val=4,
                                                                                                              left=TreeNode(
                                                                                                                  val=8,
                                                                                                                  left=None,
                                                                                                                  right=None),
                                                                                                              right=None)),
                                                                                                      right=TreeNode(
                                                                                                          val=1,
                                                                                                          left=None,
                                                                                                          right=None))))

    solution = Solution()
    print(solution.pseudoPalindromicPaths(root))

    lii = [8, 9, 4, 4, 4, 8]
    print(Counter(lii))

    # des=[[0,0,0],[0,0,0],[0,0,0]]
    des = [[0] * 3] * 3
    des[0][0] = 1
    print(des)
