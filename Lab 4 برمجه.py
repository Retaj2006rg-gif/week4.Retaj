########
total = 0

for i in range(10):
    num = int(input("Enter a number: "))

    if num == 0:
        break

    if num < 0:
        continue

    if num % 2 == 0:
        total += num   # augmented assignment

print("Final Sum =", total)
#######
num = int(input("Enter a number: "))

for i in range(1, 13):
    result = num * i

    if result % 3 == 0:
        continue

    if result > 50:
        break

    print(num, "x", i, "=", result)
########
import random

secret = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("Guess a number (1-20): "))

    if guess < 1 or guess > 20:
        print("Invalid number!")
        continue

    attempts += 1  

    if guess == secret:
        print("Correct! ")
        print("Attempts:", attempts)
        break
    else:
        print("Try again!")
#########
n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):

    if i > 50:
        break

    if i % 8 == 0:
        continue

    if i % 4 == 0:
        count += 1

print("Count =", count) 
#######
for i in range(1, 6):

    for j in range(1, i + 1):

        if i * j > 6:
            break

        if j == 3:
            continue

        print(j, end=" ")

    print()