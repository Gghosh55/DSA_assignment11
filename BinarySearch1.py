def sqrt(x):
    if x == 0:
        return 0

    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == x:
            return mid

        if mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right
print(sqrt(4))
print(sqrt(8))
print(sqrt(9))
print(sqrt(16))
print(sqrt(17))
