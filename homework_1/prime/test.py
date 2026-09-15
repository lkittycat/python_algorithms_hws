from algo import count_primes


def test_count_primes():
    # нет простых
    assert count_primes(0) == 0
    assert count_primes(1) == 0
    assert count_primes(2) == 0

    assert count_primes(3) == 1
    assert count_primes(4) == 2
    assert count_primes(5) == 2

    #из задания
    assert count_primes(10) == 4


    assert count_primes(11) == 4
    assert count_primes(12) == 5
    assert count_primes(20) == 8
    assert count_primes(100) == 25