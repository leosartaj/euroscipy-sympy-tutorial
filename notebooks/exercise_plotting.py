# differentiate the expression
expr_d = expr.diff(x)  # EXERCISE: expr.diff(x)
f2 = lambdify(x, expr_d, modules='numpy')  # EXERCISE: x, expr_d, modules='numpy'
plt.plot(nx, f2(nx));  # EXERCISE: nx, f2(nx)
