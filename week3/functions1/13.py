import random

name = str(input("Hello! What is your name?\n"))
print("Well, " + name + ", I am thinking of a number between 1 and 20.")
a = random.randint(1,20)
count = 1
while(True):
    num = int(input("Take a guess.\n"))
    if(num != a):
        if(num < a):
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        count += 1
    else:
        print("Good job, {}! You guessed my number in {} guesses!".format(name, count))
        break