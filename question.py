# givenstring = "3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 39 42 43 44 45 46"
# placestring = ""
# holdvar = 0

# cum = givenstring.split()
# print(cum)
# for i in range(len(cum)):
#     holdvar = cum[i]
#     if int(holdvar) % 3 == 0 and int(holdvar) % 5 == 0:
#         placestring += (holdvar)
#         placestring += (" ")
# print(placestring)



# listoffruits = ["cucumber", "eggplant", "corn", "cauliflower", "zucchini", "asparagus"]
# end = []
# first = "h"

# for i in range(len(listoffruits)):
#     first = listoffruits[i][0]
#     if first == "a" or first == "m":
#         if len(listoffruits[i]) > 5:
#             end.append(listoffruits[i])
# print(end)



# get = int(input("gimme yo money\n"))

# for i in range(12):
#     print(get, "x", i, "=", get * i)



# string = "GETOUTOFMYHEADN"

# string = string.lower()
# string = string.replace("n", "Ethan")
# print(string)

# string = "Hello world I am the string you were talking about"
# holder = "text"
# string = string.split()

# for i in range(len(string)):
#     holder = string[i]
#     if len(holder) >= 5:
#         print(holder)

# string = "Hello world I am the string you were talking about appropriately approximately at a time ago"
# holder = "text"
# string = string.split()

# for i in range(len(string)):
#     holder = string[i]
#     if len(holder) >= 5:
#         if holder[0] == "a":
#             print(holder)

# string = "H3ll0 w0rld I 6m the str1ng y0u w3r3 t6lk1ng ab0u1 6ppr0pri6t3ly appr0x1m6t3ly 6t a t1me ag0"
# holder = "text"

# for i in range(len(string)):
#     holder = string[i]
#     if holder.isnumeric() == True:
#         print(holder)

string = "H3ll0 w0rld I 6m the str1ng y0u w3r3 t6lk1ng ab0u1 6ppr0pri6t3ly appr0x1m6t3ly 6t a t1me ag0"
holder = "text"

for i in range(len(string)):
    holder = string[i]
    if holder.isalpha() == True:
        print(holder)