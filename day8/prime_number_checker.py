def prime_checker(number):
    if number == 2:
        print("It's a prime number.")
    elif number == 1:
        print("It's not a prime number.")
    else:
        for i in range(2, number):
            if number % i == 0:
                print("It's not a prime number.")
                break
            else:
                print("It's a prime number.")
                break


n = int(input("Check this number: "))
prime_checker(number=n)
