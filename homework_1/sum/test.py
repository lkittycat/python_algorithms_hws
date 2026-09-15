from algo import max_even_sum


def test_max_even_sum():
    #с задания
    assert max_even_sum([5, 7, 13, 2, 14]) == 36

    # один нечет элемент
    assert max_even_sum([3]) == 0

    # один чет элемент
    assert max_even_sum([8]) == 8

    # все числа чет
    assert max_even_sum([2, 4, 6, 8]) == 20

    # чет
    assert max_even_sum([1, 3, 2]) == 6
    assert max_even_sum([5, 7]) == 12

    # нечет
    assert max_even_sum([1, 2, 4]) == 6
    assert max_even_sum([9, 3, 2]) == 12
    assert max_even_sum([7, 5, 3, 2]) == 14

    # неск одинаковых нечет
    assert max_even_sum([1, 1, 1]) == 2
