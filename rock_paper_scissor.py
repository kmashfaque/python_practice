import random


# def play():
#     user = input(" 's' for scissors, 'r' for rock, 'p' for paper: \n")

#     computer = random.choice(['r', 's', 'p'])

#     if user == computer:
#         return "The game is tied"
#     if is_won(user, computer):
#         return "You won"
#     return "You lost"


# def is_won(palyer, opponent):
#     if (palyer == "r" and opponent == "s") or (palyer == "s" and opponent == "p") or (palyer == "p" and opponent == "r"):
#         return True


# result = play()
# print(result)


# computer_count = 0
# user_count = 0
# tied = 0
# count = 10


# def play(computer_count, user_count, count, tied):

#     while count > 0:
#         user = input(" 's' for scissors, 'r' for rock, 'p' for paper: \n")

#         computer = random.choice(['r', 's', 'p'])
#         if user == computer:
#             tied += 1
#         if is_won(user, computer):
#             user_count += 1

#         elif is_won(computer, user):
#             computer_count += 1

#         elif count == 0:
#             break
#         count -= 1
#     return (computer_count, user_count, tied)


# def is_won(palyer, opponent):
#     if (palyer == "r" and opponent == "s") or (palyer == "s" and opponent == "p") or (palyer == "p" and opponent == "r"):
#         return True


# computer_count, user_count, tied = play(
#     computer_count, user_count, count, tied)

# print(f"Computer Wins {computer_count} times.")
# print(f"User Wins {user_count} times.")
# print(f"Tied {tied} times.")


# state = random.getstate()

# for i in range(5):
#     val = random.randint(1, 10)
#     print(val, end="")

# print()
# state2 = random.setstate(state)


# for i in range(5):
#     val2 = random.randint(1, 10)
#     print(val2, end="")


# for i in range(10):
#     seed = random.seed(10)
#     al = random.randint(1, 10)
#     print(al)


# sed = random.seed(7)

# print(random.randint(1, 1000))

# sed2 = random.seed(7)

# print(random.randint(1, 1000))

# print(random.randint(1, 1000))

# lists = [1, 2, 3, 4, 5, 6, 7]
# coise = random.choices(lists, weights=[0, 2, 1, 2, 3, 4, 6], k=10)
# print(coise)
