#!/usr/bin/env python

"""
Threaded Downloader
"""
import time
import requests
import threading
import queue


def main():

    NEWS_API_KEY = "84d0483394c44f288965d7b366e54a74"
    base_url = 'https://newsapi.org/v1/'
    WORD = "Russia"
    TITLES = []
    # narrowed due to API request limits
    sources = ['abc-news-au', 'al-jazeera-english', 'ars-technica']
    thread_count = 2
    art_count = 0
    word_count = 0

    def get_articles(sources):
        for source in sources:
            url = base_url + "articles"
            params = {"source": source,
                      "apiKey": NEWS_API_KEY,
                      "sortBy": "top",
                      }
            resp = requests.get(url, params=params)
            if resp.status_code != 200:  # aiohttpp has "status"
                print("something went wrong with {}".format(source))
                print(resp)
                print(resp.text)
                return []
            data = resp.json()
            for art in data['articles']:
                TITLES.append(str(art['title']) + str(art['description']))

    def threading_articles(sources, thread_count=1):
        results = queue.Queue()
        sources = sources
        threads = []

        def worker(*args):
            results.put(get_articles(*args))

        for i in range(thread_count):
            thread = threading.Thread(target=worker, args=(sources,))
            threads.append(thread)
            thread.start()
            print("Thread %s started" % thread.name)

        for t in threads:
            t.join()

    def count_word(word, titles):
        word = word.lower()
        count = 0
        for title in titles:
            if word in title.lower():
                count += 1
        return count

    start = time.time()
    threading_articles(sources, thread_count)
    count_word(WORD, TITLES)
    art_count += len(TITLES)
    word_count += count_word(WORD, TITLES)

    print(WORD, "found {} times in {} articles".format(word_count, art_count))
    print("Process took {:.0f} seconds".format(time.time() - start))


if __name__ == '__main__':
    main()
