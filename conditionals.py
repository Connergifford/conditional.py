import Gifford_code as Gc
from time import sleep

Gc.CLEAR_CONSOLE()

def The_Answer():
        password = input("What is the answer to life, the universe and everything?")

        if(password == '42'):
            print("Welcome wise one. I see you've traveled the galaxy. Let's begin")
            level_1()
        elif(password == "bob"):
            print("This is no time for jokes")
        elif(password == "tom"):
            print("ah yes. the funny cat that chases the mouse")
        else:
            print("I see you are new here. go get more experience and come back")

def level_1():
    print("the man opens the door")
    sleep(2)
    print("an old wizard approaches you.")
    sleep(2)
    begin_quest = input("are you ready to begin your adventures? y/n: ")
    if(begin_quest == "y"):
        print("the adventure begins...")
    else:
            print("you're correct.Best if you go get some sleep.")

The_Answer()