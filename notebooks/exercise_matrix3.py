def matrix3():
    """
    >>> matrix3()
    [-1, -1, -1, 0, 0, 0]
    [-1, -1, -1, 0, 0, 0]
    [-1, -1, -1, 0, 0, 0]
    [ 0,  0,  0, 0, 0, 0]
    [ 0,  0,  0, 0, 0, 0]
    [ 0,  0,  0, 0, 0, 0]
    """
    return diag(-ones(3, 3), zeros(3, 3))  # EXERCISE: diag(-ones(3, 3), zeros(3, 3))
matrix3()
