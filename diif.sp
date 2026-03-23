import sympy as sp

def differentiation_calculator(function_str, variable='x'):
    x = sp.symbols(variable)
    f = sp.sympify(function_str)
    df = sp.diff(f, x)
    return df

func = input("Enter a function in terms of x: ")
derivative = differentiation_calculator(func)
print("Function:", func)
print("Derivative:", derivative)
