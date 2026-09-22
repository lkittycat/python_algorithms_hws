import unittest

from algo import Queue, Stack

class TestStack(unittest.TestCase):
    def test_pop_order(self):
        stack = Stack()
        for value in (10, 20, 30, 40):
            stack.push(value)
        for expected in (40, 30, 20, 10):
            self.assertEqual(stack.pop(), expected)
        self.assertIsNone(stack.head)

    def test_peek_keeps_element(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            Stack().pop()

    def test_peek_empty(self):
        with self.assertRaises(IndexError):
            Stack().peek()

    def test_add_after_empty(self):
        stack = Stack()
        stack.push(10)
        self.assertEqual(stack.pop(), 10)
        self.assertIsNone(stack.head)
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()
        stack.push(20)
        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.pop(), 20)
        self.assertIsNone(stack.head)

    def test_add_and_remove(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        stack.push(3)
        stack.push(4)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.peek(), 3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 1)

    def test_different_values(self):
        stack = Stack()
        values = (None, 0, -5, "hello", 7, 7)
        for value in values:
            stack.push(value)
        for expected in reversed(values):
            with self.subTest(expected=expected):
                self.assertEqual(stack.peek(), expected)
                self.assertEqual(stack.pop(), expected)
        with self.assertRaises(IndexError):
            stack.pop()

    def test_two_stacks(self):
        first = Stack()
        second = Stack()
        first.push(10)
        second.push(20)
        self.assertEqual(first.pop(), 10)
        self.assertEqual(second.peek(), 20)
        self.assertEqual(second.pop(), 20)


class TestQueue(unittest.TestCase):
    def test_dequeue_order(self):
        queue = Queue()
        for value in (1, 2, 3, 4):
            queue.enqueue(value)
        for expected in (1, 2, 3, 4):
            self.assertEqual(queue.dequeue(), expected)
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

    def test_peek_keeps_element(self):
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        self.assertEqual(queue.peek(), 10)
        self.assertEqual(queue.peek(), 10)
        
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 20)

    def test_dequeue_empty(self):
        with self.assertRaises(IndexError):
            Queue().dequeue()

    def test_peek_empty(self):
        with self.assertRaises(IndexError):
            Queue().peek()

    def test_add_after_empty(self):
        queue = Queue()
        queue.enqueue(10)
        self.assertEqual(queue.dequeue(), 10)
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)
        with self.assertRaises(IndexError):
            queue.dequeue()
        with self.assertRaises(IndexError):
            queue.peek()
        queue.enqueue(20)
        self.assertEqual(queue.peek(), 20)
        self.assertEqual(queue.dequeue(), 20)
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

    def test_add_and_remove(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        
        
        queue.enqueue(3)
        queue.enqueue(4)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.peek(), 3)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)

    def test_different_values(self):
        queue = Queue()
        values = (None, 0, -5, "hello", 7, 7)
        for value in values:
            queue.enqueue(value)
            
        for expected in values:
            with self.subTest(expected=expected):
                self.assertEqual(queue.peek(), expected)
                self.assertEqual(queue.dequeue(), expected)
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_two_queues(self):
        first = Queue()
        
        second = Queue()
        first.enqueue(10)
        second.enqueue(20)
        self.assertEqual(first.dequeue(), 10)
        self.assertEqual(second.peek(), 20)
        self.assertEqual(second.dequeue(), 20)


if __name__ == "__main__":
    unittest.main()
