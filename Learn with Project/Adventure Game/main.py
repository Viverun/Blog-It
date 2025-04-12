#Adventure Game
from itertools import count

Intro = "Hey! Welcome to this adventure game \nHere you will receive a series of choices\nand your fate will be decided on the same\nGood Luck! and Be Careful...\n"
print(Intro)
name = input("Please enter your name: ")
print(f"So {name}, you somehow found yourself in a maze and in order to clear this maze \nyou need a series of right step taken in order\n")
print("You have two lane in your path in which one leads to dense RainForest and another leads to drought up Desert \nwhich one will you choose?\n")
choice = input("Please select your option\n").strip().lower()
if choice == "rainforest" or choice == "desert":
    print(f"So you have chosen {choice} as your choice")
    if choice == "rainforest":
        print("This rainforest involves a series of hurdle to clear and in order to survive here you\nmust clear them all.. So are you ready?....\nPfftt... You don't have a choice here so buckle up\n")
        print("Now for the first task.... You have to mention atleast 3 basic stuff you need to survive in this Rainforest\nIf you failed to do so...You Die!\n")

        need_list = ["water", "shelter", "food", "cloth", "clothes", "fire"]
        count = 0
        Ans1 = input("Add first: ").strip().lower()
        if Ans1 in need_list:
            print("Correct one! Now next...")
            count += 1
        Ans2 = input("Add second: ").strip().lower()
        if Ans2 in need_list:
            print("Correct again! Now next...")
            count += 1
        Ans3 = input("Add third: ").strip().lower()
        if Ans3 in need_list:
            print("Correct again! ...")
            count += 1
        comp = f"So you have chosen {Ans1}, {Ans2}, {Ans3}"
        if count == 3:
            print("You survived..")
        else:
            print("You died because of your lack of survival knowledge")
