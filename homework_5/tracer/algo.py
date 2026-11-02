from functools import wraps


def tracer(func):
    depth = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal depth
        indent = "    " * depth
        arguments = [repr(value) for value in args]
        arguments.extend(f"{key}={value!r}" for key, value in kwargs.items())
        print(f"{indent}-> {func.__name__}({', '.join(arguments)})")
        depth += 1

        try:
            result = func(*args, **kwargs)
        except BaseException as error:
            print(f"{indent}<- {func.__name__} raises {type(error).__name__}: {error}")
            raise
        else:
            print(f"{indent}<- {func.__name__} = {result!r}")
            return result
        finally:
            depth -= 1

    return wrapper


if __name__ == "__main__":
    @tracer
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    factorial(3)
