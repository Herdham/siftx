import colorama
from colorama import Fore, Back, Style


def highlight(word:str, pattern:str):
    result = word.replace(pattern, f"{Fore.RED}{pattern}{Style.RESET_ALL}")
    print("->", result, end="")