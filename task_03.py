#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Practicing for loops."""


import decimal

def lexicographics(to_analyze):
    """A simple for-loop to loop.


    Args:
        to_analyze (str):  A required string.
    Returns:
        Tuple:  Returns a tuple with maximum, minimum and average words
        per line

    Example:
    >>> task_03.lexicographics('''Don't stop believing,
    Hold on to that feeling.''')
   (5, 3, Decimal(4.0))

   """    
    lines = to_analyze.splitlines()
    myvar = []
    mytuple = ()
    for words in lines:
        myvar.append(len(words.split()))
    mytuple = (max(myvar), min(myvar), decimal.Decimal(sum(myvar))/len(lines))
    return mytuple
