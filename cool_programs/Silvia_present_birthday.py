import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


#recursive function
def get_name():
    name = input("type your name here:")
    print("is your name:", name, "?")
    confirm_ans = input("(answer with y(yes) or n(no)) \n")
    if confirm_ans == "y":
        print("great")
    elif confirm_ans == "n":
        print("ok boomer, try again")
        get_name()
    else:
        print("try again to answer the question")
        get_name()
    return name

def is_birthday(name):
    print("is today your birthday?")
    confirm_ans = input("(answer with y(yes) or n(no)) \n")
    if confirm_ans =="y":
        print("Happy Birthday")
        return True
    if confirm_ans =="n":
        print("ooh, is this really Silvia? Try again")
        is_birthday


def show_Harry():
        print("Wanna see a picture of Harry")
        confirm_ans = input("(answer with y(yes) or n(no)) \n")
        if confirm_ans == "y":
            image = Image.open('Harry.jpg')
            image.show()
        elif confirm_ans == "n":
            print("Who are you?")
            show_Harry()
        else:
            print("try again to answer the question")
            show_Harry()


def present():
    print("Your present in minecraft,(When the server updates again), \n is 5 diamonds and a diamond pickaxe")


def run_birthday():
    name = get_name()
    birthday = False
    print("\n")
    if name == "Silvia" or name== "silvia":
        birthday = is_birthday(name)
    print("\n")
    show_Harry()
    print("\n")
    if birthday:
        present()

run_birthday()
