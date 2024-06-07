import sys
import libgenx_common as lgx
from libgen_api import LibgenSearch

results, config = [], lgx.load_config()

args = lgx.parse_args(sys.argv[1:]) if len(sys.argv) > 1 and (sys.argv[2] or sys.argv[4]) else None

if args:
    results = lgx.search(args['author'], args['title'], config['pdfOnly'])
else:
    results = lgx.search(input("  Author: "), input("  Title: "), config['pdfOnly'])

if results:
    print("\n  Nr. Author                  Title                             Year Pages    Extension ID\n")
    i = 0
    for result in results:
        i += 1
        print(f"  {i:<3} {result['Label']}")

try:
    n = int(input("\n> Choose Nr. to download or press Return to exit: ")) - 1
    s = LibgenSearch()
    lgx.download(results[n], config['downloadDir'], s.resolve_download_links(results[n])['GET'])
    sys.exit("> Goodbye!")
except ValueError:
    sys.exit("> Goodbye!")
