from algo import is_palindrome


def test():
    # однознач числа
    assert is_palindrome(1)
    assert is_palindrome(5)
    assert is_palindrome(9)

    # нечет кол-во цифр
    assert is_palindrome(121)
    assert is_palindrome(12321)
    assert is_palindrome(1234321)

    # чет коли-во цифр
    assert is_palindrome(11)
    assert is_palindrome(1221)
    assert is_palindrome(123321)

    # нули внутри
    assert is_palindrome(101)
    assert is_palindrome(1001)
    assert is_palindrome(10001)

    # не палиндромы
    assert not is_palindrome(12)
    assert not is_palindrome(31)
    assert not is_palindrome(123)
    assert not is_palindrome(12345)

    # нули в конце
    assert not is_palindrome(10)
    assert not is_palindrome(100)
    assert not is_palindrome(1010)

    # большие числа
    assert is_palindrome(12345678987654321)
    assert not is_palindrome(12345678987654320)

    # неположительные числа
    assert not is_palindrome(0)
    assert not is_palindrome(-1)
    assert not is_palindrome(-121)