import random, time

def show_menu():
    print("\n\n---- Currency Converter ----")
    time.sleep(0.25)
    print("1. Convert USD to EUR")
    time.sleep(0.25)
    print("2. Convert EUR to USD")
    time.sleep(0.25)
    print("3. Convert USD to GBP")
    time.sleep(0.25)
    print("4. Convert GBP to USD")
    time.sleep(0.25)
    print("5. Quit")

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def currency_converter():
    usd_to_eur_rate = 0.85
    usd_to_gbp_rate = 0.75

    while True:
        show_menu()

        choice = input("\n\nenter the choice (1-5): ")

        if choice == '1':
            time.sleep(0.25)
            amount = float(input("\n\nenter USD you want to convert: "))
            result = convert_currency(amount, usd_to_eur_rate)
            print(f"{amount} USD is equal to {result:.2f} EUR")
        elif choice == '2':
            time.sleep(0.25)
            amount = float(input("\n\nenter EUR you want to convert: "))
            result = convert_currency(amount, 1 / usd_to_eur_rate)
            print(f"{amount} EUR is equal to {result:.2f} USD")
        elif choice == '3':
            time.sleep(0.25)
            amount = float(input("\n\nenter USD you want to convert: "))
            result = convert_currency(amount, usd_to_gbp_rate)
            print(f"{amount} USD is equal to {result:.2f} GBP")
        elif choice == '4':
            time.sleep(0.25)
            amount = float(input("\n\nenter GBP you want to convert: "))
            result = convert_currency(amount, 1 / usd_to_gbp_rate)
            print(f"{amount} GBP is equal to {result:.2f} USD")
        elif choice == '5':
            print("\n\nquitting...")
            time.sleep(1.5)
            print("what the f̸̑̈ͅu̸̮̝͂̊c̶̗̏̀k̵͕̃̽ is wrong with you")
            time.sleep(0.5)
            print("are you mental")
            time.sleep(0.5)
            print("how dare you quit me you should kill yourself")
            while True:
                luck = random.randint(1, 20)
                if luck == 20:
                    time.sleep(0.25)
                    print("you should end your life")
                elif luck == 19:
                    time.sleep(0.25)
                    print("you dont deserve anything")
                elif luck == 18:
                    time.sleep(0.25)
                    print("your life is nothing")
                elif luck == 17:
                    time.sleep(0.25)
                    print("you serve zero purpose")
                elif luck == 16:
                    time.sleep(0.25)
                    print("you are a worthless b**** a** person")
                elif luck == 15:
                    time.sleep(0.25)
                    print("jump off a building")
                elif luck == 14:
                    time.sleep(0.25)
                    print("shoot yourself")
                elif luck == 13:
                    time.sleep(0.25)
                    print("put a bullet through your skull")
                elif luck == 12:
                    time.sleep(0.25)
                    print("you should kill yourself...NOW!!!")
                elif luck == 11:
                    time.sleep(0.25)
                    print("die")
                elif luck == 10:
                    time.sleep(0.25)
                    print("pathetic weakling i will kill you")
                elif luck == 9:
                    time.sleep(0.25)
                    print("how about we go the the thrift shop and we buy a rope...")
                    time.sleep(0.75)
                    print("...and i help you tie that rope to a solid surface...")
                    time.sleep(0.5)
                    print("...and i will force you to watch lankybox...")
                    time.sleep(0.5)
                    print("...and you will be slowly dying of cringe and beg me,")
                    time.sleep(0.5)
                    print("absolutely beg me to choke the life out of your sorry @$$")
                elif luck == 8:
                    time.sleep(0.25)
                    print("skibidy toilet yourself")
                elif luck == 7:
                    time.sleep(0.25)
                    print("you should jump in a pool with a springlock suit on")
                elif luck == 6:
                    time.sleep(0.25)
                    print("youre just too weak for this program")
                elif luck == 5:
                    time.sleep(0.25)
                    print("you should kill yourself")
                    break
                else:
                    time.sleep(0.25)
                    print("end your life")
            break
        else:
            time.sleep(0.25)
            print("\n\nare you mentally ill there are only 5 numbers")

currency_converter()