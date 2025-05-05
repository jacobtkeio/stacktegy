import curses
from vertical_print import *

HEADER = 4
SPACES = 2
MAX_WORD = 20

def draw_wordswin(wordswin, gamestate):
    (words, stack1, stack2, stack3, stack4) = gamestate
    wordswin.box('#', '#')

    (y, x) = wordswin.getyx()
    (lines, cols) = wordswin.getmaxyx()

    vertical_print(y+HEADER, x+cols//2 - MAX_WORD//2, SPACES, wordswin, words)
