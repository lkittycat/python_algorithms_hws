if __package__ in (None, ""):
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from homework_5.tracer.algo import tracer


def permutations(nums):
    result = []
    path = []
    used = [False] * len(nums)

    @tracer
    def backtrack(current):
        if len(current) == len(nums):
            result.append(current.copy())
            return current.copy()

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            current.append(nums[i])
            backtrack(current)
            current.pop()
            used[i] = False

        return None

    backtrack(path)
    return result


if __name__ == "__main__":
    print(permutations([1, 2, 3]))
