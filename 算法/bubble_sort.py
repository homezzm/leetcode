# 冒泡排序
from cal_time import *


# 冒泡排序可以改进的地方，如果在一趟过程中没有发生排序，
# 我们就认识列表中已经排好序了，后面就可以不用排序了。
# 增加exchange标识符
@cal_time
def bubble_sort(li):
    n = len(li)
    for i in range(n - 1):  # 冒泡排序共会排n-1趟
        exchange = False
        for j in range(n - i - 1):  # 无序范围=n-i-1（n=长度，i=第几趟）[那个箭头]
            if li[j] > li[j + 1]:  # 可以控制是升序还是降序
                li[j], li[j + 1] = li[j + 1], li[j]  # 交换
                exchange = True
        if not exchange:
            return


if __name__ == '__main__':
    li = [9, 8, 7, 1, 2, 3, 4, 5, 6]
    print("改进后")
    print(li, "原列表")
    bubble_sort(li)
