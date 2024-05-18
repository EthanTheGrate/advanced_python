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
time.sleep(0.05)
print("\nin case you were wondering yes i did want to call this geoguessr")

time.sleep(1)
startgame = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nStart game? (y/n)\n")

if startgame == "y" or startgame == "Y":
    while True:
        cities = ["Albuquerque", "San Francisco", "Paris", "Brooklyn", "Manhattan", "Dublin", "Mumbai", "Bernalillo", "Las Vegas", "Cancun", "Orlando", "London", "Sydney", "Atlanta", "Delhi", "Tokyo", "Shanghai", "Sao Paulo", "Sao Tome", "Orleans", "Hanoi", "Da Nang", "Saigon", "Hong Kong", "Berlin", "Hamburg", "Vienna", "Philadelphia", "Budapest", "Jerusalem", "Bucharest", "Naples", "Cairo"]
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
        time.sleep(0.25)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Unscramble this city:", scrambledcity)
        getanswer = input("")
        if getanswer == chosenone:
            score += 1
        else:
            time.sleep(0.05)
            print("wrong it was actually", chosenone)
            time.sleep(0.3)
            print("your score is", score)
            time.sleep(0.3)
            if score == 0:
                print("you are terrible")
                time.sleep(0.2)
                print("you should kill yourself...NOW!!!")
            if score > 0 and score < 10:
                print("sad")
            if score > 10 and score < 20:
                print("ok i guess")
            if score > 20 and score < 50:
                print("extraordinary")
            if score > 50:
                print("you are a master")
            break
else:
    time.sleep(0.25)
    print("\nkill yourself")