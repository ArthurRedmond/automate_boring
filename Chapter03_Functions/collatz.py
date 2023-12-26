"""Run collatz conjecture on integer until it equals 1"""

def collatz(num):
    """Run integer through collatz conjecture until it equals 1"""
    if num.isdigit():
        num = int(num)
        while num > 1:
            if num % 2 == 0:
                # If number is even print number // 2
                num = num // 2
                print(num)
            else:
                # If number is odd print 3 * number + 1
                num = (num * 3) + 1
                print(num)
    else:
        print("Invalid entry.")

def main():
    """Main function"""
    number = input("Please enter a number: ")
    collatz(number)

if __name__ == "__main__":
    main()
