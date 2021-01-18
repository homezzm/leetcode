# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        https://leetcode-cn.com/problems/find-bottom-left-tree-value/
        :type root: TreeNode
        :rtype: int
        通常BFS遍历都是从上到下，从左到右。然而根据题目意思，是要取到最下面，最左边的元素。
        故只需要对BFS遍历稍作改进即可。具体思路为从上到下保持不变, 但水平遍历方向改为从右到左即可。
        如此一来，先上后下，先右后左，此策略走下去，最后一个元素必然是最下方最左边的元素，
        最后返回该节点node.val即可
        """
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.right:  # 先右后左
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val


if __name__ == '__main__':
    root = TreeNode(val=1)#;, left=TreeNode(val=1, left=None, right=None), right=TreeNode(val=3, left=None, right=None))

    # TreeNode(val= 2, left= TreeNode(val= 1, left= TreeNode(val= 4, left= TreeNode(val= 8, left= None, right= None), right= None), right= TreeNode(val= 5, left= None, right= None)), right= TreeNode(val= 3, left= TreeNode(val= 6, left= None, right= None), right= TreeNode(val= 7, left= None, right= None)))
    solution = Solution()
    print(solution.findBottomLeftValue(root))
