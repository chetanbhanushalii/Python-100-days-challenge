import random
from random import randint

# print(randint(1,9))
# print(random.random())

number_generated = randint(1,9)

if number_generated % 2 ==0:
    print("Heads")
else:
    print("Tails")