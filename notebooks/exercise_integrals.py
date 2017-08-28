def average_value(expr, x, a, b):
    """
    Computes the average value of expr with respect to x on [a, b].

    >>> average_value(sin(x), x, 0, pi)
    2/pi
    >>> average_value(x, x, 2, 4)
    3
    >>> average_value(x*y, x, 2, 4)
    3*y
    """
    ans = integrate(expr, (x, a, b)) / (b - a)  # EXERCISE: integrate(expr, (x, a, b)) / (b - a)
    return ans
