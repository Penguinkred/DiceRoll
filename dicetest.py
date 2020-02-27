# import secrets for a Pseudo Random Number Generator
import secrets
# assign number on the die and set rolls to 0
dice = [1, 2, 3, 4, 5, 6]
# check to see if user types a whole number
while True:
    try:
        roll = int(input("Choose whole number of dice to roll: "))
        break
    except ValueError:
        print("Enter a whole number")
        pass
# Blank list for easy dice roll reading
outcome = []
# print out dice roll of users imputed amount
i = 0
while i < roll:
    outcome.append(secrets.choice(dice))
    i += 1
print(outcome)
