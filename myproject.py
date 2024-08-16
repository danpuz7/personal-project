import random
user = input("Choose a number:")

num = random.randrange(1, 100)
print("The computer chose", num)


if int(user) > num:
    print("YOU WIN!")
elif int(user) == num:
    print("TIE!!!")
else:
    print("YOU LOSE!")
