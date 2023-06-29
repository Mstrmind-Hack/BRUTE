from resources import *
from simple_term_menu import TerminalMenu
from modules.wordlist_menu import wordlist_menu
from modules.wordlist_Mainmenu_view import wordlist_menu_view, view
import subprocess
from pathlib import Path


def show_custom_wordlist():
    """
    Displays Custom Wordlists In The /../Custom_Wordlist Folder/
    """

    show_custom_wordlist.path = "wordlists/custom_wordlists/"
    show_custom_wordlist.directory_list = os.listdir(show_custom_wordlist.path)

    if show_custom_wordlist.directory_list:
        lines_wordlists()
        print(
            "\n [bold][yellow]Here Are The Current Custom Wordlists: [/yellow][/bold]"
        )

        for wordlist in show_custom_wordlist.directory_list:
            print(
                f"\n [bright_magenta]*[/bright_magenta] [bold][cyan] {wordlist}[/cyan][/bold]"
            )
        lines_wordlists()


def the_path():
    """
    Displays Path Where Custom Wordlists Exist,
    It also accounts for 'drag and drop' when user
    drags and drops the folder in the terminal.
    It also accounts for user manual input of the
    path of directory.
    This function makes sure the path is always
    displayed and used correctly no matter the
    input method used
    """
    os.system("clear")

    brute_banner()
    lines()

    the_path.path2 = os.getcwd()
    show_custom_wordlist()

    print(
        "\n [bold][yellow][[red]TIP 1[/red]][/yellow] [purple]Enter [cyan]PATH[/cyan] Where Your Custom Wordlist Resides: [cyan]/Path/../[/cyan][/purple][/bold]"
    )
    print(
        "\n [bold][yellow][[red]TIP 2[/red]][/yellow] [purple]OR Drag and Drop [cyan]THE FOLDER[/cyan] Containing The Wordlist File.[/purple][/bold]"
    )
    print(
        "\n [bold][yellow][[red]NOTE [/red]][/yellow] [purple]IF YOU HAVE MANY WORDLISTS JUST PASTE THEM IN[/purple][/bold]"
    )
    print(
        "\t [bold][purple][cyan]/Brute/wordlists/custom_wordlists/ [/cyan]Folder [/purple][/bold]"
    )

    lines()

    BRUTE_CUSTOM_WORDLIST_PATH()
    cp_path = input("")

    if cp_path[0] and cp_path[-1] != "/":
        the_path.CP_PATH = f"{cp_path}"

        if "'" in the_path.CP_PATH:
            the_path.CP_PATH = the_path.CP_PATH.replace("'", "", 2)
            the_path.CP_PATH = the_path.CP_PATH.replace(" ", "", 1)
            the_path.CP_PATH = f"{the_path.CP_PATH}/"

            print(
                f"\n [bold][red]Path: [sky_blue2][blink]{the_path.CP_PATH}[/blink][/sky_blue2] [/red][/bold]"
            )
            lines()

        else:
            if the_path.CP_PATH[0] == "/":
                the_path.CP_PATH = f"{cp_path}/"

            else:
                the_path.CP_PATH = f"/{cp_path}/"

    elif cp_path[0] != "/":
        the_path.CP_PATH = f"/{cp_path}"

    elif cp_path[-1] != "/":
        the_path.CP_PATH = f"{cp_path}/"

    elif cp_path[0] and cp_path[-1] == "/":
        the_path.CP_PATH = f"{cp_path}"

    else:
        the_path.CP_PATH = f"{cp_path}/"

    os.system("clear")
    brute_banner()

    print(
        f"\n [bold][red]Path: [sky_blue2][blink]{the_path.CP_PATH}[/blink][/sky_blue2] [/red][/bold]"
    )
    lines()


def the_path_remove():
    """
    This function captures the path where BRUTE
    folder resides in the user system. It makes sure
    that no matter the location where /BRUTE/ folder is,
    it can always find the Custom wordlist folder
    to Remove the files.
    """

    the_path_remove.path3 = os.getcwd()

    os.system("clear")

    brute_banner()
    show_custom_wordlist()

    if show_custom_wordlist.directory_list:
        # lines()
        print(
            "\n [bold][yellow][[blink][red]*[/red][/blink]][/yellow] [purple]Enter [sky_blue2]FILE NAME WITH EXTENSION I.E Name.txt[/sky_blue2][/purple][/bold]"
        )

        BRUTE_CUSTOM_WORDLIST_ERASE()

        the_path_remove.rm_filename = input("")
        the_path_remove.is_File_present = os.path.isfile(
            f"{the_path_remove.path3}/wordlists/custom_wordlists/{the_path_remove.rm_filename}"
        )

    else:
        lines()
        print(f"\n [bold][red]It Looks Like There Are No Custom Wordlists[/red][/bold]")
        lines()

        note()
        run_again()


def modify_wordlist():
    """
    Menu that allows for adding and removing wordlists
    """

    try:
        modify_wordlist.options3 = [
            "View Included Wordlists",
            "Add Wordlist",
            "Remove Wordlist",
        ]
        modify_wordlist.terminal_menu3 = TerminalMenu(
            modify_wordlist.options3,
            title="",
            menu_cursor=" >> ",
            menu_cursor_style=("fg_red", "bold"),
            menu_highlight_style=("fg_yellow", "underline", "italics", "bold"),
        )
        modify_wordlist.menu3_entry_index = modify_wordlist.terminal_menu3.show()

        if (
            modify_wordlist.options3[modify_wordlist.menu3_entry_index]
            == "View Included Wordlists"
        ):
            path = "wordlists/"
            directory_list = os.listdir(path)
            view(path)
            # os.system("clear")
            wordlist_menu_view()

        if (
            modify_wordlist.options3[modify_wordlist.menu3_entry_index]
            == "Add Wordlist"
        ):
            the_path()
            show_custom_wordlist()

            print(
                "\n [bold][yellow][[blink][red]*[/red][/blink]][/yellow] [purple]MANUALLY Enter [sky_blue2]FILE NAME WITH EXTENSION I.E Name.txt[/sky_blue2][/purple][/bold]"
            )
            print(
                "  [bold][purple]   Where your Current Wordlist Resides:[/purple][/bold]"
            )
            lines()

            BRUTE_CUSTOM_WORDLIST()

            the_path.cp_filename = input("")

            the_path.is_File_present = os.path.isfile(
                f"{the_path.CP_PATH}{the_path.cp_filename}"
            )

            print(the_path.is_File_present)

            if the_path.is_File_present:
                os.system("clear")
                brute_banner()
                subprocess.run(
                    [
                        "cp",
                        f"{the_path.CP_PATH}{the_path.cp_filename}",
                        f"{the_path.path2}/wordlists/custom_wordlists/{the_path.cp_filename}",
                    ]
                )

                os.system("clear")

                brute_banner()
                show_custom_wordlist()

                print(
                    f"\n [bold][medium_spring_green]SUCCESS![sky_blue2] Wordlist {the_path.cp_filename}[/sky_blue2] Added [/medium_spring_green][/bold]"
                )

            else:
                os.system("clear")

                brute_banner()
                show_custom_wordlist()

                print(
                    f"\n [bold][red]It Looks Like [sky_blue2]{the_path.cp_filename}[/sky_blue2] OR [sky_blue2]{the_path.CP_PATH}[/sky_blue2] Does Not Exist, Check Spelling And Try Again.[/red][/bold]"
                )

            run_again()

        if (
            modify_wordlist.options3[modify_wordlist.menu3_entry_index]
            == "Remove Wordlist"
        ):
            the_path_remove()

            if the_path_remove.is_File_present:
                subprocess.run(
                    [
                        "rm",
                        f"{the_path_remove.path3}/wordlists/custom_wordlists/{the_path_remove.rm_filename}",
                    ]
                )

                os.system("clear")

                brute_banner()
                show_custom_wordlist()

                print(
                    f"\n [bold][medium_spring_green]SUCCESS![sky_blue2] Wordlist {the_path_remove.rm_filename}[/sky_blue2] Removed [/medium_spring_green][/bold]"
                )

            else:
                os.system("clear")

                brute_banner()
                show_custom_wordlist()

                print(
                    f"\n [bold][red]It Looks Like [sky_blue2]{the_path_remove.rm_filename}[/sky_blue2] Does Not Exist. Check Spelling And Try Again.[/red][/bold]"
                )

            run_again()

    except TypeError:
        os.system("clear")

        brute_banner()
        print(f"\n[bold][red] Command Not Understood [/red][/bold]")
        run_again()
