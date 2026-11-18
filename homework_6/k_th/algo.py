from random import randrange


def find_kth_largest(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("k должно быть от 1 до длины массива")

    target = len(nums) - k
    left, right = 0, len(nums) - 1

    while left <= right:
        pivot = nums[randrange(left, right + 1)]
        lower, current, upper = left, left, right

        while current <= upper:
            if nums[current] < pivot:
                nums[lower], nums[current] = nums[current], nums[lower]
                lower += 1
                current += 1
            elif nums[current] > pivot:
                nums[current], nums[upper] = nums[upper], nums[current]
                upper -= 1
            else:
                current += 1

        if target < lower:
            right = lower - 1
        elif target > upper:
            left = upper + 1
        else:
            return nums[target]


if __name__ == "__main__":
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))
    print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
