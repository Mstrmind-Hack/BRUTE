from resources import *
import requests
from requests.exceptions import *
from modules.wordlist_menu import *
from modules.run_menu import run_menu

os.system("clear")
brute_banner()
directory_banner()

print(
    "\n [bold][yellow][[blink][red]*[/red][/blink]][/yellow] [purple]Enter [sky_blue2]URL[/sky_blue2] Or [sky_blue2]IP[/sky_blue2] Address[/purple][/bold]"
)

lines()
BRUTE_URL()

url = input("")

os.system("clear")

brute_banner()
directory_banner()
seconds()
lines()
BRUTE_TIME()

space = " " * 1
space2 = " " * 2
space3 = " " * 3
space4 = " " * 4
space5 = " " * 5
space6 = " " * 6
space7 = " " * 7

speed = input()


def speed_force():
    """
    Displays the wait time between each word
    """

    print(
        f"\n\t[bold][sky_blue2] TIME BETWEEN WORDS: [gold1]{speed}[/gold1] Seconds[/sky_blue2][/bold]"
    )


try:
    value = int(speed)

    os.system("clear")

    brute_banner()
    directory_banner()
    speed_force()
    lines()

    print(
        "\n [bold][yellow][[blink][red]*[/red][/blink]][/yellow] [sky_blue2]Select Wordlist[/sky_blue2][/bold]"
    )

    wordlist_menu()

    os.system("clear")

    brute_banner()
    directory_banner()

    file = open(f"{wordlist_menu.fileName}", "r")
    file.readline()

    if "http" in url:
        URL = url

    if "https" in url:
        URL = url

    if "http" not in url:
        URL = f"http://{url}"

    if URL[-1] == "/":
        URL1 = URL
        print(
            f"\n\t[bold][sky_blue2] BRUTEFORCING: [gold1]{URL1}[/gold1][/sky_blue2][/bold]"
        )

    if URL[-1] != "/":
        URL1 = f"{URL}/"
        print(
            f"\n\t[bold][sky_blue2] BRUTEFORCING: [gold1]{URL1}[/gold1][/sky_blue2][/bold]"
        )
    speed_force()
    lines()

    def request_brains():
        run_menu()

        print(f"\n[bold][magenta2] COMMON HTML  ERROR CODES[/magenta2][/bold]")
        print(
            f"[bold][medium_spring_green]  [200] [/medium_spring_green][light_salmon3] OK [/light_salmon3][magenta2] [/magenta2][/bold]"
        )
        print(
            f"[bold][bright_yellow]  [301] [/bright_yellow][light_salmon3] MOVED PERMANENTLY[/light_salmon3][magenta2] [/magenta2][/bold]"
        )
        print(
            f"[bold][bright_yellow]  [302] [/bright_yellow][light_salmon3] MOVED TEMPORARILY[/light_salmon3][magenta2] [/magenta2][/bold]"
        )

        print(
            f"[bold][cyan]  [400] [/cyan][light_salmon3] BAD REQUEST[/light_salmon3][magenta2] [/magenta2][/bold]"
        )
        print(
            f"[bold][cyan]  [404] [/cyan][light_salmon3] NOT FOUND[/light_salmon3][magenta2] [/magenta2][/bold]"
        )
        print("\n")

        print(
            "[bold][cyan] +-------+---------------+------------+-------------------------------+[/cyan][/bold]"
        )
        print(
            "[bold][cyan] |  [magenta]CODE[/magenta] |   [magenta]DIRECTORY[/magenta]   |    [magenta]SIZE[/magenta]    |          [magenta]REDIRECT[/magenta]             |[/cyan][/bold]"
        )
        print(
            "[bold][cyan] +-------+---------------+------------+-------------------------------+[/cyan][/bold]"
        )
        for request_brains.word in file:

            def request_codes():
                request_brains.word = request_brains.word.strip()
                supplied_url = f"{URL1}{request_brains.word}"
                headers = {"User-Agent": "Chromium"}

                # Other user Angents can be used. 'Google Chrome' or 'Chromium' works

                response = requests.get(supplied_url, headers=headers)
                res = response.history
                the_length = len(response.content)
                the_code = response.status_code
                the_url = response.url
                console = Console()

                if res:
                    for redirect in response.history:
                        the_length = len(redirect.content)
                        the_code = redirect.status_code
                        redirected_url = redirect.url
                        code = str(redirect.status_code)
                        res_len = str(the_length)
                        res_word = str(request_brains.word)

                        print(" [bold][cyan]|", end="")
                        print(
                            f"[bold][bright_yellow]{space}{code:^5s}[/bright_yellow][/bold]",
                            end="",
                        )
                        print(f"{space}[bold][cyan]|", end="")
                        print(
                            f"{space2}[bold][bright_yellow]/{res_word:10s}[/bright_yellow][/bold]",
                            end="",
                        )
                        print(f"{space2}[bold][cyan]|", end="")
                        print(f"{space4}[bold][sky_blue1]{res_len:8s}", end="")
                        print("[bold][cyan]|", end="")
                        print(f"{space2}[bold][medium_spring_green]{response.url:^15s}")

                else:
                    if response.status_code == 200:
                        code = str(response.status_code)
                        res_len = str(the_length)
                        res_word = str(request_brains.word)

                        print(" [bold][cyan]|", end="")

                        print(
                            f"[bold][medium_spring_green]{space}{code:^5s}[/medium_spring_green][/bold]",
                            end="",
                        )
                        print(f"{space}[bold][cyan]|", end="")
                        print(
                            f"{space2}[bold][medium_spring_green]/{res_word:10s}[/medium_spring_green][/bold]",
                            end="",
                        )
                        print(f"{space2}[bold][cyan]|", end="")
                        print(f"{space4}[bold][sky_blue1]{res_len:8s}", end="")
                        print("[bold][cyan]|", end="")
                        print(f"{space4}{space:^15s}")

            if run_menu.options3[run_menu.menu3_entry_index] == "RUN":
                request_codes()

    request_brains()
    run_again()

except ConnectionError:
    print(
        "\n[bold][red] Connection Timed out, Check Spelling And Try Again[/red][/bold]"
    )
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
