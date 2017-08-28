def fib(n):
    """
    Uses series expansion and a generating function to compute the nth Fibonnicci number.

    >>> fib(0)
    0
    >>> fib(4)
    3
    >>> fib(9)
    34
    """
    gen_func = x/(1 - x - x**2) # generating function
    expansion = gen_func.series(x, 0, n + 1)  # EXERCISE: series(x, 0, n + 1)
    num = expansion.coeff(x, n)  # EXERCISE: coeff(x, n)
    return num
