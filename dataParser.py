import os
import json
from city import City
from connections import Connections


def get_dataset():
    files = []
    i = 1
    with os.scandir('resources/') as entries:
        for entry in entries:
            print(i, "- ", entry.name)
            i += 1
            files.append(entry.name)

    try:
        chosen_file = int(input("select a data set: "))
    except ValueError as e:
        chosen_file = 0

    if chosen_file > len(files) or chosen_file <= 0:
        print("Invalid file. \n")
        return None
    else:
        return files[chosen_file - 1]


def parse_data():
    file =  get_dataset()
    if file is not None:
        with open("resources/" +file,  encoding='utf-8') as json_file:
            data = json.load(json_file)
            cities = dict()
            connections = dict()
            for city in data['cities']:
                cities[city['name']] = City(city['name'], city['address'], city['country'], city['latitude'], city['longitude'])

            for connection in data['connections']:
                if connection['from'] != connection['to']:
                    weight = {'distance': connection['distance'], 'duration':  connection['duration']}
                    connections[(connection['from'], connection['to'])] = weight

                    cities[connection['from']].add_next(cities[connection['to']], weight)

        return cities, connections
    else:
        return None , None
