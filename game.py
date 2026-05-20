import random
generate_random_numbers =  random.randint(1, 100)
guess = int(input("guess a number between 1 and 100: "))
while guess != generate_random_numbers:
            if guess < generate_random_numbers:
                    print("too low")
            elif guess > generate_random_numbers:
                    print("too high")
            guess = int(input("guess a number between 1 and 100: "))
print("congratulations you guessed the number")