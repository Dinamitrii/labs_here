import random
import string
from sys import maxsize

minsize = abs(6)
maxsize = abs(maxsize - minsize)
given_str = ""


length = int(input(f"How long do you want password to be?..."
                   f"[.minsize of {minsize}.]...[maxsize of -->{abs(maxsize - minsize)}<-- symbols.] "))

while length is None or length < minsize:
    given_str = ""

    print("Try again...pls...")

    length = int(input(f"How long do you want password to be?..."
                       f"[.minsize of {minsize}.]...[maxsize of -->{abs(maxsize - minsize)}<-- consecutive symbols.] "))


if int(length) >= minsize <= abs(maxsize - minsize):
    given_str = ""

    for char in range(int(length)):
        upper = random.choice(ascii(string.ascii_uppercase))
        lowerr = random.choice(ascii(string.ascii_lowercase))
        nums = random.choice(ascii(string.digits))
        symbols = random.choice(ascii(string.punctuation))

        given_str += ("".join(map(str, random.sample(upper + lowerr + nums + symbols, 1)[-1])))

print("\n")
print(f"Your desired length of password is -->{len(given_str)}<-- symbols."
          f"[maximum possible -->{abs(maxsize - minsize)}<-- consecutive symbols.]")
print("\n")
print(f"Your Password is from here -->{given_str}<-- to here.")
print("\n")
print(f"Maximum possible -->{abs(maxsize - minsize)}<-- consecutive symbols.")
