# Homework 2 — Data Structures

## Task

Complete the `Stack` class in [src/stack.py](src/stack.py). A stack stores items in last-in, first-out order. For example, if you push A and then B, popping returns B first and A second.

- `push(item)` adds an item to the top of the stack.
- `pop()` removes and returns the top item. If the stack is empty, raise `IndexError`.

## Files

Edit [src/stack.py](src/stack.py). The provided [tests/test_stack.py](tests/test_stack.py) checks that items come out in reverse order and that popping an empty stack raises the required error.

## Run the tests

Open a terminal in this homework folder, `assignments/hw02`. With Python 3 installed, run `python3 -m unittest discover -s tests -v`.

On Windows, use `py -3` in place of `python3` if needed. The tests will fail until you implement the starter methods. This practice assignment ends when both tests pass.
