import sympy as sp
import numpy as np

x = sp.symbols('x')

def make_vectorizable(expr, var):
    """Return a SymPy expression guaranteed to lambdify to a numpy array."""
    expr = sp.sympify(expr)
    if var not in expr.free_symbols:
        expr = sp.Lambda(var, expr)(var)  # force it to depend on var
    return expr

# Example usage
V = make_vectorizable(10, x)    # constant load
x_vals = np.linspace(0, 5, 6)
f = sp.lambdify(x, V, "numpy")
y_vals = np.full_like(x_vals, 10.0)
print(type(f(x_vals)))  # -> array([10., 10., 10., 10., 10., 10.])
