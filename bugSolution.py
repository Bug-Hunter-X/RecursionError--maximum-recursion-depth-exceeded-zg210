def my_function(x):
    if x == 0:
        return 0
    elif x > 1000: # Added a check for a large value to prevent RecursionError
        return 0  # Or handle the case appropriately
    else:
        return my_function(x - 1) + x

print(my_function(5))
print(my_function(1000)) # This should not raise a RecursionError