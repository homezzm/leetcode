class Solution(object):
    def fizzBuzz(self, n):
        """
        https://leetcode-cn.com/problems/fizz-buzz/
        :type n: int
        :rtype: List[str]
        """
        li = []
        for i in range(1, n + 1):
            strs = ""
            if i % 3 == 0:
                strs = "Fizz"
            if i % 5 == 0:
                strs += "Buzz"
            li.append(strs if len(strs) > 0 else str(i))
        return li


if __name__ == '__main__':
    solution = Solution()
    print(solution.fizzBuzz(15))
