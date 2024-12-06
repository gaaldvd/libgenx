"""
LibGenX CLI script.
"""

import sys

from colorama import Style
from libgentools import SearchRequest
from libgenx_common import get_query_arg


def main():
    """Main function of the LibGenX CLI script."""
    print(Style.BRIGHT + "\nWelcome to LibGenX!" + Style.RESET_ALL)
    query = get_query_arg()

    # main loop
    while True:
        if not query:
            query = input("Enter search query: ")
        request = SearchRequest(query)
        print(f"\n{Style.BRIGHT}Search query: {Style.RESET_ALL}{query}")
        print(f"{Style.BRIGHT}Results: {Style.RESET_ALL}"
              f"{len(request.results)}")

        while True:
            c = input("\nFilter results, new search or quit [f/s/q]: ").lower()
            match c:
                # filter results
                case "f":  # TODO filter results
                    print("filter...")
                    continue
                # new search
                case "s":
                    query = None
                    break
                # close application
                case "q":
                    sys.exit(f"\n{Style.BRIGHT}Goodbye!{Style.RESET_ALL}")
                # invalid command
                case _:
                    print("Available commands: [f]ilter, [s]earch, [q]uit!")
                    continue


if __name__ == '__main__':
    main()
