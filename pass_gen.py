import random
import string
from sys import maxsize
import pyperclip
import textwrap


minsize = abs(6)
maxsize = abs(maxsize - minsize)
given_str = ""


length = input(f"How long do you want password to be?..."
               f"[minsize of {minsize} symbols]..."
               f"[maxsize of -->{maxsize}<-- consecutive symbols more time consuming.]")

while length is None or length == "" or int(length) < minsize:

    given_str = ""

    print("Try again...pls...")


    length = input(f"How long do you want password to be?..."
                   f"[minsize of {minsize} symbols.]..."
                   f"[maxsize of -->{maxsize}<-- consecutive symbols more time consuming.]")

while minsize < int(length) <= maxsize:

    given_str = ""


    for char in range(int(length)):

        upper = random.choice(ascii(string.ascii_uppercase))
        lowerr = random.choice(ascii(string.ascii_lowercase))
        nums = random.choice(ascii(string.digits))
        symbols = random.choice(ascii(string.punctuation))

        given_str += ("".join(map(str, random.sample(upper + lowerr + nums + symbols, 1)[-1])))

    print(f"Your desired length of password is -->{len(given_str)}<-- symbols."
                f"of maximum possible -->{maxsize}<-- consecutive symbols more time consuming.\n")
    print(f"Your Password is from here -->{textwrap.fill(given_str, width=111)}<-- to here between the arrows.\n")
    print(f"Maximum possible -->{maxsize}<-- consecutive symbols more time consuming.\n.")

    print(f"Do you want to use again with new sample 'Y'/yes or 'N'/no or 'E'/export to a "
          f".txt file for convenience...Enter your choice Y/N/E...: ")

    action = input().lower()

    if action == "e":
        pyperclip.copy(given_str)
        open('password.txt', 'w').writelines(pyperclip.paste())

        print("Exported to 'password.txt'")
        break

    elif action == "n":
        pyperclip.copy(given_str)
        open('password.txt', 'w').writelines(pyperclip.paste())

        print("Exported to 'password.txt' by system settings")

        break

    elif action == "y":

        length = input(f"How long do you want password to be?..."
                  f"[minsize of {minsize} symbols.]..."
                  f"[maxsize of -->{maxsize}<-- consecutive symbols more time consuming.]")

        length = int(length)
    else:
        action = length