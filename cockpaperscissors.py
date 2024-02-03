import time
import random

def cockpaperscissors():

    botchoice = random.randint(1,3)

    print("**///COCK! PAPER! SCISSORS!!!\\\**\n")
    time.sleep(1)
    print("rock = 1")
    time.sleep(0.05)
    print("paper = 2")
    time.sleep(0.05)
    print("scissors = 3")
    time.sleep(0.5)
    getuser = int(input("enter your choice\n"))

    if getuser == botchoice:
        print("lmao you both chose the same thing")
    elif (getuser == 1) and (botchoice == 2) or (getuser == 2) and (botchoice == 3) or (getuser == 3) and (botchoice == 1):
        time.sleep(0.2)
        print("you failed womp womp")
        time.sleep(0.2)
        print("try again??")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n")
        cockpaperscissors()
    elif (getuser == 1) and (botchoice == 3) or (getuser == 2) and (botchoice == 1) or (getuser == 3) and (botchoice == 2):
        time.sleep(0.2)
        print("you win yayyy")
        time.sleep(0.2)
        print("youre not an mentally disabled person")
    else:
        print("ARE YOU FUCKING RETARDED")
        time.sleep(0.2)
        print("YOU ARE STUPID")
        time.sleep(0.2)
        print("KYS")
        time.sleep(0.2)
        print("what the f̸̑̈ͅu̸̮̝͂̊c̶̗̏̀k̵͕̃̽ is wrong with you")
        time.sleep(0.5)
        print("are you mental")
        time.sleep(0.5)
        print("you should kill yourself")
        time.sleep(0.5)
        while True:
            time.sleep(0.1)
            luck = random.randint(1, 20)
            if luck == 20:
                print("you should end your life")
            elif luck == 19:
                print("you dont deserve anything")
            elif luck == 18:
                print("your life is nothing")
            elif luck == 17:
                print("you serve zero purpose")
            elif luck == 16:
                print("you are a worthless b**** a** person")
            elif luck < 16 and luck > 10:
                print("you should jump off a bridge")
            elif luck < 10 and luck > 5:
                print("kill yourself")
            elif luck == 1:
                print("im so tired")
                break
            else:
                print("end your life")

cockpaperscissors()