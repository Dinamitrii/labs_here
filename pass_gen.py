import random
import string
from sys import maxsize
import pyperclip

minsize = abs(6)
maxsize = abs(maxsize - minsize)
given_str = ""
# length = 0

length = input(f"How long do you want password to be?..."
               f"[.minsize of {minsize} symbols.]..."
               f"[maxsize of -->{abs(maxsize - minsize)}<-- consecutive symbols.]")

while length is None or length == "" or int(length) < minsize:

    given_str = ""

    print("Try again...pls...")


    length = input(f"How long do you want password to be?..."
                   f"[.minsize of {minsize} symbols.]..."
                   f"[maxsize of -->{abs(maxsize - minsize)}<-- consecutive symbols.]")
while True:

    if minsize < int(length) <= abs(maxsize - minsize):

        given_str = ""


    for char in range(int(length)):

        upper = random.choice(ascii(string.ascii_uppercase))
        lowerr = random.choice(ascii(string.ascii_lowercase))
        nums = random.choice(ascii(string.digits))
        symbols = random.choice(ascii(string.punctuation))

        given_str += ("".join(map(str, random.sample(upper + lowerr + nums + symbols, 1)[-1])))

    print(f"Your desired length of password is -->{len(given_str)}<-- symbols."
                f"maximum possible -->{abs(maxsize - (minsize + minsize))}<-- consecutive symbols.")
    print(f"Your Password is from here -->{given_str}<-- to here between the arrows.")
    print(f"Maximum possible -->{abs(maxsize - (minsize + minsize))}<-- consecutive symbols.")

    print(f"{input("Do you want to use again with new sample 'Y'/yes or 'N'/no or 'E'/export"
                       " to txt file for convenience...Enter your choice Y/N/E...:\n ")}")


    if input().lower() == "e":
        pyperclip.copy(given_str)
        open('password.txt', 'w').writelines(pyperclip.paste())

        print("Exported to 'password.txt'")

        break

    elif input().lower() == "n":
        pyperclip.copy(given_str)
        open('password.txt', 'w').writelines(pyperclip.paste())

        print("Exported to 'password.txt' by system settings")

        break

    elif input().lower() == "y":

        length = input(f"How long do you want password to be?..."
                  f"[.minsize of {minsize} symbols.]..."
                  f"[maxsize of -->{abs(maxsize - minsize)}<-- consecutive symbols.]")

        length = int(length)


        # for char in range(length):
        #
        #     upper = random.choice(ascii(string.ascii_uppercase))
        #     lowerr = random.choice(ascii(string.ascii_lowercase))
        #     nums = random.choice(ascii(string.digits))
        #     symbols = random.choice(ascii(string.punctuation))
        #
        #     given_str += ("".join(map(str, random.sample(upper + lowerr + nums + symbols, 1)[-1])))
        #
        #     continue


    # print(f"Your desired length of password is -->{len(given_str)}<-- symbols."
    #             f"maximum possible -->{abs(maxsize - minsize)}<-- consecutive symbols.")
    # print(f"Your Password is from here -->{given_str}<-- to here between arrows.")
    # print(f"Maximum possible -->{abs(maxsize - minsize)}<-- consecutive symbols.")
