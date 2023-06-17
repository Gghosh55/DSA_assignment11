from collections import Counter


def intersect(nums1, nums2):
    counter1 = Counter(nums1)
    counter2 = Counter(nums2)
    result = []

    for num, freq in counter1.items():
        if num in counter2:
            common_freq = min(freq, counter2[num])
            result.extend([num] * common_freq)

    return result
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))

nums3 = [4,9,5]
nums4 = [9,4,9,8,4]
print(intersect(nums3, nums4))