#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""if and else statements."""


def bool_to_str(bval):
    """if and else statements.

    Args:
        bval (boolean):  Arg to be evaluated for truthiness or
        falsiness.
    Returns:
        str:  Returns 'Yes' or 'No'

    Examples:
    >>> task_02.bool_to_str(True)
    'Yes'
    >>> task_02.bool_to_str('')
    'No'

    """    
    if bval:
        return_val = 'Yes'
    else:
        return_val = 'No'
    return return_val
