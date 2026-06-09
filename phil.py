import collections
import re
from urllib.error import URLError, HTTPError
from urllib.parse import quote, unquote
from urllib.request import urlopen
import sys


def get_content(name):
    try:
        with urlopen('http://ru.wikipedia.org/wiki/' + quote(name)) as page:
            content = page.read().decode('utf-8')
            return content
    except (URLError, HTTPError):
        return None


def extract_content(page):
    if page is None:
        return 0, 0,

    begin = re.search(r'<div id="mw-content-text"', page).start()
    end = re.search(r'<div id="mw-navigation">', page).start() - 1

    return begin, end,


def extract_links(page, begin, end):
    reg_exp = re.compile(r"/wiki[^>\"#: -]+[\"\']", re.IGNORECASE)
    links_list = re.findall(reg_exp, page[begin:end])
    full_links_list = set()

    for link in links_list:
        name = unquote(link[6:-1])
        full_links_list.add(name)

    return full_links_list


def find_chain(start, finish):
    if start == finish:
        return [start, finish]

    queue_of_pages = collections.deque([[start]])
    visited_pages = set()
    content_of_pages = {}

    while queue_of_pages:
        path = queue_of_pages.popleft()
        current_page = path[-1]

        if current_page == finish:
            return path

        if current_page not in visited_pages:
            visited_pages.add(current_page)

            if current_page not in content_of_pages:
                content = get_content(current_page)
                content_of_pages[current_page] = content
            else:
                content = content_of_pages[current_page]

            if content:
                begin, end = extract_content(content)
                links = extract_links(content, begin, end)

                for link in links:
                    if link == finish:
                        return path + [link]

                    new_path = list(path) + [link]
                    queue_of_pages.append(new_path)

    return None


if __name__ == '__main__':
    if len(sys.argv) < 2:
        word = input('Enter word: ')
    else:
        word = sys.argv[1]

    print(find_chain(word, 'Философия'))
