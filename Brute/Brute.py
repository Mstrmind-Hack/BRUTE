from resources import *

os.system("clear")
brute_banner()


try:
    """
    Imports the main menu with all its functions
    """

    from modules.menu import menu

except KeyboardInterrupt:
    os.system("clear")
    print("\n")
    print("[bold][deep_pink1] Exiting...[/deep_pink1][/bold]")
