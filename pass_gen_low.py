import random
import string

from sys import maxsize

length = input("How long do you want password to be?...[minsize of 6 characters]...: ")

length = int(length)

result = ""
for _ in range(length):
    result = random.sample((random.choices(ascii(string.ascii_lowercase) + random.choice(ascii(string.digits))
                                           + random.choice(ascii(string.ascii_uppercase) + random.choice(ascii(string.punctuation))))),1)

    result += ("".join(str(result)))

print(result)
print(len(result))