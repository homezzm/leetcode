class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        https://leetcode-cn.com/problems/contains-duplicate-ii/
        """
        # 用字典查找
        # 元素存入key,索引存入value
        dic = {}
        # 遍历nums
        for i in range(len(nums)):
            # 如果有相同元素，匹配成功
            if nums[i] in dic:
                # 判断索引差
                # 小于k符合条件
                if i - dic[nums[i]] <= k:
                    return True
                # 不小于k则将索引更新为更接近未来匹配的那一个
                else:
                    dic[nums[i]] = i
            else:
                dic[nums[i]] = i

        return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.containsNearbyDuplicate([7,8,9,7], 3))
