
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
def bisection_search(n=0):
    """Performs a bisection(spits array in half using a double pointer......(high + low)//2 ) search to find a number."""
    #?lesson 6
    high = 1001
    low = 0
    middle = (high+low)//2
    guess = 1
    if n == middle:
        return middle, guess
    while n != middle:
        if n > middle:
            low = middle
        elif n < middle:
            high = middle
        middle = (high+low)//2
        guess += 1
    return middle, guess
def eval_quadratic(a=0, b=0, c=0, x=0):
    """
    #? Lesson 7
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    Returns the value of the quadratic a×x² + b×x + c.
    """
    return (a * x ** 2) + (b * x) + c
def two_quadratics(*args):
#? Lesson 7 - part 2
    coe = list(args)
    if len(args) < 3:
        return "try with 3 arguments"
    else:
        print(eval_quadratic(coe[0], coe[1], coe[2], coe[3]) + eval_quadratic(coe[-4], coe[-3], coe[-2], coe[-1]))
def same_chars(s1, s2):
#?lesson 8
    """
    s1 and s2 are strings
    Returns boolean True is a character in s1 is also in s2, and vice 
    versa. If a character only exists in one of s1 or s2, returns False.
    """
    lst1 = set(s1)
    lst2 = set(s2)
    return lst1.issubset(lst2) and lst1.issuperset(lst2)
def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    get_len = len(tA)
    i = 0
    summ = 0
    while i < get_len:
        prod = tA[i] * tB[i]
        summ += prod
        i += 1
    return (get_len, summ)
#? Lesson 11
def remove_and_sort(Lin=[], k=0):
    """ Lin is a list of ints
        k is an int >= 0
    Mutates Lin to remove the first k elements in Lin and 
    then sorts the remaining elements in ascending order.
    If you run out of items to remove, Lin is mutated to an empty list.
    Does not return anything.
    """
    print(Lin)
    i = 0
    curr = Lin[i]
    nxt = Lin[i+1]
    if len(Lin) < k:
        return []
    for _ in range(len(Lin[:k])):
        Lin.pop(i)
    if Lin[i+1] is None:
        return Lin
    while curr > nxt:
        Lin.pop(0)
        Lin.append(curr)
        return Lin


def main():
##? Lesson 1
#    a = input("Enter a number: ")
#    b = input("Enter another number: ")
#    c = input("Enter a third number: ")
#    total = add_numbers(int(a), int(b), int(c))
#    print(f"The total is: {total}")
#
##? Lesson 2
#    if check_positive(total):
#        print("The total is positive.")
#    elif total == 0:
#        print("The total is Zero.")
#    else:
#        print("The total is negative.")
#
##? Lesson 3
#    n = int(input("How many times to print 'hello world'? "))
#    print_hello_world(n)
#
##? Lesson 4
#    root = cube_root(n=n)
#    print(f"The cube root of {n} is: {root}")
#
##? Lesson 5
#    string = input("Enter a string: ")
#    even_chars = even_index(string)
#    print(f"Characters at even indices: {even_chars}")
#
##? Lesson 6
#    n = int(input("search for a number: "))
#    ans, guess = bisection_search(n)
#    print(f"Answer: {ans},\n Guess: {guess}")    
#
##? Lesson 7
#    a = int(input("Enter coefficient 1: "))
#    b = int(input("Enter coefficient 2: "))
#    c = int(input("Enter coefficient 3: "))
#    x = int(input("Enter X variable: "))
#    ans = eval_quadratic(a,b,c,x)
#    print(ans)
##? Lesson 7 - part 2
#    two_quadratics(1, 1, 1, 2, 1, 1, 1, 2)
#
#? Lesson 8
#    print(same_chars("abc", "cab"))     # prints True
#    print(same_chars("abccc", "caaab")) # prints True
#    print(same_chars("abcd", "cabaa"))  # prints False
#    print(same_chars("abcabc", "cabz")) # prints False
#
#? Lesson 9
#    tA = (1, 3, 3)
#    tB = (4, 5, 6)  
#    print(dot_product(tA, tB))     #*prints (3,32)
#? Lesson 11
    L = [1,6,3,2,4,5,2,34]
    k = 3
    remove_and_sort(L, k)
    print(L)   #* prints the list [3, 6]
    print(L[1])
if __name__ == "__main__":
    main() 