from resources import *
from simple_term_menu import TerminalMenu
from modules.add_remove_wordlists import modify_wordlist
from modules.about import about

try:
    main_menu()

    def menu():
        """
        Main Menu, Select from all four options
        """

        menu.options = [
            "Directory Scanner",
            "Subdomain Scanner",
            "Wordlists",
            "About And Warnings",
        ]

        terminal_menu = TerminalMenu(
            menu.options,
            title="",
            menu_cursor=" >> ",
            menu_cursor_style=("fg_red", "bold"),
            menu_highlight_style=("fg_yellow", "underline", "italics", "bold"),
        )
        menu.menu_entry_index = terminal_menu.show()

        if menu.options[menu.menu_entry_index] == "Directory Scanner":
            import modules.scanner

        if menu.options[menu.menu_entry_index] == "Subdomain Scanner":
            import modules.subdomain_scanner

        if menu.options[menu.menu_entry_index] == "Wordlists":
            modify_wordlist()
            run_again()

        if menu.options[menu.menu_entry_index] == "About And Warnings":
            about()
            run_again()

    menu()

except KeyboardInterrupt:
    print("\n")
    print("[bold][deep_pink1] Exiting...[/deep_pink1][/bold]")
    time.sleep(2)

except TypeError:
    os.system("clear")
    brute_banner()
    print(f"\n[bold][red] Command Not Understood [/red][/bold]")
    run_again()
