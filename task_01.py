#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fibonacci sequence  genrator function."""


def fibonacci(maxint):
    """Fibonacci  with  while loop.
    Args:
        maxint (int): it will serve as the upper bound of the loop
    Returns:
        list:  Return the newly generated sequence as a list.

    Examples:
        task_01.fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]

        """
    a, b = 0, 1
    fibo_list = [a]
    while b < maxint:
          fibo_list.append(b)
          a, b = b, a + b 
    return fibo_list  
