def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    num = int(input("Enter a number: "))
    print(even_or_odd(num))

if __name__ == "__main__":
    main()