# Program to check if a number is prime or composite

# Input from the user
number = int(input("Enter a number: "))

if number > 1:
    # Check for factors
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"{number} is a composite number.")
            break
    else:
        print(f"{number} is a prime number.")
elif number == 1:
    print("1 is neither prime nor composite.")
else:
    print("Enter a positive integer greater than 0.")
