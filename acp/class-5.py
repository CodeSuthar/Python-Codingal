def fibonacci(till):
    a, b = 0, 1
    while a < till:
        print(a, end=' ')
        a, b = b, a + b
    print()

ask = int(input("Enter a number: "))

fibonacci(ask)