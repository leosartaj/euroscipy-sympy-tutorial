def find_999999(expr, limit=100000):
    """
    Find the first place in the decimal expr where 999999 appears.

    Only checks up to limit digits.

    Returns False when 999999 does not appear.

    >>> find_999999(pi)
    762
    >>> find_999999(E)
    False
    >>> find_999999(E, 1000000) # This one will take a few seconds to compute
    384340
    """
    # index where 999999 appears
    found = str(expr.evalf(limit)).split('.', 2)[1].find('999999') + 1  # EXERCISE: str(expr.evalf(limit)).split('.', 2)[1].find('999999') + 1
    if found == 0:  # EXERCISE: 0
        return False
    return found
