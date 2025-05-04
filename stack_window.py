import curses
from vertical_print import *

SPACES = 3
HSPACES = 2 + SPACES

def draw_stackwin(stackwin, gamestate):
    (words, stack1, stack2, stack3, stack4) = gamestate
    stackwin.box('#', '#')

    (y, x) = stackwin.getyx()
    (lines, cols) = stackwin.getmaxyx()
    voffset = (len(stack1) * SPACES)//2

    vertical_print(y+lines//2 - voffset, cols//2 - 2*HSPACES+1, SPACES, stackwin, stack1)
    vertical_print(y+lines//2 - voffset, cols//2 - 1*HSPACES+1, SPACES, stackwin, stack2)
    vertical_print(y+lines//2 - voffset, cols//2 + 1*HSPACES-1, SPACES, stackwin, stack3)
    vertical_print(y+lines//2 - voffset, cols//2 + 2*HSPACES-1, SPACES, stackwin, stack4)
