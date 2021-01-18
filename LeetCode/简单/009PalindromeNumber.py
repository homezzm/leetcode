def palindrome_number(x):
    """
    """
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    if x == 0 or x // 10 == 0: return True

    rn = 0
    while x > rn:
        rn = rn * 10 + x % 10
        x //= 10
    return x == rn or x == rn // 10


if __name__ == '__main__':
    print(palindrome_number(100))
