from resources import *
import requests
from requests.exceptions import *
from modules.wordlist_menu import *
from modules.verbose_menu import verbose_menu3


os.system("clear")
brute_banner()
subdomain_banner()

print(
    "\n [bold][yellow][[blink][red]*[/red][/blink]][/yellow] [purple]Enter [sky_blue2]Domain Name[/sky_blue2] I.E [sky_blue2]Address.com[/sky_blue2]  [/purple][/bold]"
)

lines()
BRUTE_SUBS()

url = input("")

if "www." in url:
    url = url.replace("www.", "", 1)


def brute_force():
    print(
        f"\n\t[bold][sky_blue2] BRUTEFORCING: [gold1]{url}[/gold1][/sky_blue2][/bold]"
    )


os.system("clear")

brute_banner()
subdomain_banner()
brute_force()
lines()

seconds()
BRUTE_TIME()
speed = input()


def speed_force():
    print(
        f"\n\t[bold][sky_blue2] TIME BETWEEN WORDS: [gold1]{speed}[/gold1] Seconds[/sky_blue2][/bold]"
    )


speed_force()

try:
    brute_force()

    value = int(speed)

    os.system("clear")

    brute_banner()
    subdomain_banner()
    brute_force()
    speed_force()
    lines()

    print(
        "\n [bold][yellow][[blink][red]*[/red][/blink]][/yellow] [sky_blue2]Select Wordlist[/sky_blue2][/bold]"
    )

    wordlist_menu()

    os.system("clear")

    brute_banner()
    subdomain_banner()
    brute_force()
    speed_force()
    lines()

    file = open(f"{wordlist_menu.fileName}", "r")
    file.readline()

    def verbose():
        """
        This Function Shows All Requests Sent For Each
        Dictionary Subdomain Word
        """

        print("\n")

        for word in file:
            word = word.strip()

            print(
                f"\t[bold][light_slate_blue]Testing: [/light_slate_blue] [light_salmon3]https://{word}.{url}[/light_salmon3][/bold]"
            )

            try:
                res = requests.get(f"https://{word}.{url}")
                print(
                    f"\n[green_yellow]  [!][/green_yellow][magenta2][bold] https://{word}.{url}[/bold][/magenta2]\n"
                )

            except requests.ConnectionError:
                pass
            time.sleep(int(value))

    def Results_only():
        """
        This Funtion Shows Only The Subdomains Found
        """

        print("\n")
        for word in file:
            word = word.strip()

            try:
                res = requests.get(f"https://{word}.{url}")
                print(
                    f"[green_yellow]  [!][/green_yellow][magenta2][bold] https://{word}.{url}[/bold][/magenta2]"
                )
            except requests.ConnectionError:
                pass
            time.sleep(int(value))

    verbose_menu3()

    if verbose_menu3.options3[verbose_menu3.menu3_entry_index] == "Show Results Only":
        Results_only()

    if verbose_menu3.options3[verbose_menu3.menu3_entry_index] == "Verbose":
        verbose()
    run_again()


except KeyboardInterrupt:
    print("\n[bold][red] Stopping Scan [/red][/bold]")
    time.sleep(2)
    run_again()

except TypeError:
    os.system("clear")
    brute_banner()
    print(f"\n[bold][red] Command Not Understood [/red][/bold]")
    run_again()

except:
    print(" \n[bold][red] Not A Valid Input![/red][/bold]")
    run_again()
