### Credits

- https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Slant&t=Snake ascii art for snake title page

## bug
- While code prevented right and down keystrokes from doubling back, left and up keystrokes would result in gameover.
## solution
- changed code to directly interact at the keystoke entry. This fixed the code.

## bug
- curses.curs_set(0) caused an error in Heroku application
## solution
- no solution, had to remove curses.curs_set() function.


