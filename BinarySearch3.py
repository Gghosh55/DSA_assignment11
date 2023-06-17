def missingNumber(nums):
    n = len(nums)
    missing = n

    for i in range(n):
        missing ^= i ^ nums[i]

    return missing
nums = [3, 0, 1]
nums1 = [0,1]
nums2 = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))
print(missingNumber(nums1))
print(missingNumber(nums2))
