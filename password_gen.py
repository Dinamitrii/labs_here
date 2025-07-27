import random
import string
from os import linesep
from sys import maxsize
import pyperclip
import textwrap
import time



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

while minsize <= int(length) <= maxsize or action.lower() == "y":

    starting_time_zero_point = time.time()

    given_str = ""

    for char in range(int(length)):

        upper = random.choice(ascii(string.ascii_uppercase))
        lowerr = random.choice(ascii(string.ascii_lowercase))
        nums = random.choice(ascii(string.digits))
        symbols = random.choice(ascii(string.punctuation))

        given_str += ("".join(map(str, random.sample(upper + lowerr + nums + symbols, 1)[-1])))
    endtime_zero_point = time.time()

    print(f"Your desired length of password is -->{len(given_str)}<-- symbols "
          f"of maximum possible -->{maxsize}<-- consecutive symbols but more time consuming generation.\n")

    print(f"Your Password is from here -->{textwrap.fill(given_str, width=162)}<-- to here exactly "
          f"between the arrows.\n")

    action = input(f"Do you want to use again with new sample 'Y'es / 'N'o / 'E'xport to a "
                   f"'generated_password.txt' file for convenience...Enter your choice...:\n").lower().strip()

    if action.lower() == "e":
        pyperclip.copy(given_str)
        hashed_pass = abs(hash(given_str))
        open('generated_password.txt', 'w').writelines(pyperclip.paste())
        open('generated_password.txt', 'a').writelines('\n')
        open('generated_password.txt', 'a').writelines(str(hashed_pass))

        print("Exported to 'generated_password.txt'")

        print(f"Until exporting it took exactly {(endtime_zero_point - starting_time_zero_point):.3f} seconds "
              f"to generate the password.")
        break

    elif action.lower() == "n":
        pyperclip.copy(given_str)
        hashed_pass = abs(hash(given_str))
        open('generated_password.txt', 'w').writelines(pyperclip.paste())
        open('generated_password.txt', 'a').writelines('\n')
        open('generated_password.txt', 'a').writelines(str(hashed_pass))
        print("Exported to 'generated_password.txt' by system settings")

        print(f"Until exiting it took exactly {(endtime_zero_point - starting_time_zero_point):.3f} seconds "
              f"to generate the password.")
        break

    elif action.lower() == "y":
        length = input(f"How long do you want password to be?..."
                       f"[minsize of {minsize} symbols]..."
                       f"[maxsize of -->{maxsize}<-- consecutive symbols but more time consuming generation.]!!!\n")
        length = int(length)
        continue
    else:
        action = action.lower() == "n"

endtime_zero_point = time.time()

print(f"Your 'FUN' continued for 'ABOUT ONLY'{(endtime_zero_point - starting_time_zero_point):.3f} seconds.")