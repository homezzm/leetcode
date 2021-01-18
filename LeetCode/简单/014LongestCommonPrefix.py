def longest_common_prefix(strs):
    """
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串""。
    示例1:
    输入: ["flower","flow","flight"]
    输出: "fl"

    示例2:
    输入: ["dog","racecar","car"]
    输出: ""
    解释: 输入不存在公共前缀。
    说明:所有输入只包含小写字母a-z。
    """
    if not strs or len(strs) == 0: return ""

    min_len = len(min(strs, key=len))
    common_str = ""
    dicts = {}
    for col in range(0, min_len):
        for ch in strs:
            dicts[ch[col]] = ch[col]
        if len(dicts) == 1:
            common_str += [elem for elem in dicts.values()][0]
            dicts.clear()
    return common_str


if __name__ == '__main__':
    print(longest_common_prefix(['abcc','abcd','abef','abo']))
