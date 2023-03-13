import requests
import xmltodict
import re

mappings = {
    "channel": "https://www.youtube.com/feeds/videos.xml?channel_id={}",
    "playlist": "https://www.youtube.com/feeds/videos.xml?playlist_id={}"
}

def fetch(item):
    
    response = requests.get(mappings[item["type"]].format(item["id"]))
    body = xmltodict.parse(response.text)

    videos = []
    i = 0

    for video in body["feed"]["entry"]:

        if(re.search(item["regex"], video["title"]) == None): continue
        if(i >= 3): break

        videos.append({
            "author": {
                "id": video["yt:channelId"],
                "name": video["author"]["name"]
            },
            "video": {
                "id": video["yt:videoId"],
                "title": video["title"],
                "thumbnail": "https://i.ytimg.com/vi/{}/hqdefault.jpg".format(video["yt:videoId"]),
                "url": "https://youtu.be/{}".format(video["yt:videoId"])
            }
        })
        
        i += 1

    return videos