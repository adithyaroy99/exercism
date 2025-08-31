def square(number):
    if not 1<= number <=64:
        # when the square value is not in the acceptable range
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number-1)

def total():
    return sum(2**(i-1) for i in range(1,65))
