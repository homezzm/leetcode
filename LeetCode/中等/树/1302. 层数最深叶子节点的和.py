# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque


class Solution(object):
    def deepestLeavesSum(self, root):
        """
        https://leetcode-cn.com/problems/deepest-leaves-sum/
        :type root: TreeNode
        :rtype: int
        第二版层次遍历，最后的结果是一个二维数组，计算最一组元素值即可
        """
        if not root:return 0
        q,res=deque(),[]
        q.append(root)
        while q:
            res.append([i.val for i in q])
            n=len(q)
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return sum(res[-1])


        #下面是第一版，
        # if not root: return 0
        # q, leafQueue, sumVal = deque(), deque(), 0
        # q.append(root)
        # while q:
        #     n = len(q)
        #     leafQueue.clear()
        #     for leafNode in range(n):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #         leafQueue.append(node)  # q1保存弹出的节点
        #     if len(q) == 0:  # 说明到了最后一层
        #         for leafNode in leafQueue:
        #             sumVal+=leafNode.val
        #
        # return sumVal
if __name__ == '__main__':
    root =TreeNode(val= 1, left= TreeNode(val= 2, left= TreeNode(val= 4, left= TreeNode(val= 7, left= None, right= None), right= None), right= TreeNode(val= 5, left= None, right= None)), right= TreeNode(val= 3, left= None, right= TreeNode(val= 6, left= None, right= TreeNode(val= 8, left= None, right= None))))
    sol=Solution()
    print(sol.deepestLeavesSum(root))