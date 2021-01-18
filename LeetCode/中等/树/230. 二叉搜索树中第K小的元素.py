# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    #通过构造 BST 的中序遍历序列，则第 k-1 个元素就是第 k 小的元素。
    def kthSmallest1(self, root, k):
        # 这是官方代码，挺牛的，学习[11]+[22]=[11,22]python中两个列表相加会变成一个列表
        def inOrder(node):
            return inOrder(node.left) + [node.val] + inOrder(node.right) if node else []

        return inOrder(root)[k - 1]

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        放到数组中，然后二分查找
        """

        li = []

        def dfs(node):  # 中序遍历就是有序的
            if not node: return
            dfs(node.left)
            li.append(node.val)
            dfs(node.right)

        dfs(root)
        # print(li)
        return self.binarySearch(li, k)

    def binarySearch(self, li, k):  # 必须是排序后的
        left, right = 0, len(li) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if (mid + 1) == k:
                return li[mid]
            elif (mid + 1) > k:
                right -= 1
            else:
                left += 1
        else:
            return None


if __name__ == '__main__':
    root = TreeNode(val=5,
                    left=TreeNode(val=3, left=TreeNode(val=2, left=TreeNode(val=1, left=None, right=None), right=None),
                                  right=TreeNode(val=4, left=None, right=None)),
                    right=TreeNode(val=6, left=None, right=None))
    solution = Solution()
    # print(solution.kthSmallest(root,1))
    li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
          30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    # li=[1,2,3,4]
    print(solution.binarySearch(li, 12))
