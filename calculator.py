def add(a,b):
    return a + b


def substract(a,b):
    return a - b


def multiply(a,b):
    return a * b


def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    a = 10
    b = 5
    print("Python Calculator")
    print("First Number :",a)
    print("Second Number :",b)
    print("Addition :",add(a,b))
    print("Substraction :",substract(a,b))
    print("Multiplication :",multiply(a,b))
    print("Division :",divide(a,b))

if __name__ == "__main__":
    main()