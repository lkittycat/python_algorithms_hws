def two_sum(arr, k):
    seen = {}

    for i, value in enumerate(arr):
        needed = k - value
        if needed in seen:
            return seen[needed], i
        seen[value] = i

    raise ValueError("pair not found :(")
