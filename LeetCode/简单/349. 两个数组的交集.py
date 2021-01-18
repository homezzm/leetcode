class Solution(object):
    def intersection(self, nums1, nums2):
        """
        https://leetcode-cn.com/problems/intersection-of-two-arrays/
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2: return []
        nums_set = set(nums1)
        li=[]
        for num in nums2:
            if num in nums_set and num not in li:
                li.append(num)
        return li

if __name__ == '__main__':
    solution = Solution()
    print(solution.intersection([1, 2, 2, 1], [2, 2]))
