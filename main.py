def main():
    a = input("Enter a number: ")
    b = input("Enter another number: ")
    c = input("Enter a third number: ")
    total = (int(a) + int(b)) * int(c)
    print(f"The total is: {total}")
    if total > 0:
        print("The total is positive.")
    elif total < 0:
        print("The total is negative.")
    else:
        print("The total is zero.")
    count = 0
    n = int(input("How many times to print 'hello world'? "))
    while count < n:
        print("hello world\n")
        count += 1
if __name__ == "__main__":
    main()
