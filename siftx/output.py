from colorama import Back, Fore, Style

def optional():
    print("""
        siftx [search:text] [path] [options]

        Options:
            -r          recursice
            -i          ignore case
            -n          line numbers
            -c          context lines
            --ast       python-aware parsing
            --django    django intelligence
            --json      machine-readable output
    """)