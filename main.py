import json

from utils.fetch import *
from utils.push import *

file_config = open("./config.json")
file_data = open("./data.json")

config = json.load(file_config)
data = json.load(file_data)

for item in config["followed"]:

    results = fetch(item)

    for new in results:
        if(new["author"]["id"] in data and new["video"]["id"] not in data[new["author"]["id"]]): 
            for subscriber in item["subscriptions"]:
                for targetedSubscriber in config["subscribers"]:
                    if(targetedSubscriber["name"] == subscriber):
                        push(targetedSubscriber["url"], new)

    data[item["id"]] = [item["video"]["id"] for item in results]

    with open("./data.json", "w") as file:
        json.dump(data, file, indent=4)

file_config.close()
file_data.close()