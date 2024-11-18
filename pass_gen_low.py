import random
import string

from sys import maxsize

length = input("How long do you want password to be?...[minsize of 6 characters]...: ")

length = int(length)

str_with_result = ""

result = random.sample((((random.choice(ascii(string.ascii_lowercase) + (random.choice(ascii(string.digits))) +
                                      (random.choice(string.ascii_uppercase)) +
                                      (random.choice(ascii(string.punctuation)))))for x in (range(len(str_with_result)), length)),),1)

# print(result)

str_with_result += ("".join(str(result) for x in range(length)))




print(str_with_result)
print(len(str_with_result))