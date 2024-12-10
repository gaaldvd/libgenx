"""
LibGenX CLI script.
"""

from sys import exit as close
from re import findall
from time import sleep
from colorama import Style, Fore
from libgentools import *
from libgenx_common import get_query_arg
import json  # TEMP


def list_entries(entries):
    """List results."""

    # print header
    print(Style.BRIGHT + "\nNo.".ljust(6)
          + "Author".ljust(24) + "Title".ljust(34)
          + "Year".ljust(5) + "Pages".ljust(9) + "Extension".ljust(10)
          + "ID".ljust(11) + "\n" + "-" * 96 + Style.RESET_ALL)

    # list entries
    for entry, i in zip(entries, range(len(entries))):
        auth = entry['auth']
        title = entry['title']
        year = "" if entry['year'] is None else str(entry['year'])
        pp = "" if entry['pp'] is None else entry['pp']
        ext = entry['ext']
        eid = str(entry['id'])
        print(f"{i + 1:<4}"
              f" {auth[:20] + '...' if len(auth) > 20 else auth:<23}"
              f" {title[:30] + '...' if len(title) > 30 else title:<33}"
              f" {year:<4} {pp[:8]:<8} {ext:<9} {eid:<10}")


def parse_filter_seq(seq):
    """Interpret sequence and return filtering parameters."""

    # filtering mode
    if "-x" in seq:
        mode = "exact"
        seq = seq.replace("-x", "").strip().replace("  ", " ")
    else:
        mode = "partial"

    # translate to the corresponding key-value pairs from libgentools.FILTERS
    matches = findall(r"-(\w) (.*?)(?= -\w|$)", seq)
    filters_raw = {f"-{key}": value.strip() for key, value in matches}

    # validate filters
    filters = {}
    for key, value in filters_raw.items():
        if key in FILTERS:
            filters[FILTERS[key]] = value
        else:
            raise FilterError(f"Invalid filter: {key}")

    return filters, mode


def main():
    """Main function of the LibGenX CLI script."""
    print(Style.BRIGHT + "\nWelcome to LibGenX!" + Style.RESET_ALL)
    tries = 0

    # get query from cli arguments
    query = get_query_arg()

    # TODO get filters from cli arguments

    # DEBUG read from file
    with open("data", "r") as f:
        data = json.load(f)

    # main loop
    while True:

        # get query from the user if there is no cli query argument
        if not query:
            query = input("Enter search query: ")
        print(f"\n{Style.BRIGHT}Search query:{Style.RESET_ALL} {query}")

        # get results from LibGen
        try:
            print("Fetching results from LibGen...")
            # request = SearchRequest(query)
        except QueryError as qerr:
            print(f"\n{Fore.MAGENTA}{qerr}{Style.RESET_ALL}")
            query = None
            continue
        except ConnectionError as cerr:
            if tries == 4:
                close(f"{Fore.RED}{cerr}{Style.RESET_ALL}\n")
            else:
                tries += 1
                print(f"{Fore.RED}{cerr} Retrying in     ", end="")
                for i in range(9, 0, -1):
                    print(f"\b\b\b\b{i}", end="...", flush=True)
                    sleep(1)
                print(Style.RESET_ALL)
                continue
        else:
            # results = Results(request.results)
            results = Results(data)
            print(f"{Style.BRIGHT}{len(results.entries)}{Style.RESET_ALL}"
                  " entries found.")
            list_entries(results.entries)

            # DEBUG save to file
            # with open("data", "w") as f:
            #     json.dump(results.entries, f)

        # show details/download, filter results,
        # start new search or close application
        while True:
            c = input("\nDownload, filter results, new search"
                      " or quit [d/f/s/q]: ").lower()
            match c:

                # TODO show details, download entry
                case "d":
                    print("details, download...")
                    continue

                # filter results
                case "f":

                    # get filtering sequence
                    try:
                        seq = input("Filtering sequence: ")
                        filters, mode = parse_filter_seq(seq)
                    except FilterError as ferr:
                        print(f"\n{Fore.MAGENTA}{ferr}{Style.RESET_ALL}")
                        continue
                    else:
                        print(f"\n{Style.BRIGHT}Filtering mode:"
                              f"{Style.RESET_ALL} {mode}")
                        print(f"{Style.BRIGHT}Filters{Style.RESET_ALL}")
                        for key, value in zip(filters.keys(), filters.values()):
                            print(f"  {key + ':':<6} {value}")

                    # apply filter and return filtered results
                    try:
                        if filters:
                            results = results.filter_entries(filters, mode)
                        else:
                            print(f"\n{Fore.MAGENTA}"
                                  f"No valid filters were specified!"
                                  f"{Style.RESET_ALL}")
                            continue
                    except FilterError as ferr:
                        print(f"\n{Fore.MAGENTA}{ferr}{Style.RESET_ALL}")
                        continue
                    else:
                        if len(results.entries) > 0:
                            print(f"{Style.BRIGHT}{len(results.entries)}"
                                  f"{Style.RESET_ALL} entries found.")
                            list_entries(results.entries)
                        else:
                            print(f"{Fore.MAGENTA}No matching entries found!"
                                  f"{Style.RESET_ALL}")
                        continue

                # new search
                case "s":
                    tries = 0
                    query = None
                    break

                # close application
                case "q":
                    close(f"\n{Style.BRIGHT}Goodbye!{Style.RESET_ALL}\n")

                # invalid command
                case _:
                    print("Available commands: [f]ilter, [s]earch, [q]uit!")
                    continue


if __name__ == '__main__':
    main()
