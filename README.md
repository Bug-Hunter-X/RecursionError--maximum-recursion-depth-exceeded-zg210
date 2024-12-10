# RecursionError in Python

This repository demonstrates a common error in recursive Python functions: exceeding the maximum recursion depth.  The `bug.py` file contains a recursive function that lacks proper handling for very large input values, leading to a `RecursionError`. The `bugSolution.py` file provides a corrected implementation that avoids this error.

## How to Reproduce

1. Clone this repository.
2. Run `bug.py` using a Python interpreter.
3. Observe the `RecursionError` when the input is large (for example,  my_function(1000)).
4. Run `bugSolution.py` to see the corrected implementation. 

## Solution

The solution involves adding a check for very large values to prevent unnecessary recursion, using iterative approach or tail recursion optimisation (if possible).