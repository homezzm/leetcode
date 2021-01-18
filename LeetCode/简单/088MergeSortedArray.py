class Solution(object):
    """
    https://leetcode-cn.com/problems/merge-sorted-array/
    """
    def merge(self, nums1, m, nums2, n):
        p, p1, p2 = m + n - 1, m - 1, n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]

if __name__ == '__main__':
    solution = Solution()
    nums1 = [2, 0]
    nums2 = [1]
    solution.merge(nums1, 1, nums2, 1)
    print(nums1)
