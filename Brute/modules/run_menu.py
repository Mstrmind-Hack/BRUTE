from resources import *
from simple_term_menu import TerminalMenu


def run_menu():
    run_menu.options3 = ["RUN"]
    run_menu.terminal_menu3 = TerminalMenu(
        run_menu.options3,
        title="",
        menu_cursor=" >> ",
        menu_cursor_style=("fg_red", "bold"),
        menu_highlight_style=("fg_yellow", "underline", "italics", "bold"),
    )
    run_menu.menu3_entry_index = run_menu.terminal_menu3.show()
