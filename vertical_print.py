import curses

def vertical_print(y, x, spaces, window, list):
    offset = 0
    for item in list:
        window.addstr(y+offset, x, str(item).rjust(2))
        offset += spaces
