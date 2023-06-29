from resources import *
from simple_term_menu import TerminalMenu


def verbose_menu3():
    verbose_menu3.options3 = ["Show Results Only", "Verbose"]
    verbose_menu3.terminal_menu3 = TerminalMenu(
        verbose_menu3.options3,
        title="",
        menu_cursor=" >> ",
        menu_cursor_style=("fg_red", "bold"),
        menu_highlight_style=("fg_yellow", "underline", "italics", "bold"),
    )
    verbose_menu3.menu3_entry_index = verbose_menu3.terminal_menu3.show()
