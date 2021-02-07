class Solution(object):
    def verifyPostorder(self, postorder):
        """
        https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
        :type postorder: List[int]
        :rtype: bool
        输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
        输入: [1,6,3,2,5] 输出: false
        输入: [1,3,2,6,5] 输出: true
        [1,3,2]
        left=1 right=2
        """

        def dfs(left, right):
            if left >= right: return True #只有一个元素直接返回

            inx = left
            # 确保postorder[left:mid-1]都是比根节点小的值
            while postorder[inx] < postorder[right]:
                inx += 1
            mid = inx
            while postorder[inx] > postorder[right]:
                inx += 1
            # inx==right表示右子树中没有小于根节点的值，所以是一颗正常的二叉搜索树
            return inx == right and dfs(left, mid - 1) and dfs(mid, right - 1)

        return dfs(0, len(postorder) - 1)
