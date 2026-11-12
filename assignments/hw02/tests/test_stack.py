import unittest

from src.stack import Stack


class StackTests(unittest.TestCase):
    def test_items_pop_in_reverse_order(self):
        stack = Stack()
        stack.push("A")
        stack.push("B")
        self.assertEqual(stack.pop(), "B")
        self.assertEqual(stack.pop(), "A")

    def test_pop_from_empty_stack_raises_index_error(self):
        with self.assertRaises(IndexError):
            Stack().pop()
