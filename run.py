import curses
import time
import gspread
from curses import wrapper, KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from curses.textpad import Textbox, rectangle
from google.oauth2.service_account import Credentials

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

    # screens
    score = curses.newwin(1, 10, 0, 34)
    game_area = curses.newwin(23, 79, 0, 0)
    instructions = curses.newwin(3, 79, 20, 0)
    stdscr.clear()
# Game area

    score.clear()
    game_area.clear()
    instructions.clear()

    try:
        rectangle(stdscr, 0, 0, 23, 74)
    except curses.error:
        pass


wrapper(main)
