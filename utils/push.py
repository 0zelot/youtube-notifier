import requests

def push(url, item):
    requests.post(url,
        data = "{} posted a new video: {}".format(item["author"]["name"], item["video"]["title"]).encode("utf-8"),
        headers = {
            "Title": item["video"]["title"].encode("utf-8"),
            "Icon": item["video"]["thumbnail"],
            "Click": item["video"]["url"]
        })