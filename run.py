import curses
import time
import gspread
from curses import wrapper, KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from curses.textpad import Textbox, rectangle
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('curses_snake')

def main(stdscr):

    stdscr.clear()
# Game area
    gamearea = curses.newwin(23, 79, 0, 0)
    gamearea.clear()

    try:
        rectangle(stdscr, 0, 0, 23, 79)
    except curses.error:
        pass


wrapper(main)
