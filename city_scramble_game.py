import time
import random
# time sequence
loadtime = 100
loadto = random.randint(30, 70)
while loadto < loadtime:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading:", loadto, "%")
    loadto = loadto + 1
    time.sleep(0.05)

time.sleep(0.5)
print("\n//--------------------------------------\\\ \n-------------|City Scrambler|------------- \n\\\--------------------------------------//")
score = 0

time.sleep(0.1)
startgame = input("\nStart game? (y/n)\n")

if startgame == "y" or startgame == "Y":
    while True:
        cities = ["Albuquerque", "San Francisco", "Paris", "New York", "Dublin", "Mumbai", "Bernalillo", "Las Vegas", "Cancun"]
        citiesint = random.randint(0, len(cities) - 1)

        chosenone = cities[citiesint]
        scrambledcity = []
        listofused = []
        getnum = 0
        while len(listofused) < len(chosenone):
            getnum = random.randint(0, len(chosenone) - 1)
            if getnum not in listofused:
                listofused.append(getnum)
                scrambledcity.append(chosenone[getnum])
            else:
                print("\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Unscramble this city:", scrambledcity)
        getanswer = input("")
        if getanswer == chosenone:
            score += 1
        else:
            print("wrong it was actually", chosenone)
            print("your score is", score)
            if score == 0:
                print("you are terrible")
                print("you should kill yourself...NOW!!!")
            if score > 0 and score < 5:
                print("sad")
            if score > 5 and score < 10:
                print("ok i guess")
            else:
                print("extraordinary")
            break
else:
    print("kill yourself")