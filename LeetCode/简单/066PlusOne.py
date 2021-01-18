class Solution(object):
    def plusOne(self, digits):
        """
        给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
        最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
        你可以假设除了整数 0 之外，这个整数不会以零开头。

        示例1：
        输入：digits = [1,2,3]
        输出：[1,2,4]
        解释：输入数组表示数字 123。

        示例2：
        输入：digits = [4,3,2,1]
        输出：[4,3,2,2]
        解释：输入数组表示数字 4321。
        示例 3：

        输入：digits = [0]
        输出：[1]

        提示：
        1 <= digits.length <= 100
        0 <= digits[i] <= 9
        """
        if not digits: return digits
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry == 0: break
            value = digits[i] + carry
            digits[i] = value % 10
            carry = value // 10
        if carry == 1:
            newDigits = [carry]
            newDigits[1:len(digits)] = digits[0: len(digits)]
            return newDigits
        else:
            return digits


if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne([9,9,9,9,9,9]))
