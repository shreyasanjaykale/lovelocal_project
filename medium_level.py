def majority_elements(nums):
    if not nums:
        return []

    n = len(nums)
    threshold = n // 3

    count = {}
    result = set()

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

        if count[num] > threshold:
            result.add(num)

    return list(result)

# Examples
nums1 = [3, 2, 3]
result1 = majority_elements(nums1)
print(result1)

nums2 = [1]
result2 = majority_elements(nums2)
print(result2)

nums3 = [1, 2]
result3 = majority_elements(nums3)
print(result3)
