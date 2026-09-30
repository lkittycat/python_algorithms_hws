import unittest

from algo import HashTable


class TestHashTable(unittest.TestCase):
    def test_insert_and_search(self):
        table = HashTable()
        table.insert("name", "Anna")
        table.insert("age", 20)
        self.assertEqual(table.search("name"), "Anna")
        self.assertEqual(table.search("age"), 20)
        self.assertEqual(table.size, 2)

    def test_update(self):
        table = HashTable()
        table.insert("name", "Anna")
        table.insert("name", "Masha")
        self.assertEqual(table.search("name"), "Masha")
        self.assertEqual(table.size, 1)

    def test_search_empty(self):
        table = HashTable()
        with self.assertRaises(KeyError):
            table.search("missing")

    def test_delete_empty(self):
        table = HashTable()
        with self.assertRaises(KeyError):
            table.delete("missing")
        self.assertEqual(table.size, 0)

    def test_delete(self):
        table = HashTable()
        table.insert("a", 1)
        table.insert("b", 2)
        table.delete("a")
        with self.assertRaises(KeyError):
            table.search("a")
        self.assertEqual(table.search("b"), 2)
        self.assertEqual(table.size, 1)

    def test_collisions(self):
        table = HashTable(8)
        # У целых 0, 8 и 16 одинаковый остаток от деления хеша на 8.
        table.insert(0, "first")
        table.insert(8, "second")
        table.insert(16, "third")
        self.assertEqual(len(table.buckets[0]), 3)
        table.insert(8, "updated")
        self.assertEqual(table.size, 3)
        self.assertEqual(table.search(8), "updated")
        table.delete(8)
        self.assertEqual(table.search(0), "first")
        self.assertEqual(table.search(16), "third")
        with self.assertRaises(KeyError):
            table.search(8)
        with self.assertRaises(KeyError):
            table.delete(24)
        self.assertEqual(table.size, 2)
        table.delete(0)
        table.delete(16)
        self.assertEqual(table.size, 0)

    def test_resize(self):
        table = HashTable(4)
        for i in range(3):
            table.insert(i, i * 10)
        self.assertEqual(table.capacity, 4)
        table.insert(0, 100)
        self.assertEqual(table.capacity, 4)
        table.insert(3, 30)
        self.assertEqual(table.capacity, 8)
        self.assertEqual(table.size, 4)
        self.assertEqual(table.search(0), 100)
        for i in range(1, 4):
            self.assertEqual(table.search(i), i * 10)

    def test_collisions_after_resize(self):
        table = HashTable(4)
        for i in range(4):
            table.insert(i * 4, i)
        self.assertEqual(table.capacity, 8)
        for i in range(4):
            self.assertEqual(table.search(i * 4), i)
        table.delete(4)
        table.insert(12, 100)
        self.assertEqual(table.search(12), 100)
        self.assertEqual(table.size, 3)

    def test_add_after_empty(self):
        table = HashTable()
        table.insert("a", 1)
        table.delete("a")
        table.insert("a", 2)
        self.assertEqual(table.search("a"), 2)
        self.assertEqual(table.size, 1)

    def test_different_values(self):
        table = HashTable()
        table.insert("empty", None)
        table.insert("zero", 0)
        table.insert("list", [1, 2])
        self.assertIsNone(table.search("empty"))
        self.assertEqual(table.search("zero"), 0)
        self.assertEqual(table.search("list"), [1, 2])

    def test_different_keys(self):
        table = HashTable()
        table.insert(-5, "negative")
        table.insert(0, "zero")
        table.insert("", "empty string")
        table.insert(None, "none")
        table.insert("ключ", "value")
        self.assertEqual(table.search(-5), "negative")
        self.assertEqual(table.search(0), "zero")
        self.assertEqual(table.search(""), "empty string")
        self.assertEqual(table.search(None), "none")
        self.assertEqual(table.search("ключ"), "value")

    def test_list_cannot_be_key(self):
        table = HashTable()
        with self.assertRaises(TypeError):
            table.insert([1, 2], "value")
        self.assertEqual(table.size, 0)

    def test_small_capacity(self):
        table = HashTable(1)
        table.insert("a", 1)
        table.insert("b", 2)
        self.assertEqual(table.search("a"), 1)
        self.assertEqual(table.search("b"), 2)

    def test_wrong_capacity(self):
        with self.assertRaises(ValueError):
            HashTable(0)
        with self.assertRaises(ValueError):
            HashTable(-1)

    def test_two_tables(self):
        first = HashTable()
        second = HashTable()
        first.insert("a", 1)
        second.insert("a", 2)
        first.delete("a")
        self.assertEqual(second.search("a"), 2)

    def test_many_elements(self):
        table = HashTable()
        for i in range(1000):
            table.insert(i, i * 2)
        self.assertEqual(table.size, 1000)
        for i in range(1000):
            self.assertEqual(table.search(i), i * 2)
        for i in range(0, 1000, 2):
            table.delete(i)
        self.assertEqual(table.size, 500)
        for i in range(1, 1000, 2):
            self.assertEqual(table.search(i), i * 2)

    def test_storage_is_lists(self):
        table = HashTable()
        for i in range(20):
            table.insert(i, i)
        self.assertIsInstance(table.buckets, list)
        for bucket in table.buckets:
            self.assertIsInstance(bucket, list)
            for pair in bucket:
                self.assertIsInstance(pair, list)
                self.assertEqual(len(pair), 2)


if __name__ == "__main__":
    unittest.main()
