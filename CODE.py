def calc(op, x, y):
    if op == "add":
        return x + y
    elif op == "subtract":
        return x - y
    elif op == "multiply":
        return x * y
    elif op == "divide":
        if y == 0:
            print("Error: Division by zero")
        else:
            x / y  # Bug: forgot return
    else:
        print("Invalid operation")

# Test cases
print(calc("add", 3, 3))        # Should be 5
print(calc("divide", 11, 0))    # Should show error
print(calc("divide", 1, 2))    # Should be 5.0, but returns None
print(calc("power", 1, 3))      # Invalid op test
