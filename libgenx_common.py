import getopt
import json
from libgen_api import LibgenSearch
from urllib.request import urlretrieve


def parse_args(args):
    flags = "a:t:"
    long_flags = ["author=", "title="]
    search_fields = {'author': "", 'title': ""}
    try:
        arguments, values = getopt.getopt(args, flags, long_flags)
        for arg, value in arguments:
            if arg in ("-a", "-author"):
                search_fields['author'] = value
            elif arg in ("-t", "-title"):
                search_fields['title'] = value
        return search_fields
    except getopt.error as err:
        print(str(err))


def load_config():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
        print(f"Configuration - Download directory: {config['downloadDir']}, PDF only: {config['pdfOnly']}")
        return config


def search(author, title, pdf):
    s = LibgenSearch()
    results = []

    if author and title:
        pass  # todo cross filter author and title results
    elif author:
        print(f"Searching: {author}")
        results = s.search_author(author)
    elif title:
        print(f"Searching: {title}")
        results = s.search_title(title)
    else:
        print("Search fields are empty!")

    if results:
        if pdf:
            results = [result for result in results if result['Extension'] == "pdf"]
        for result in results:
            result['Label'] = (
                    f"{result['Author'][:20] + '...' if len(result['Author']) > 20 else result['Author']:<23}" +
                    f" {result['Title'][:30] + '...' if len(result['Title']) > 30 else result['Title']:<33}" +
                    f" {result['Year']:<9} {result['Pages']:>9} {result['Extension']:>5} {result['ID']}")
        print(f"  Results: {len(results)}")
        return results


def download(result, download_dir, url):
    filename = f"{download_dir}/{result['ID']}.{result['Extension']}"
    print(f"Downloading: {result['Label']}")
    urlretrieve(url, filename)
    print("  Done!")
