def operation(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError("Division by zero")
    else:
        raise ValueError("Invalid operator")

def calculator(l):
    i = 0
    while i < len(l):
        if l[i] in ('*', '/'):
            left = float(l[i-1])
            right = float(l[i+1])
            result = operation(left, right, l[i])
            l[i-1:i+2] = [result]
            i -= 1
        else:
            i += 1
    
    result = float(l[0])
    i = 1
    while i < len(l):
        op = l[i]
        num = float(l[i+1])
        result = operation(result, num, op)
        i += 2
    
    return result

a = input()
l = a.split()
print("Result:", calculator(l))
