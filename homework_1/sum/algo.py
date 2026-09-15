def max_even_sum(nums):
    total = 0
    min_odd = None

    for num in nums:
        total += num

        if num % 2 != 0:
            if min_odd is None or num < min_odd:
                min_odd = num

    if total % 2 == 0:
        return total

    return total - min_odd