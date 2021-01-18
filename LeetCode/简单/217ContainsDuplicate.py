class Solution(object):
    def containsDuplicate(self, nums):
        """
        https://leetcode-cn.com/problems/contains-duplicate/
        """
        if not nums: return False
        dicts = {}
        for inx, num in enumerate(nums):
            if dicts.__contains__(num):
                return True
            else:
                dicts[num] = inx
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.containsDuplicate(  [1,1,1,3,3,4,3,2,4,2]))
