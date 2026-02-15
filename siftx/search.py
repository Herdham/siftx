import sys
from .files import open_file
from colorama import Back, Fore, Style
from .highlight import highlight


def search_command(command):
    #if command["search"].startswith("search:"):
        word = command["search"]
        if len(word) != 0:
            search_file(word, command["file"], command["number_line"], 
                        command["invert"], command["ignore_case"], command["counter"])
        else:
            print(Fore.RED, command["usage"])
    #else:
        #print(Fore.RED, command["usage"])



def count_word(word:list, pattern:str):
    for eachword in word:
        if eachword.startswith(pattern[0]) and eachword.endswith(pattern[len(pattern) - 1]):
            return word.count(eachword)
        


def search_file(pattern:str, file, number_line, invert, ignore_case, counter):
    if open_file(file):
        with open(file, "r", errors="ignore") as output:
            
            first_case = pattern[0].lower() + pattern[1:]
            second_case = pattern[0].upper() + pattern[1:]
            counts = 0

            for line, word in enumerate(output, 1):
                if pattern in word.strip().split(" ") and number_line:
                    # change = find_word(word.strip().split(" "), pattern)
                    # word.strip().split(" ")[change].upper()
                    print(line, word, end="", sep=": ")
                elif pattern in word.strip().split(" ") and not invert and not counter:
                    highlight(word, pattern)
                else:
                    if invert and not pattern in word.strip().split(" "):
                        print(word, end="")
                    elif ignore_case:
                        if first_case in word.strip().split(" ") or second_case in word.strip().split(" "):
                            print("-i:", word, end="")
                    elif counter and pattern in word.strip().split(" "):
                        counts += count_word(word.strip().split(" "), pattern)
                        print(counts)
                    continue
            
                    
    else:
        print("File doest not exit")