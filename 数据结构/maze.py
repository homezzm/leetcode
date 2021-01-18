# 迷宫问题 栈解决
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 方向的函数列表
# x,y四个方向 [上=x-1,y]  [下=x+1,y]  [左=x,y-1]  [右=x,y+1]
dirs = [
    lambda x, y: (x + 1, y),  # 下
    lambda x, y: (x - 1, y),  # 上
    lambda x, y: (x, y - 1),  # 左
    lambda x, y: (x, y + 1)  # 右
]


def maze_path(x1, y1, x2, y2):
    # x1,y1表示起点位置
    # x2,y2表示终点位置
    stack = [(x1, y1)]  # 用个列表来简单实现
    # 栈空的话表示没有路，起点坐标都给弹出去了，上哪说理去
    while len(stack) > 0:  # 栈不空的时候才循环
        curr_node = stack[-1]  # 当前的位置，也就是最栈中最后一个坐标，-1倒序
        # 拿到当前节点的时候就要判定下是否已经到达了终点
        if curr_node[0] == x2 and curr_node[1] == y2:
            for p in stack:  # 把路径输出
                print(p)
            return True  # 走通了

        for dir in dirs:
            # dir就是lambda函数 curr_node是坐标元组x=curr_node[0]
            # 通过dir计算出能走的坐标
            next_node = dir(curr_node[0], curr_node[1])
            # 如果下一个节点能走
            if maze[next_node[0]][next_node[1]] == 0:  # 0是路 1是墙
                stack.append(next_node)
                maze[next_node[0]][next_node[1]] = 2  # 2表示已经走过了 在地图中标识下
                # 找到一个能走的点就可以
                break
        else:  # 如果一个都找不到就要回退了
            # 虽然没有路，但走过了就标识成2，防止重复走
            maze[next_node[0]][next_node[1]] = 2
            # 出栈
            stack.pop()
    # 外层的while跳出了，表示没有路可走
    print("没有路！")
    return False


if __name__ == '__main__':
    maze_path(1, 1, 8, 8)
