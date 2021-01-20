# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def checkSubTree(self, t1, t2):
        """
        https://leetcode-cn.com/problems/check-subtree-lcci/
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: bool
        检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。
        设计一个算法，判断 T2 是否为 T1 的子树。
        如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，
        从节点 n 处把树砍断，得到的树与 T2 完全相同。

        thinking:题目说了数量非常大，递归啥的就不方便了，而且还说了是【一模一样】的，
        能不能获取两棵树的前序，然后t2在t1里进行匹配即可
        前序根节点在第一个位置 t1=[1,2,3,4,5] t2=[3,4] 这就变成了子串匹配的问题了
        """
        if not t1 or not t2:
            return True
        nodeLi1, nodeLi2 = [], []

        self.preOrder(t1, nodeLi1)
        self.preOrder(t2, nodeLi2)

        node1StartInx = node1EndInx = -1
        if nodeLi2[0] in nodeLi1:
            node1StartInx = nodeLi1.index(nodeLi2[0])
        if nodeLi2[-1] in nodeLi1:
            node1EndInx = nodeLi1.index(nodeLi2[-1])

        if node1StartInx < 0 or node1EndInx < 0: return False  # 没有找到
        if len(nodeLi2) != len(nodeLi1[node1StartInx:node1EndInx + 1]): return False  # 不一样长

        for t2Val in nodeLi2:
            if t2Val != nodeLi1[node1StartInx]:
                return False
            node1StartInx += 1

        return True

    def preOrder(self, node, li):
        if not node: return
        li.append(node.val)
        self.preOrder(node.left, li)
        self.preOrder(node.right, li)


if __name__ == '__main__':
    t1 = TreeNode(val=1, left=TreeNode(val=2, left=None, right=None), right=TreeNode(val=3, left=None, right=None))
    t2 = TreeNode(val=2, left=None, right=None)

    solution = Solution()
    print(solution.checkSubTree(t1, t2))
    # val = 2^=ord(2)
    # print()
