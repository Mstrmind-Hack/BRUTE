from resources import *


def brute_banner():
    """
    Displays the banner of the tool.
    This function is messy but it works!
    """

    print("\n[magenta] ██████  ██████  ██    ██ ████████ ███████[/magenta] ")
    print(
        "[bold][blue_violet] ██   ██ ██   ██ ██    ██    ██    ██[/blue_violet][/bold]"
    )
    print(" [cyan]██████  ██████  ██    ██    ██    █████[/cyan]")
    print(
        "[bold][blue_violet] ██   ██ ██   ██ ██    ██    ██    ██[/blue_violet][/bold]"
    )
    print(
        "[bold][blue_violet] ██████  ██   ██  ██████     ██    ███████[/blue_violet][/bold]"
    )

    print(
        f"\n [bold][medium_spring_green]Tool Created By: [purple]@Mstrmind.hack[/purple] [Instagram][/medium_spring_green][/bold]"
    )
    print(
        f"\n[bold][dark_sea_green2] Version: [purple]1.0[/purple] [/dark_sea_green2][/bold]"
    )


def main_menu():
    """
    Funtion displays on CLI that the user is currently
    on the main menu
    """

    print(f"\n[bold][orange_red1] --------- MAIN MENU --------- [/orange_red1][/bold]")


def wlist_menu():
    """
    Function displays on the CLI that the user is using
    the wordlist menu
    """

    print(
        f"\n[bold][orange_red1] --------- WORDLIST MENU --------- [/orange_red1][/bold]"
    )


def directory_banner():
    """
    Lets the user know that they are bruteforcing directories
    """

    print(
        f"\n[bold][orange_red1] --------- DIRECTORY BRUTEFORCING --------- [/orange_red1][/bold]"
    )


def run():
    """
    Run Menu for verbosity
    """

    print(
        f"\n[bold][orange_red1] [blink]RUN MENU[/blink] Select An Option [/orange_red1][/bold]"
    )


def lines():
    """
    Division/separator line
    """

    print(
        f"\n[bold][orange_red1] ------------------------------------------ [/orange_red1][/bold]"
    )


def lines_wordlists():
    """
    Division/separator line for wordlists
    """

    print(f"\n[bold][green] ------------------------------------------ [/green][/bold]")


def subdomain_banner():
    """
    Lets users know they are bruteforcing target subdomains
    """

    print(
        f"\n[bold][orange_red1] --------- SUBDOMAIN BRUTEFORCING --------- [/orange_red1] [/bold]"
    )
