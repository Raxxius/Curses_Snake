import curses
import time
import random
# import gspread
from curses import wrapper, KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from curses.textpad import Textbox, rectangle
# from google.oauth2.service_account import Credentials

"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('curses_snake')
"""


def main(stdscr):
    intro(stdscr)
    game(stdscr)
    # scores()


def intro(stdscr):
    curses.curs_set(0)
    title = curses.newwin(13, 32, 7, 25)
    stdscr.clear()
    title.clear()
    title.addstr("Welcome to: \n"
                 "   _____             __       \n"
                 "  / ___/____  ____ _/ /_____  \n"
                 "  \__ \/ __ \/ __ `/ //_/ _ \ \n"
                 " ___/ / / / / /_/ / ,< /  __/ \n"
                 "/____/_/ /_/\__,_/_/|_|\___/  \n"
                 "\n"
                 "press any key to continue")
    
    stdscr.refresh()
    title.refresh()
    stdscr.getch()


def game(stdscr):
    # screens
    score = 0
    player_score = curses.newwin(1, 10, 0, 34)
    game_area = curses.newwin(21, 78, 1, 1)
    instructions = curses.newwin(1, 79, 23, 0)
    stdscr.clear()

    curses.curs_set(0)
    player_score.clear()
    game_area.clear()
    instructions.clear()

    rectangle(stdscr, 0, 0, 22, 79)
    player_score.addstr(f"Score: {score}")

    try:
        instructions.addstr("  Use the Keypad to move the snake to the food," 
                            "press P to pause and X to exit")
    except curses.error:
        pass

    stdscr.refresh()
    instructions.refresh()
    player_score.refresh()
    stdscr.getch()

    # Initate snake
    snake = [(11, 40), (12,40), (13,40)]


    # game logic
    score = 0

# def scores(stdscr):


wrapper(main)
