class Solution(object):
    def restoreIpAddresses(self, s):
        """
        https://leetcode-cn.com/problems/restore-ip-addresses/
        :type s: str
        :rtype: List[str]
        给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
        有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
        例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。
        """

        res, n = [], len(s)
        if n < 4 or n > 12: return res

        def backtrack(startInx, paths):  # pointNum是记录的“.”数量
            if len(paths) == 4:
                ip = '.'.join(paths)
                if len(ip) == len(s) + 3:
                    res.append(ip)
                return

            for i in range(startInx, len(s)):
                first = s[startInx:i + 1]
                last = s[i + 1:]
                if len(last) > 9: continue  # 剩余部分太多，直接剪枝 比如25525511135，取2之后剩余10个数，而IP的后三位最多只能是9个数

                if not self.isValidate(first): continue
                paths.append(first)
                backtrack(i + 1, paths)
                paths.pop()

        backtrack(0, [])
        return res

    def isValidate(self, s):
        if len(s) > 1 and s[0] == '0':  # 不能含有前导 0
            return False
        if int(s) > 255:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.restoreIpAddresses('01011'))
    # ss = ['11', '22', '33']
    # print('.'.join(ss))
