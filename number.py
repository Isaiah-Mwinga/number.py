import random
import math
lower = int(input("Enter lower bound:-"))
upper= int(input("Enter upper bound:-"))
x = random.randint(lower, upper)
print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      "chances to guess the integer\n")
count = 0
while count < math.log(upper - lower + 1, 2):
    count +=1
    guess = int(input("Guess a number:-"))
    if x == guess:
        print("congratulations folk",
              count, "try it")
        break
    elif x > guess:
        print("you guess too small niggah!")
    if x < guess:
        print("you Guessed too high pappy!")
    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" %x)
        print("\tBetter Luck Next time pappy!")
