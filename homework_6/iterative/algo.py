def mergesort(nums):
    result = nums.copy()
    size = len(result)
    buffer = [None] * size
    width = 1

    while width < size:
        for left in range(0, size, 2 * width):
            middle = min(left + width, size)
            right = min(left + 2 * width, size)
            i, j = left, middle
            for k in range(left, right):
                if i < middle and (j >= right or result[i] <= result[j]):
                    buffer[k] = result[i]
                    i += 1
                else:
                    buffer[k] = result[j]
                    j += 1
        result, buffer = buffer, result
        width *= 2

    return result


def partition(nums, left, right):
    pivot = nums[right]
    i = left
    for j in range(left, right):
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i


def quicksort(nums):
    result = nums.copy()
    stack = [(0, len(result) - 1)]

    while stack:
        left, right = stack.pop()
        while left < right:
            middle = partition(result, left, right)
            if middle - left < right - middle:
                if middle + 1 < right:
                    stack.append((middle + 1, right))
                right = middle - 1
            else:
                if left < middle - 1:
                    stack.append((left, middle - 1))
                left = middle + 1

    return result


if __name__ == "__main__":
    nums = [5, 2, 8, 1, 3]
    print(mergesort(nums))
    print(quicksort(nums))
