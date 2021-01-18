# 快速排序
from cal_time import *


def partition(li, left, right):
    temp = li[left]  # 保存第一个牌

    while left < right:
        while left < right and li[right] >= temp:  # 从右边找比temp小的数
            """
            right -= 1  在找的过程中，right的指针一直在向前移动
            有一种情况是条件是>=temp，如果right指针一直找都没有找到比temp小的数，
            最终的结果就是找到自己的位置，由于条件是>=所以right的指针还会再向前移动
            最终变成-1程序报错，所以在while中要再加一个条件left<right
            """
            right -= 1
        li[left] = li[right]  # 如果找到了，那把右边的值写到左边的空位上

        while left < right and li[left] <= temp:
            left += 1  # 左侧指针每次都向right前进一位
        li[right] = li[left]  # 把左边的值写到右边空位上

    li[left] = temp  # 最后把拿出去的值写到中间位置，
    # 这里li[left]与li[right]写哪个都一样，因为都是中间位置两具重叠了
    return left  # 返回的是mid的索引位置，使用left或right都一样因为它两重叠了


def _quick_sort(li, left, right):
    if left < right:  # 至少有两个元素
        mid = partition(li, left, right)
        _quick_sort(li, left, mid - 1)  # 从中间到左边的位置
        _quick_sort(li, mid + 1, right)  # 从中间到右边的位置


@cal_time  # 如果把一个装饰器放在递归函数上那这个装饰器也会跟着递归
def quick_sort(li):
    _quick_sort(li, 0, len(li) - 1)


if __name__ == '__main__':
    li = [5, 7, 4, 6, 3, 1, 2, 9, 8]

    #加在哪里，如果加在partition中，那么每一次都会进行交换
    # temp = left  # 保存第一个牌的下标
    # ran_temp = random.randint(0, len(li) - 1)  # 随机找了一个数与第一个数进行交换
    # li[temp], li[ran_temp] = li[ran_temp], li[temp]

    quick_sort(li)
    print(li)
