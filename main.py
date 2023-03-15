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
        if(new not in data[results[0]["author"]["id"]]): 
            push(new)

    data[results[0]["author"]["id"]] = results

    with open("./data.json", "w") as f:
        json.dump(data, f, indent=4)

file_config.close()
file_data.close()