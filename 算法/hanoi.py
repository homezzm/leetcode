# hanoi即是汉诺塔的英文
def hanoi(n, a, b, c):  # 其实这就是题目(把n个盘子从A经过B移动到C)
    """
    :param n: N个盘子
    :param a:a盘子的名字
    :param b:b盘子的名字
    :param c:c盘子的名字
    :return:
    """
    if n > 0:  # 递归终止条件
        hanoi(n - 1, a, c, b)  # 1.把n-1个盘子从A经过C移动到B
        print('moving from %s to %s' % (a, c))  # 2.把第n个圆盘从A移动到C
        hanoi(n - 1, b, a, c)  # 3.把n-1个盘子从B经过A移动到C


if __name__ == '__main__':
    hanoi(3, 'A', 'B', 'C')
