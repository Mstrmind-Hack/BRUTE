import sys
import os
import time
from time import sleep
import requests
from rich.console import Console
from rich import print
from rich.syntax import Syntax
from rich.table import Table, Column
from rich import box
from rich.layout import Layout
from rich.live import Live
from rich.table import Table
from rich.progress import track
from modules.brute_banner import *
from modules.run_again import run_again


def BRUTE():
    print(
        "\n [bold][cyan] [[deep_pink1]BRUTE[/deep_pink1]][/cyan][blink][red]>> [/red][/blink] [/bold]",
        end="",
    )


def BRUTE_URL():
    print(
        "\n [bold][cyan] [[deep_pink1]BRUTE[/deep_pink1]][/cyan][cyan][[slate_blue1]URI-URL-IP[/slate_blue1]][/cyan] [blink][red]>> [/red][/blink][/bold]",
        end="",
    )


def BRUTE_SUBS():
    print(
        "\n [bold][cyan] [[deep_pink1]BRUTE[/deep_pink1]][/cyan][cyan][[slate_blue1]DOMAIN NAME[/slate_blue1]][/cyan] [blink][red]>> [/red][/blink][/bold]",
        end="",
    )


def BRUTE_TIME():
    print(
        "\n [bold][cyan] [[deep_pink1]BRUTE[/deep_pink1]][/cyan][cyan][[slate_blue1]Seconds/WORD[/slate_blue1]][/cyan] [blink][red]>> [/red][/blink][/bold]",
        end="",
    )


def BRUTE_CUSTOM_WORDLIST():
    print(
        "\n [bold][cyan] [[deep_pink1]BRUTE[/deep_pink1]][/cyan][cyan][[slate_blue1]Select Custom Wordlist[/slate_blue1]][/cyan] [blink][red]>> [/red][/blink][/bold]",
        end="",
    )


def BRUTE_CUSTOM_WORDLIST_PATH():
    print(
        "\n [bold][cyan] [[deep_pink1]BRUTE[/deep_pink1]][/cyan][cyan][[slate_blue1]SET PATH[/slate_blue1]][/cyan] [blink][red]>> [/red][/blink][/bold]",
        end="",
    )


def BRUTE_CUSTOM_WORDLIST_ERASE():
    print(
        "\n [bold][cyan] [[deep_pink1]BRUTE[/deep_pink1]][/cyan][cyan][[slate_blue1]Erase Wordlist[/slate_blue1]][/cyan] [blink][red]>> [/red][/blink][/bold]",
        end="",
    )


def note():
    print(
        "\n [bold][red]NOTE:[/red] [purple]You Can [sky_blue2]Add/Remove[/sky_blue2] Custom Wordlist Through The [sky_blue2]Main Menu[/sky_blue2].[/purple][/bold]"
    )


def seconds():
    print(
        "\n [bold][yellow][[blink][red]*[/red][/blink]][/yellow] [sky_blue2]Seconds[/sky_blue2] [purple]Between Words? (Type Number [sky_blue2]0[/sky_blue2] for Default)..[/purple][/bold]"
    )
