import random


# def guess_number(x):
#     count = 3
#     random_number = random.randint(1, x)
#
#     guess = 0

#     while count > 0:
#         guess = int(input(f"Guess the between 1 to {x}: "))

#         if guess != random_number:
#             if guess < random_number:
#                 count -= 1
#                 print("Your number is low!!")
#             elif guess > random_number:
#                 count -= 1
#                 print("Your number is high!!")
#         else:
#             print(f"You have guessed the correct number {random_number}")
#             break
#     if count == 0:
#         print("Your trial is over")


# guess_number(10)


# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = ""
#     while feedback != "c":

#         if low != high:
#             guess = random.randint(low, high)
#         else:
#             guess = low
#         feedback = input(
#             f"Is the {guess} too high (H) or too low (L) or Correct (C): ").lower()
#         if feedback == "h":
#             high = guess-1
#         elif feedback == "l":
#             low = guess+1
#     print("Yayyy, you have guessed the number the correctly!!")


# computer_guess(1000)
