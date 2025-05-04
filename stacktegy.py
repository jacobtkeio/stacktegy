import curses

from sentence import *
from words_window import *
from input_window import *
from stack_window import *

stack1 = []
stack2 = []
stack3 = []
stack4 = []

windows = []

DIV = 5
RING = 2
MAX_WORD = 20

def refresh_all():
    curses.update_lines_cols()

    for (win, draw) in windows:
        win.clear()
        if draw != None:
            draw(win)
        win.refresh()

def main(screen):
    screen.keypad(False)

    curses.echo()
    curses.nocbreak()
    curses.use_default_colors()

    wordswin = curses.newwin(int((DIV-1)*curses.LINES/DIV - RING),  int(curses.COLS/DIV) - RING,            RING,                           int((DIV-1)*curses.COLS/DIV))
    inputwin = curses.newwin(int(curses.LINES/DIV - RING),          int(curses.COLS - 2*RING),              int((DIV-1)*curses.LINES/DIV),  RING)
    stackwin = curses.newwin(int((DIV-1)*curses.LINES/DIV - RING),  int((DIV-1)*curses.COLS/DIV - RING),    RING,                           RING)

    windows.append((screen, None))
    windows.append((wordswin, draw_wordswin))
    windows.append((inputwin, draw_inputwin))
    windows.append((stackwin, draw_stackwin))

    refresh_all()

    while True:
        usrinput = screen.getstr(int((DIV-1)*curses.LINES/DIV + (curses.LINES/(DIV*2) - RING)), int(curses.COLS/2 - MAX_WORD/2), MAX_WORD)
        usrinput = usrinput.decode(encoding="utf-8")
        refresh_all()
        read_sentence(usrinput)

curses.wrapper(main)
