def evaluate(exprs, x, x0):
    """
    Differentiate each expression in exprs  and evaluate at the point x = x0.

    >>> x, y = symbols('x y')
    >>> exprs = [x**2, cos(x), x*y]
    >>> evaluate(exprs, x, 1)
    [2, -sin(1), y]
    >>> evaluate(exprs, y, 0)
    [0, 0, x]
    """
    ans = [expr.diff(x).subs({x: x0}) for expr in exprs]  # EXERCISE: [expr.diff(x).subs({x: x0}) for expr in exprs]
    return ans
