import random


def binary_search(li, val):  # 二分查找，必须是有序的
    left,right=0,len(li)-1
    while left<=right:
        mid= left+(right-left)//2
        if li[mid]==val:
            return mid
        elif li[mid]>val:
            right=mid-1
        else:
            left=mid+1
    return None


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))


def bubble_sort(li):  # 冒泡排序
    pass


def select_sort(li):  # 选择排序
    pass


def insert_sort(li):  # 插入排序
    pass


def partition(li, left, right):
    pass


def quick_sort(li, left, right):  # 快速排序
    pass


# li = [random.randint(0, 100000) for i in range(10000)]
# random.shuffle(li)
# print(li)
# quick_sort(li, 0, len(li) - 1);
# print(li)


def sift(li, low, high):
    pass


def heap_sort(li):
    pass


def merge(li, low, mid, high):  # 规并排序
    pass


def merge_sort(li, low, high):
    pass


# li = list(range(10000))
# random.shuffle(li)
# print(li)
# merge_sort(li, 0, len(li) - 1)
# print(li)

if __name__ == '__main__':
    pass
    # li = list(range(10000))
    # random.shuffle(li)
    # print(li)
    # merge_sort(li, 0, len(li) - 1)
    # print(li)

# li = [random.randint(0, 100000) for i in range(10000)]
# random.shuffle(li)
# print(li)
# heap_sort(li)
# print(li)

# li = [random.randint(0, 100000) for i in range(10000)]
# random.shuffle(li)
# print(li)
# quick_sort(li, 0, len(li) - 1);
# print(li)

# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 81))

# li = [random.randint(0, 100) for i in range(10)]
# print(li)
# random.shuffle(li)
# bubble_sort(li)
# print(li)

# li = [random.randint(0, 100) for i in range(10)]
# random.shuffle(li)
# print(li)
# select_sort(li)
# print(li)

# li = [random.randint(0, 100) for i in range(10)]
# random.shuffle(li)
# print(li)
# inesrt_sort(li)
# print(li)
