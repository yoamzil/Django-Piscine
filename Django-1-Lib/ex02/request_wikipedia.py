import sys

import dewiki
import requests


def getBestTitle(search, URL, HEADERS):
    SEARCH_PARAMS = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": search,
    }
    R = requests.get(url=URL, params=SEARCH_PARAMS, headers=HEADERS)
    DATA = R.json()

    results = DATA["query"]["search"]
    if not results:
        print("Error: no results found for your search")
        sys.exit(1)
    return results[0]["title"]


def searchWiki(title, URL, HEADERS):
    PARAMS = {
        "action": "query",
        "format": "json",
        "prop": "revisions",
        "rvprop": "content",
        "rvslots": "main",
        "redirects": True,
        "titles": title,
    }

    R = requests.get(url=URL, params=PARAMS, headers=HEADERS)
    DATA = R.json()
    pages = DATA["query"]["pages"]
    page = next(iter(pages.values()))
    if "revisions" not in page:
        print("Error: article not found")
        sys.exit(1)
    result = page["revisions"][0]["slots"]["main"]["*"]
    clean_result = dewiki.from_string(result)
    return clean_result


def main():
    if len(sys.argv) != 2:
        print("Usage: python request_wikipedia.py <topic>")
        sys.exit(1)

    URL = "https://en.wikipedia.org/w/api.php"
    HEADERS = {"User-Agent": "request_wikipedia/1.0 (amzilyouness@gmail.com)"}
    try:
        title = getBestTitle(sys.argv[1], URL, HEADERS)
        result = searchWiki(title, URL, HEADERS)
        filename = sys.argv[1].replace(" ", "_") + ".wiki"
        with open(filename, "w") as f:
            f.write(result)
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        sys.exit(1)
    except KeyError:
        print("Error: could not find content for this article")
        sys.exit(1)


if __name__ == "__main__":
    main()
