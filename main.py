import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg

def print_main_menu():
    print("=-=-= PMP =-=-=\n")
    print("Select an option: ")
    print("1 - Play a song")
    print("2 - Play a playlist")
    print("0 - Exit")

def get_opt():
    while True:
        try:
            opt = int(input("> "))
            if opt not in [0, 1, 2]:
                print("Select a valid number")
                continue
            return opt
        except ValueError:
            print("Select a valid number")

def main():
    pg.init()
    print_main_menu()
    opt = get_opt()

if __name__ == "__main__":
    main()
