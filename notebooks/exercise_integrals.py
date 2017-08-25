mu, sigma = symbols('mu, sigma')
int_sin = integrate(sin(x), x)  # EXERCISE: sin(x), x
int_sin_def = integrate(sin(x), (x, 0, pi))  # EXERCISE: sin(x), (x, 0, pi)
int_poly = integrate(x**5 + 12*x**3 - 2*x + 1, (x, 0, y))  # EXERCISE: x**5 + 12*x**3 - 2*x + 1, (x, 0, y)
int_bell = integrate(exp(-(x - mu)**2) / (2*sigma)**2, x)  # EXERCISE: exp(-(x - mu)**2) / (2*sigma)**2, x
int_sin, int_sin_def, int_poly, int_bell
