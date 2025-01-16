def my_function(x):
    if x == 0:
        return 0
    elif x < 0:
        return 0  # Handle negative input
    else:
        return x + my_function(x - 1)

# Or, using iteration instead of recursion for better performance and to avoid stack overflow
def my_function_iterative(x):
    result = 0
    for i in range(x + 1):
        result += i
    return result