def valid_parentheses(s):
    """
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
    有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。

    示例 1:
    输入: "()"
    输出: true

    示例2:
    输入: "()[]{}"
    输出: true

    示例3:
    输入: "(]"
    输出: false

    示例4:
    输入: "([)]"
    输出: false

    示例5:
    输入: "{[]}"
    输出: true
    """
    dicts = {')': '(', ']': '[', '}': '{'}
    li = []
    for ch in s:
        if ch in {'(', '[', '{'}:
            li.append(ch)
        else:
            if not len(li):
                return False
            elif li[-1] == dicts[ch]:
                li.pop()
            else:
                return False
    return True if len(li) == 0 else False


if __name__ == '__main__':
    print(valid_parentheses('{[]}'))
