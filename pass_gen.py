import random
import string
from sys import maxsize
import pyperclip
import textwrap

minsize = abs(6)
maxsize = abs(maxsize - minsize)
given_str = ""
action = ""

length = input(f"How long do you want password to be?..."
               f"[minsize of {minsize} symbols]..."
               f"[maxsize of -->{maxsize}<-- consecutive symbols but more time consuming generation.]\n")

while length is None or length == "" or int(length) < minsize:
    given_str = ""

    print("Try again...pls...")

    length = input(f"How long do you want password to be?..."
                   f"[minsize of {minsize} symbols]..."
                   f"[maxsize of -->{maxsize}<-- consecutive symbols but more time consuming generation.]\n")

while minsize <= int(length) <= maxsize:

    given_str = ""

    for char in range(int(length)):
        upper = random.choice(ascii(string.ascii_uppercase))
        lowerr = random.choice(ascii(string.ascii_lowercase))
        nums = random.choice(ascii(string.digits))
        symbols = random.choice(ascii(string.punctuation))

        given_str += ("".join(map(str, random.sample(upper + lowerr + nums + symbols, 1)[-1])))

    print(f"Your desired length of password is -->{len(given_str)}<-- symbols "
          f"of maximum possible -->{maxsize}<-- consecutive symbols but more time consuming generation.\n")
    print(f"Your Password is from here -->{textwrap.fill(given_str, width=111)}<-- to here between the arrows.\n")
    print(f"Maximum possible -->{maxsize}<-- consecutive symbols but more time consuming generation.\n")


    action = input(f"Do you want to use again with new sample 'Y'es / 'N'o / 'E'xport to a "
          f"'password.txt' file for convenience...Enter your choice...: ").lower().strip()



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
                       f"[maxsize of -->{maxsize}<-- consecutive symbols but more time consuming generation.]")

        length = int(length)
    else:
        action = length
