import random
def guess():
    num = random.randint(1, 1000)
    attempts = 0
    while True:
        user = int(input("choose a number dumpster whore <333: "))
        if user > num:
            print("too high")
            attempts += 1
        elif user < num:
            print("too low")
            attempts += 1
        else:
            attempts += 1
            if attempts > 50:
                print(f"are you autistic the number was {num}")
                print(f"there is no way you took {attempts} tries")
                break
            elif attempts < 50 and attempts > 25:
                print(f"you took way too long to find {num}")
                print(f"you took {attempts} tries")
                break
            elif attempts < 25 and attempts > 1:
                print(f"YAY YOURE SMART YOU FOUND {num}!!!")
                print(f"YOURE NOT AUTISTIC YOU ONLY TOOK {attempts} tries")
                break
            else:
                print(f"no way you found {num} first try")
                print("filthy hacker")
                break

guess()