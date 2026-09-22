import unittest

from algo import Node, method1, method2


def make_list(values):
    head = None
    for value in reversed(values):
        node = Node(value)
        node.next = head
        head = node
    return head


class TestMerge(unittest.TestCase):
    def get_nodes(self, head):
        nodes = []
        seen = set()
        while head is not None:
            self.assertNotIn(id(head), seen, "В результате появился цикл")
            seen.add(id(head))
            nodes.append(head)
            head = head.next
        return nodes

    def check_merge(self, first, second, expected):
        for merge in (method1, method2):
            with self.subTest(method=merge.__name__):
                # Для каждого способа создаём списки заново: слияние меняет связи.
                list1 = make_list(first)
                list2 = make_list(second)
                original = self.get_nodes(list1) + self.get_nodes(list2)
                result = self.get_nodes(merge(list1, list2))

                self.assertEqual([node.value for node in result], expected)
                # Проверяем сами объекты, чтобы копирование значений не прошло тест.
                self.assertCountEqual(
                    [id(node) for node in result],
                    [id(node) for node in original],
                )

    def test_example(self):
        self.check_merge([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])

    def test_both_empty(self):
        self.check_merge([], [], [])

    def test_first_empty(self):
        self.check_merge([], [1, 2, 3], [1, 2, 3])

    def test_second_empty(self):
        self.check_merge([1, 2, 3], [], [1, 2, 3])

    def test_one_node_each(self):
        self.check_merge([1], [2], [1, 2])
        self.check_merge([2], [1], [1, 2])
        self.check_merge([1], [1], [1, 1])

    def test_first_list_smaller(self):
        self.check_merge([1, 2], [3, 4, 5], [1, 2, 3, 4, 5])

    def test_second_list_smaller(self):
        self.check_merge([3, 4, 5], [1, 2], [1, 2, 3, 4, 5])

    def test_alternating_numbers(self):
        self.check_merge([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6])

    def test_same_numbers(self):
        self.check_merge([2, 2, 2], [2, 2], [2, 2, 2, 2, 2])

    def test_negative_numbers_and_zero(self):
        self.check_merge([-5, -1, 0], [-4, 0, 3], [-5, -4, -1, 0, 0, 3])

    def test_different_lengths(self):
        self.check_merge([3], [1, 2, 4, 5, 6], [1, 2, 3, 4, 5, 6])
        self.check_merge([1, 2, 4, 5, 6], [3], [1, 2, 3, 4, 5, 6])

    def test_many_nodes(self):
        self.check_merge(
            list(range(0, 10_000, 2)),
            list(range(1, 10_000, 2)),
            list(range(10_000)),
        )


if __name__ == "__main__":
    unittest.main()
