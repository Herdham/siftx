import sys
from argparse import ArgumentParser
from .output import optional
from .search import search_command
import colorama
from colorama import Back, Fore, Style


def main():
    parser = ArgumentParser(description="Siftx is a command line interface")
    parser.usage = f"{Fore.RED} siftx [search:text] [path] [options] {Style.RESET_ALL}"

    group = parser.add_mutually_exclusive_group()
    
    parser.add_argument("search", help="search command helps in search through a text")

    parser.add_argument("file", help="file to search through")

    parser.add_argument("-n", "--number_line", 
                        help="for print number line of where text exits", action="store_true")
    
    group.add_argument("-v", "--invert",
                        help="indirect printing", action="store_true")
    
    parser.add_argument("-i", "--ignore_case",
                        help="printing without checking weather it's case_sensitive or not", 
                        action="store_true")
    
    group.add_argument("-c", "--counter", 
                       help="count the number of time word occure in the text", 
                       action="store_true")
    
    
    result = parser.parse_args()
    # commands = {"search": result.search, "usage": parser.usage, "file":result.file, 
    #             "line_number": result.number_line, "invert": result.invert, 
    #             "ignorecase" : result.ignore_case, "counter" : result.counter}
    
    commands = vars(result)
    if commands:
        search_command(commands)

    



    

if __name__ == "__main__":
    main()