import random
import string


def code_generation():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

code_1 = code_generation()
counter = 0
for i in range(2000000):
    code_flow = code_generation()
    if code_flow == code_1:
        counter += 1
    print(i)
print(code_1)
print(counter)