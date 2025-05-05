import curses

MAX_WORD = 20

def draw_inputwin(inputwin, gamestate):
    inputwin.box('#', '#')

def get_sentence(screen, window):
    (y, x) = window.getyx()
    (lines, cols) = window.getmaxyx()
    usrinput = window.getstr(y + lines//2, x + cols//2 - MAX_WORD//2, MAX_WORD)
    usrinput = usrinput.decode(encoding="utf-8")
    usrinput = usrinput.lower()
    usrinput = usrinput.split(" ")
    return usrinput

