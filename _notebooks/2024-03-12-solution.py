# My solution
def multiply(x,y):
    count = 0
    result = 0
    while count < abs(y):
        result += x
        count += 1 
    if y < 0:
        return -1*result
    return result

print(multiply(2, 5))  # Expected output: 10
print(multiply(2, -5))  # Expected output: -10
print(multiply(-2, 5))  # Expected output: -10
print(multiply(-2, -5)) # Expected output 10