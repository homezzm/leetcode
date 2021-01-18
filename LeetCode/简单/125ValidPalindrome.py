class Solution(object):
    """
    https://leetcode-cn.com/problems/valid-palindrome/
    """
    def isPalindrome(self, s):
        if not s: return True
        filter_str = "".join(filter(str.isalnum, s)).lower()
        left, right = 0, len(filter_str) - 1
        while left <= right:
            if filter_str[left] == filter_str[right]:
                left += 1
                right -= 1
            else:
                return False

        return True

        # filter_str = "".join(filter(str.isalnum, s)).lower()
        # li = []
        # for ch in filter_str[::-1]:
        #     li.append(ch)
        # return "".join(li) == filter_str


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
