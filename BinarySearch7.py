def searchRange(nums, target):
    left = findLeftPosition(nums, target)
    right = findRightPosition(nums, target)

    return [left, right]


def findLeftPosition(nums, target):
    left = 0
    right = len(nums) - 1
    position = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

        if nums[mid] == target:
            position = mid

    return position


def findRightPosition(nums, target):
    left = 0
    right = len(nums) - 1
    position = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

        if nums[mid] == target:
            position = mid

    return position
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))

nums1 = [5,7,7,8,8,10]
target1 = 6
print(searchRange(nums1, target1))

nums2 = []
target2 = 8
print(searchRange(nums2, target2))


