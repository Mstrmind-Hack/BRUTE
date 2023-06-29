from resources import *
from simple_term_menu import TerminalMenu


def title():
    """
    Displays Border Around Options Menu
    """

    print("\n")

    table0 = Table(
        title=f"",
        show_header=False,
        header_style="bold orange3",
        show_lines=False,
        min_width=1,
        expand=True,
        box=box.DOUBLE_EDGE,
        border_style=f"cyan",
        title_justify="left",
    )

    table0.add_row(
        f"[orange][bold]Select From The Options Below[/orange][/bold]",
        style="bold purple",
    )

    print(table0)


def run_again():
    """
    Menu which allows users to either
    run the tool again, or exit the tool.
    To run the tool again, it executes
    <python3 Brute.py> command
    """

    try:
        title()

        table_ra = Table(
            title=f"",
            show_header=False,
            header_style="bold orange3",
            show_lines=False,
            min_width=1,
            expand=True,
            box=box.DOUBLE_EDGE,
            border_style=f"cyan",
            title_justify="left",
        )

        table_ra.add_row(
            f"[orange][bold]Select From The Options Below[/orange][/bold]",
            style="bold purple",
        )

        run_again.options = ["Main Menu", "Exit"]

        run_again.terminal_menu2 = TerminalMenu(
            run_again.options,
            title="",
            menu_cursor=" >> ",
            menu_cursor_style=("fg_red", "bold"),
            menu_highlight_style=("fg_yellow", "underline", "italics", "bold"),
        )

        run_again.menu_entry_index = run_again.terminal_menu2.show()

        if run_again.options[run_again.menu_entry_index] == "Main Menu":
            import subprocess

            subprocess.run(["python3", "Brute.py"])

        if run_again.options[run_again.menu_entry_index] == "Exit":
            print(
                f"\n[bold][red] [!] Warning, Exiting Will Clear The Screen[/red][/bold]"
            )
            print(f"[bold][red]    Are You Sure You Want To Exit?[/red][/bold]")

            def terminate():
                """
                Menu asks the user if they wish to terminate.
                If they termitate it offers:
                1) To exit and clear the screen
                OR
                2) Exit and do not clear the screen
                """

                terminate.options = [
                    "Yes Exit And Clear The Screen",
                    "Exit But Do Not Clear The Screen",
                ]
                terminate.terminal_menu3 = TerminalMenu(
                    terminate.options,
                    title="",
                    menu_cursor=" >> ",
                    menu_cursor_style=("fg_red", "bold"),
                    menu_highlight_style=("fg_yellow", "underline", "italics", "bold"),
                )

                terminate.menu_entry_index = terminate.terminal_menu3.show()
                if (
                    terminate.options[terminate.menu_entry_index]
                    == "Yes Exit And Clear The Screen"
                ):
                    print(f"\n[bold][green] Exiting...[/green][/bold]")
                    time.sleep(3)
                    os.system("clear")
                    exit()

                if (
                    terminate.options[terminate.menu_entry_index]
                    == "Exit But Do Not Clear The Screen"
                ):
                    print(f"\n[bold][green] Exiting...[/green][/bold]")
                    exit()

            terminate()

    except TypeError:
        os.system("clear")
        brute_banner()
        print(f"\n[bold][red] Command Not Understood [/red][/bold]")
        run_again()
