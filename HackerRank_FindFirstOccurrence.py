def findFirstOccurrence(nums, target):
    low, high = 0, len(nums) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            result = mid          # record the index
            high = mid - 1        # continue searching left
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1


    return result

