#
# secret = 4
#
# guess = int(input("Vpiši skrito število: "))
#
# if secret == guess:
#     print("Čestitke, uganil si pravilno število!")
# else:
#     print("Ups, to ne bo pravilno. Skrito število je " + str(secret))
#


# # while zanka
# secret = 4
# guess = None
#
# while guess != secret:
#     guess = int(input("Vpiši skrito število: "))
#
#     if secret == guess:
#         print("Čestitke, uganil si pravilno število!")
#     else:
#         print("Ups, to ne bo pravilno, poskusi znova.")
#
# print("Igra končana!")


# # for zanka
# secret = 4
# guess = None
#
# print("Ugani število, imaš 5 poskusov.")
# for trial_count in range(5):
#     guess = int(input("Vpiši skrito število: "))
#     print(f"to je tvoj {trial_count + 1}. poskus.")
#
#     if secret == guess:
#         print("Čestitke, uganil si pravilno število!")
#         break
#     else:
#         print("Ups, to ne bo pravilno. Poskusi ponovno.")
#
# print("Igra končana!")
#
# # if not (guess == secret):
# if guess != secret:
#     print(f"Pravilno število je bilo {secret}.")


# While - break
# secret = 4
#
# while True:
#     guess = int(input("Vpiši skrito število: "))
#
#     if secret == guess:
#         print("Čestitke, uganil si pravilno število!")
#         break
#     else:
#         print("Ups, to ne bo pravilno, poskusi znova.")
#
# print("Igra končana!")
#

import random

attempts = 0
secret = random.randint(1, 30)

while True:
    guess = int(input("Vpiši skrito število: "))
    attempts += 1
    # attempts = attempts + 1

    if guess > secret:
        print("Ne, poskusi z nižjim številom.")
    elif guess < secret:
        print("Ups, to ne bo pravilno, poskusi z višjim številom.")
    else:
        print("Čestitke, uganil si pravilno število!")
        print(f"Porabil si {attempts} poskusov.")
        with open("high-score.txt", "w") as attempts_file:
            attempts_file.write(str(attempts))
        break

print("Igra končana!")

