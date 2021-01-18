from 算法 import heap_sort, insert_sort, quick_sort, binary_search, select_sort, bubble_sort, linear_search
from 算法 import merge_sort,sheel_sort,radix_sort
import random
import copy

def get_li():
    li = list(range(10000))
    random.shuffle(li)  # 把列表打散
    return li

def copy_li(li):# 做个深拷贝
    return copy.deepcopy(li)

if __name__ == '__main__':

    print('查找对比')
    linear_search.linear_search(get_li(), 3890)  # 顺序查找
    binary_search.binary_search(get_li(), 3890)  # 二分查找法

    print('排序对比')
    print('lowB三人组begin...')
    bubble_sort.bubble_sort(get_li())  # 冒泡排序
    insert_sort.insert_sort(get_li())  # 插入排序
    select_sort.select_sort(get_li())  # 选择排序
    print('lowB三人组end...')

    print('NB三人组begin...')
    heap_sort.heap_sort(get_li())   #堆排序
    quick_sort.quick_sort(get_li())  # 快速排序
    merge_sort.merge_sort(get_li()) #归并排序
    print('NB三人组end...')

    sheel_sort.shell_sort(get_li()) #希尔排序
    radix_sort.radix_sort(get_li()) #基数排序