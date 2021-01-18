class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = [0]
        for num in nums:
            self.dp.append(self.dp[-1] + num)


    def sumRange(self, i, j):
        """
        https://leetcode-cn.com/problems/range-sum-query-immutable/
        :type i: int
        :type j: int
        :rtype: int
        """
        print(self.dp[j + 1] - self.dp[i])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':
    li = [-2, 0, 3, -5, 2, -1]
    numArray = NumArray(li)
    # print(li)
    print(numArray.sumRange(0, 2))
