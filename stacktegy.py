import curses
from random import random

from sentence import *
from words_window import *
from input_window import *
from stack_window import *

DIV = 5
RING = 2
MAX_WORD = 20
MAX_STACK = 8

windows = []

stack1 = [int(100*random()) for i in range(MAX_STACK)]
stack2 = [int(100*random()) for i in range(MAX_STACK)]
stack3 = [int(100*random()) for i in range(MAX_STACK)]
stack4 = [int(100*random()) for i in range(MAX_STACK)]
words = []

gamestate = (words, stack1, stack2, stack3, stack4)


def refresh_all():
    curses.update_lines_cols()
    for (win, draw) in windows:
        win.clear()
        if draw != None:
            draw(win, gamestate)
        win.refresh()

def get_sentence(screen):
    usrinput = screen.getstr(int((DIV-1)*curses.LINES/DIV + (curses.LINES/(DIV*2) - RING)), int(curses.COLS/2 - MAX_WORD/2), MAX_WORD)
    usrinput = usrinput.decode(encoding="utf-8")
    usrinput = usrinput.lower()
    usrinput = usrinput.split(" ")
    return usrinput

def config_curses(main_screen):
    curses.echo()
    curses.nocbreak()
    curses.use_default_colors()
    main_screen.keypad(False)

def main(screen):
    config_curses(screen)

    wordswin = curses.newwin(int((DIV-1)*curses.LINES/DIV - RING),  int(curses.COLS/DIV) - RING,            RING,                           int((DIV-1)*curses.COLS/DIV))
    inputwin = curses.newwin(int(curses.LINES/DIV - RING),          int(curses.COLS - 2*RING),              int((DIV-1)*curses.LINES/DIV),  RING)
    stackwin = curses.newwin(int((DIV-1)*curses.LINES/DIV - RING),  int((DIV-1)*curses.COLS/DIV - RING),    RING,                           RING)

    windows.append((screen, None))
    windows.append((wordswin, draw_wordswin))
    windows.append((inputwin, draw_inputwin))
    windows.append((stackwin, draw_stackwin))

    refresh_all()

    while True:
        refresh_all()
        sentence = get_sentence(screen)
        apply_sentence(sentence, gamestate)

curses.wrapper(main)
