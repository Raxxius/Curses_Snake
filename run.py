import curses
import time
import random
# import gspread
from curses import wrapper, KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
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
    curses.noecho()
    curses.curs_set(0)
    player_score = curses.newwin(1, 10, 0, 34)
    game_area = curses.newwin(22, 79, 1, 1)
    game_area.keypad(1)
    instructions = curses.newwin(1, 79, 23, 0)
    stdscr.clear()

    player_score.clear()
    game_area.clear()
    instructions.clear()

    player_score.addstr(f"Score: {score}")

    try:
        instructions.addstr("  Use the Keypad to move the snake to the food," 
                            "press P to pause and X to exit")
    except curses.error:
        pass

    stdscr.refresh()
    instructions.refresh()
    player_score.refresh()

    # Initiate snake
    snake = [(11, 75), (11, 76), (11, 77)]

    # Initiate food

    food = [random.randint(1, 21), random.randint(1, 78)]
    game_area.addch(food[0], food[1], ".")

    # Initial direction of snake = lefet
    key = KEY_LEFT

    # game logic
    while key != 120 or 88:

        # game speed
        game_area.timeout(150)
        game_area.border(0)

        prev_key = key
        new_key = game_area.getch()
        key = key if new_key == -1 else new_key

        # Ignore keystrokes that aren't arrow keys, P(or p) and X(or x)
        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 120, 88]:
            key = prev_key
        
        # calculate snake coordinates
        y = snake[0][0]
        x = snake[0][1]

        snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

        # check border collision
        if y == 0:
            break
        if y == 21:
            break
        if x == 0:
            break
        if x == 78:
            break
        
        # check snake collision
        if snake[0] in snake[1:]: 
            break

        if snake[0] == food:
            food = []
            score += 1
            player_score.clear()
            player_score.addstr(f"Score: {score}")
            player_score.refresh()
            while food == []:
                food = [random.randint(1, 21), random.randint(1, 78)]
                if food in snake: food = []
            game_area.addch(food[0], food[1], ".")
        # remove last part of snake
        else:  
            last = snake.pop()
            game_area.addch(last[0], last[1], ' ')
        game_area.addch(snake[0][0], snake[0][1], "*")


# def scores(stdscr):


wrapper(main)
