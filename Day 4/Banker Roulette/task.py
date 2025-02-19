import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

len_friends = len(friends)

random_no = random.randint(0,len_friends-1)
print(friends[random_no])