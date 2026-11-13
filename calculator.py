def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b  # возможное деление на ноль

def main():
    c = 2
    d = 3
    print(add(c, d))
    print(sub(5, 2))
    print(mul(4, 3))
    print(div(10, 0))  # деление на ноль
    unused = 10  # неиспользуемая переменная

if __name__ == "__main__":
    main()
