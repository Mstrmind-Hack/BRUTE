from resources import *
from simple_term_menu import TerminalMenu
from modules.run_again import run_again


def view(path):
    os.system("clear")

    brute_banner()

    # path = ""
    directory_list = os.listdir(path)

    if directory_list:
        lines_wordlists()
        print("\n [bold][yellow]Here Are The Current Wordlists: [/yellow][/bold]")

        for wordlist in directory_list:
            print(
                f"\n [bright_magenta]*[/bright_magenta] [bold][cyan] {wordlist}[/cyan][/bold]"
            )
        lines_wordlists()

    else:
        lines()
        print("\n[bold][red] No Custom Wordlists To Show =( [/red][/bold]")
        lines()
        note()
        run_again()


def wordlist_menu_view():
    """
    This menu only displays all the current
    wordlists included in the tool
    when viewing them from the main menu
    """

    wordlist_menu_view.options2 = [
        "View All Custom Wordlist",
    ]
    wordlist_menu_view.terminal_menu2 = TerminalMenu(
        wordlist_menu_view.options2,
        title="",
        menu_cursor=" >> ",
        menu_cursor_style=("fg_red", "bold"),
        menu_highlight_style=("fg_yellow", "underline", "italics", "bold"),
    )
    wordlist_menu_view.menu2_entry_index = wordlist_menu_view.terminal_menu2.show()

    if (
        wordlist_menu_view.options2[wordlist_menu_view.menu2_entry_index]
        == "View All Custom Wordlist"
    ):
        os.system("clear")

        brute_banner()
        path = "wordlists/custom_wordlists/"
        directory_list = os.listdir(path)

        view(path)
