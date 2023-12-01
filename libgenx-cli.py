import libgenx_common as lgx
from libgen_api import LibgenSearch

s = LibgenSearch()
results = s.search_title(input("\ntitle: "))
# results = s.search_title("pride and prejudice")

print("\nNr.  Author                  Title                             Year   Pages   Extension\n")
i = 0
for result in results:
    i += 1
    print(f"{i:>3}. {result['Author'][:20] + '...' if len(result['Author']) > 20 else result['Author']:<23}"
          f" {result['Title'][:30] + '...' if len(result['Title']) > 30 else result['Title']:<33}"
          f" {result['Year']:<4} {result['Pages']:>9} {result['Extension']}")

lgx.download(int(input("\ndownload: ")) - 1, s, results)
# lgx.download(1, s, results)
