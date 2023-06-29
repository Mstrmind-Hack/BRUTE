from resources import *
from simple_term_menu import TerminalMenu
from modules.run_again import run_again


def wordlist_menu():
    wordlist_menu.options2 = [
        "Directory-List-1.0",
        "Directory List Small 2.3",
        "Directory List Medium 2.3",
        "Directory List Medium 2.3 Edited",
        "SecList-subdomains-top1million-5000",
        "SecList-subdomains-top1million-20000",
        "Use A Custom Wordlist",
    ]

    wordlist_menu.terminal_menu2 = TerminalMenu(
        wordlist_menu.options2,
        title="",
        menu_cursor=" >> ",
        menu_cursor_style=("fg_red", "bold"),
        menu_highlight_style=("fg_yellow", "underline", "italics", "bold"),
    )

    wordlist_menu.menu2_entry_index = wordlist_menu.terminal_menu2.show()
    if wordlist_menu.options2[wordlist_menu.menu2_entry_index] == "Directory-List-1.0":
        wordlist_menu.fileName = "wordlists/directory-list-1.0.txt"

    if (
        wordlist_menu.options2[wordlist_menu.menu2_entry_index]
        == "Directory List Small 2.3"
    ):
        wordlist_menu.fileName = "wordlists/directory-list-2.3-small.txt"

    if (
        wordlist_menu.options2[wordlist_menu.menu2_entry_index]
        == "Directory List Medium 2.3"
    ):
        wordlist_menu.fileName = "wordlists/directory-list-2.3-medium.txt"

    if (
        wordlist_menu.options2[wordlist_menu.menu2_entry_index]
        == "Directory List Medium 2.3 Edited"
    ):
        wordlist_menu.fileName = "wordlists/directory_medium_edited.txt"

    if (
        wordlist_menu.options2[wordlist_menu.menu2_entry_index]
        == "SecList-subdomains-top1million-5000"
    ):
        wordlist_menu.fileName = "wordlists/SecList-subdomains-top1million-5000.txt"
    if (
        wordlist_menu.options2[wordlist_menu.menu2_entry_index]
        == "SecList-subdomains-top1million-20000"
    ):
        wordlist_menu.fileName = "wordlists/SecList-subdomains-top1million-20000.txt"
    if (
        wordlist_menu.options2[wordlist_menu.menu2_entry_index]
        == "Use A Custom Wordlist"
    ):
        os.system("clear")

        brute_banner()

        path = "wordlists/custom_wordlists/"
        directory_list = os.listdir(path)

        if directory_list:
            lines_wordlists()

            print(
                "\n [bold][yellow]Here Are The Current Custom Wordlists: [/yellow][/bold]"
            )

            for wordlist in directory_list:
                print(
                    f"\n [bright_magenta]*[/bright_magenta] [bold][cyan] {wordlist}[/cyan][/bold]"
                )
            lines_wordlists()

            print(
                "\n [bold][yellow][[blink][red]*[/red][/blink]][/yellow] [purple]MANUALLY Enter [sky_blue2]FILE NAME WITH EXTENSION I.E Name.txt[/sky_blue2][/purple][/bold]"
            )
            print(
                "  [bold][purple]   Where your Current Wordlist Resides:[/purple][/bold]"
            )

            BRUTE_CUSTOM_WORDLIST()

            myfilename = input("")
            wordlist_menu.fileName = f"wordlists/custom_wordlists/{myfilename}"

        else:
            lines()
            print(
                "\n [bold][red] =( It Looks Like You Have Not Added Any Custom Wordlists.. [/red][/bold]"
            )
            lines()
            note()
            run_again()
