def add_numbers(a, b, c):
    """Adds two numbers and multiplies the result by a third number."""
    #?lesson 1
    return (a + b) * c
def check_positive(a):
    """Checks if a number is positive."""
    #?lesson 2
    return a > 0
def print_hello_world(n):
    """Prints 'hello world' n times."""
    #?lesson 3
    for i in range(n):
        print("hello world")
def cube_root(n):
    """Calculates the cube root of a number."""
    #?lesson 4
    cube = n ** (1/3)
    if cube % 1 == 0:
        return int(cube)
    else:
        return "Error"
def even_index(str=''):
    """Returns characters at even indices of a string."""
    #?lesson 5
    return str[::2]

import random
def bisection_search(n=0):
    lst = [random.randint(0, 100) for _ in range(1000)]
    halfway: int = len(lst) // 2
    high = len(lst)
    low = 0

    if n == halfway:
        return halfway

    while n > low:
        low = halfway
        for _ in lst[low:halfway]:
            if n == _:
                return _
            break
        for _ in lst[halfway:high]:
            if n == _:
                return _

    
def main():
    a = input("Enter a number: ")
    b = input("Enter another number: ")
    c = input("Enter a third number: ")
    total = add_numbers(int(a), int(b), int(c))
    print(f"The total is: {total}")

    if check_positive(total):
        print("The total is positive.")
    elif total == 0:
        print("The total is Zero.")
    else:
        print("The total is negative.")

    n = int(input("How many times to print 'hello world'? "))
    print_hello_world(n)

    root = cube_root(n=n)
    print(f"The cube root of {n} is: {root}")

    string = input("Enter a string: ")
    even_chars = even_index(string)
    print(f"Characters at even indices: {even_chars}")

    n = int(input("search for a number"))
    ans = bisection_search(n)
    print(ans)
if __name__ == "__main__":
    main()