def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # Check if the mid element is larger than the last element
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]
nums = [3,4,5,1,2]
print(findMin(nums))

nums1 = [4,5,6,7,0,1,2]
print(findMin(nums1))

nums2 = [11,13,15,17]
print(findMin(nums2))

