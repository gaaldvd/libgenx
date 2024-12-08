"""
LibGenX CLI script.
"""

from sys import exit as close
from colorama import Style, Fore
from libgentools import SearchRequest, Results, QueryError, FilterError
from libgenx_common import get_query_arg


def list_entries(entries):
    """List results."""
    print(Style.BRIGHT + "\nNo.".ljust(6)
          + "Author".ljust(24) + "Title".ljust(34)
          + "Year".ljust(5) + "Pages".ljust(9) + "Extension".ljust(10)
          + "ID".ljust(11) + "\n" + "-" * 96 + Style.RESET_ALL)
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


def main():
    """Main function of the LibGenX CLI script."""
    print(Style.BRIGHT + "\nWelcome to LibGenX!" + Style.RESET_ALL)
    tries = 0

    # get query from cli arguments
    query = get_query_arg()

    # main loop
    while True:

        # get the query from the user if there is no cli query argument
        if not query:
            query = input("Enter search query: ")
        print(f"\n{Style.BRIGHT}Search query:{Style.RESET_ALL} {query}")

        # get the results from LibGen
        try:
            print("Fetching results from LibGen...")
            request = SearchRequest(query)
        except QueryError as qerr:
            print(f"\n{Fore.MAGENTA}{qerr}{Style.RESET_ALL}")
            query = None
            continue
        except ConnectionError as cerr:
            if tries == 6:
                close(f"\n{Fore.RED}{cerr}{Style.RESET_ALL}")
            else:
                tries += 1
                print(f"\n{Fore.RED}{cerr}{Style.RESET_ALL}")
                continue
        else:
            results = Results(request.results)
            print(f"{Style.BRIGHT}{len(results.entries)}{Style.RESET_ALL}"
                  " entries found.")
            list_entries(results.entries)

        # filter results, start new search or close application
        while True:
            c = input("\nFilter results, new search or quit [f/s/q]: ").lower()
            match c:

                # filter results
                case "f":

                    # TODO get filtering sequence from the user
                    filters = {'auth': "Jane Austen", 'ext': "pdf"}
                    mode = "exact"
                    print(f"\n{Style.BRIGHT}Filtering mode:{Style.RESET_ALL}"
                          f" {mode}")
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
                        print(f"{Style.BRIGHT}{len(results.entries)}"
                              f"{Style.RESET_ALL} entries found.")
                        list_entries(results.entries)
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
