from platform import platform
from sys import maxsize

maximum_number = abs(maxsize)

counter_fizz_buzz = 0
counter_fizz = 0
counter_buzz = 0

number = int(input("Enter a number to start from: "))

while True:
    number += 1
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz" + f' {number}')
        counter_fizz_buzz += 1
        print(f"FizzBuzz result is: !!!{counter_fizz_buzz}!!!")
        continue
    if number % 3 ==0:
        print("Fizz" + f' {number}')
        counter_fizz += 1
        print(f"Fizz result is: !!{counter_fizz}!!")
        continue
    if number % 5 == 0:
        print("Buzz" + f' {number}')
        counter_buzz += 1
        print(f"Buzz result is: !{counter_buzz}!")
        continue

    print(number)
