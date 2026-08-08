import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg

def print_main_menu():
    print("=-=-= PMP =-=-=\n")
    print("Select an option: ")
    print("1 - Play a song")
    print("2 - Play a playlist")

def get_opt():
    while True:
        try:
            opt = int(input("> "))
            return opt
        except ValueError:
            print("Select a valid number")

def main():
    pg.init()
    print_main_menu()
    get_opt()

if __name__ == "__main__":
    main()
