
def main():
    # Program to find factorial of a number using recursive method.

    num = int(input("Enter a number: "))
    fact = calculate_factorial(num)
    print(f'The factorial of {num} is {fact}. ')

def calculate_factorial(num):
    if num  == 1 or num == 0:
        return 1
    else:
        return num * calculate_factorial(num - 1)
    

if __name__ == "__main__":
    main()
