from urllib.request import urlretrieve


def download(nr, s, results):
    links = s.resolve_download_links(results[nr])
    print(f'\n{links}')
    print("downloading...")
    urlretrieve(links['GET'], "download.pdf")
    print('done!')
