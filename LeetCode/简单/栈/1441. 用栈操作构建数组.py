class Solution(object):
    def buildArray(self, target, n):
        """
        https://leetcode-cn.com/problems/build-an-array-with-stack-operations/
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        li, j = [], 0
        for i in range(1, n + 1):
            if j >= len(target): break;
            if i < target[j]:
                li.append('Push')
                if i not in target:  # 没有就是被删除了
                    li.append("Pop")
            else:
                li.append('Push')
                j += 1
        return li


if __name__ == '__main__':
    solution = Solution()
    solution.buildArray([1, 2,3], 3)
