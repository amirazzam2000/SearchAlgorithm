import sys

class City:

    def __init__(self, name, address, country, latitude, longitude):
        self.name = name
        self.address = address
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.connects_to = []
        self.coming_from = []
        self.weighted_distance = sys.maxsize
        self.visited = False

    def mark_as_visited(self):
        self.visited = True

    def un_visit(self):
        self.visited = False

    def is_visited(self):
        return self.visited

    def add_next(self, city, weight):
        self.connects_to.append({'city': city, 'weight': weight})
        self.connects_to.sort(key=lambda x: x['weight']['distance'])

    def get_connections(self):
        return self.connects_to

    def add_coming_from(self, coming_from: [], reset=False):
        if reset:
            self.coming_from = []
        self.coming_from.extend(coming_from)
        self.coming_from.append(self)

