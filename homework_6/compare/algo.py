from functools import wraps
from random import Random
from time import perf_counter


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f"{func.__name__}: {elapsed:.6f} сек.")
        return result

    return wrapper


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def mergesort(nums):
    if len(nums) < 2:
        return nums.copy()
    middle = len(nums) // 2
    left = mergesort(nums[:middle])
    right = mergesort(nums[middle:])
    return merge(left, right)


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

    def sort(left, right):
        while left < right:
            middle = partition(result, left, right)
            if middle - left < right - middle:
                sort(left, middle - 1)
                left = middle + 1
            else:
                sort(middle + 1, right)
                right = middle - 1

    sort(0, len(result) - 1)
    return result


if __name__ == "__main__":
    random = Random(42)
    size = 3000
    cases = {
        "случайный": [random.randrange(size) for _ in range(size)],
        "возрастающий": list(range(size)),
        "убывающий": list(range(size, 0, -1)),
        "одинаковые числа": [7] * size,
    }
    timed_merge = timer(mergesort)
    timed_quick = timer(quicksort)
    for name, nums in cases.items():
        print(f"\n{name}, n = {len(nums)}")
        expected = sorted(nums)
        for _ in range(3):
            assert timed_merge(nums) == expected
            assert timed_quick(nums) == expected
