class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2: return []
        if len(nums1) > len(nums2):  # 把小的数组做成哈希
            return self.intersect(nums2, nums1)
        dicts = {}
        result = []
        for num in nums1:
            if num in dicts:
                dicts[num] += 1
            else:
                dicts[num] = 1

        for num in nums2:
            if num in dicts and dicts[num] > 0:
                dicts[num] -= 1
                result.append(num)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
