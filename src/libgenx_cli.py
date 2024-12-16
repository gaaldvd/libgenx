"""
LibGenX CLI script.
"""

from sys import exit as close, argv
from os.path import dirname, abspath, join
from os import makedirs
from re import findall
from time import sleep
from colorama import Style, Fore
from libgentools import *
from libgenx_common import get_cli_args, load_config


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
    request, results, filters = None, None, None

    # load configuration file
    config = load_config()

    # get query and filters from cli arguments
    query, seq = get_cli_args()

    # main loop
    while True:

        # get query from the user if there is no cli query argument
        if not query:
            query = input("Enter search query: ")
        print(f"\n{Style.BRIGHT}Search query:{Style.RESET_ALL} {query}")

        # show filters from cli arguments if there are any
        if seq:
            try:
                filters, mode = parse_filter_seq(seq)
            except FilterError as ferr:
                print(f"\n{Fore.MAGENTA}{ferr}{Style.RESET_ALL}\n")
            else:
                print(f"{Style.BRIGHT}Filtering mode:"
                      f"{Style.RESET_ALL} {mode}")
                print(f"{Style.BRIGHT}Filters{Style.RESET_ALL}")
                for key, value in zip(filters.keys(), filters.values()):
                    print(f"  {key + ':':<6} {value}")

        # get results from LibGen
        try:
            print(f"\nFetching results from LibGen"
                  f"{" (pdf only)" if config['pdfOnly'] else ""}...")
            request = SearchRequest(query)
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
            results = Results(request.results)
            if filters:
                results = results.filter_entries(filters, mode)
            if config['pdfOnly']:
                results = results.filter_entries({'ext': "pdf"})
            print(f"{Style.BRIGHT}{len(results.entries)}{Style.RESET_ALL}"
                  " entries found.")
            list_entries(results.entries)

        # show details/download, filter results,
        # start new search or close application
        while True:
            c = input("\nDownload, filter results, new search"
                      " or quit [d/f/s/q]: ").lower()
            match c:

                # show details, download entry
                case "d":

                    # prompt for entry number
                    while True:
                        num = input("Entry no. (press Return to cancel): ")
                        if num == "":
                            break
                        try:
                            num = int(num)
                            if num < 1 or num > len(results.entries):
                                raise ValueError
                        except ValueError:
                            print(f"\n{Fore.MAGENTA}"
                                  f"Entry number must be between 1 and "
                                  f"{len(results.entries)}!"
                                  f"{Style.RESET_ALL}\n")
                            continue

                        # show details
                        else:
                            entry = results.entries[num - 1]
                            print(f"\n{Style.BRIGHT}Author:{Style.RESET_ALL}"
                                  f" {entry['auth']}")
                            print(f"{Style.BRIGHT}Title:{Style.RESET_ALL}"
                                  f" {entry['title']}")
                            print(f"{Style.BRIGHT}Publisher:{Style.RESET_ALL}"
                                  f" {entry['pub']} ({entry['year']})")
                            print(f"{Style.BRIGHT}Language:{Style.RESET_ALL}"
                                  f" {entry['lang']}")
                            print(f"{Style.BRIGHT}Pages, format:"
                                  f"{Style.RESET_ALL}"
                                  f" {entry['pp']} pp., {entry['ext']}\n")

                            # prompt for download
                            while True:
                                c = input("Enter 'y' to download"
                                          " (press Return to cancel): ").lower()
                                if c == "":
                                    break
                                if c == "y":
                                    print(f"Downloading {entry['id']}:"
                                          f" {entry['title']}...")
                                    path = (join(dirname(dirname(abspath(
                                        argv[0]))), "downloads")
                                            if config['downloadDir'] == ""
                                            else config['downloadDir'])
                                    makedirs(path, exist_ok=True)
                                    downloaded = results.download(entry, path)
                                    if downloaded:
                                        print("Done!")
                                    else:
                                        print("Downloading failed!")
                                    break
                                continue
                        break

                # filter results
                case "f":

                    # prompt for filtering sequence
                    try:
                        seq = input("Filtering sequence: ")
                        filters, mode = parse_filter_seq(seq)
                        seq = None
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
                    print(f"{Fore.MAGENTA}Available commands:"
                          f" [f]ilter, [s]earch, [q]uit!{Style.RESET_ALL}")
                    continue


if __name__ == '__main__':
    main()
