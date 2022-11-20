command = input()
sum_of_all_prime_number = 0
sum_of_all_non_prime_number = 0
while command != "stop":
    number = int(command)
    if number < 0:
        print(f"Number is negative.")
        command = input()
    elif number == 0:
        command = input()
    elif number > 3:
        if number % 2 == 0:
            sum_of_all_non_prime_number += number
            command = input()
        elif number % 3 == 0:
            sum_of_all_non_prime_number += number
            command = input()
        else:
            sum_of_all_prime_number += number
            command = input()
    else:
        sum_of_all_prime_number += number
        command = input()
print(f"Sum of all prime numbers is: {sum_of_all_prime_number}")
print(f"Sum of all non prime numbers is: {sum_of_all_non_prime_number}")