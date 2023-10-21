import sys
import requests
from bs4 import BeautifulSoup

webCrawl = []
CRAWLED = set()


def request(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
              }
    try:
        response = requests.get(url, headers=header)
        return response.text
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        pass


def getLinks(mainDomain):
    links = []
    try:
        soup = BeautifulSoup(mainDomain, "html.parser")
        tags_a = soup.find_all("a", href=True)
        for tag in tags_a:
            link = tag["href"]
            if link.startswith("http"):
                links.append(link)

        return links
    except:
        pass


def crawl():
    while 1:
        if webCrawl:
            url = webCrawl.pop()

            html = request(url)
            if html:
                links = getLinks(html)
                if links:
                    for link in links:
                        if link not in CRAWLED and link not in webCrawl:
                            webCrawl.append(link)

                print("Crawling {}".format(url))

                CRAWLED.add(url)
            else:
                CRAWLED.add(url)
        else:
            print("Done")
            break


if __name__ == "__main__":
    url = sys.argv[1]
    webCrawl.append(url)
    crawl()