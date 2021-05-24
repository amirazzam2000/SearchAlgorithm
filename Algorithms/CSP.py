class CSP:

    def __init__(self, cities: dict, connections: dict):
        self.cities = cities
        self.connections = connections
        self.distance = 0

    def find_minimum_distance(self, start, end):

        next = self.cities[start].get_connections()

        if len(next) > 1:
            next.sort(key=lambda x: x['weight']['distance'])

        for i in range(len(next)):
            next_city = next[i]['city']
            if next_city.name == end:
                path = [next_city.name]
                self.distance += self.connections[start, next_city.name]['distance']
                return path
            elif not next_city.is_visited():
                next_city.mark_as_visited()
                path = self.find_minimum_distance(next_city.name, end)
                if len(path) != 0:
                    self.distance += self.connections[start, next_city.name]['distance']
                    if next_city.name not in path:
                        path.append(next_city.name)
                    if start not in path:
                        path.append(start)
                    return path
        return []

    def printResults(self, results):
        print("total distance: ", self.distance, "m")
        self.distance = 0
        if len(results) > 0:
            for s in reversed(results):
                print(s)
        else:
            print("there isn't a path to that city from where you are!")
