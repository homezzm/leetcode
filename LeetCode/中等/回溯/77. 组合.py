class Solution(object):
    def combine(self, n, k):
        """
        https://leetcode-cn.com/problems/combinations/
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res, path = [], []

        def backtracking(n, k, startIndex):
            if len(path) == k:  # 终止条件
                res.append([i for i in path])  # 存放结果
                return
            for i in range(startIndex, n - (k - len(path)) + 2):  # 选择：本层集合中元素
                path.append(i)  # 处理节点
                print('递归前：', path)
                backtracking(n, k, i + 1)  # 递归
                path.pop()  # 回溯，撤销处理结果
                print('递归后：', path)

        backtracking(n, k, 1)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 2))
