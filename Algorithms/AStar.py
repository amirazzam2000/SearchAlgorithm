from itertools import tee


class AStar:

    def __init__(self, cities: dict, connections: dict):
        self.cities = cities
        self.connections = connections


    def find_minimum_distance(self, start, end):
        future = []
        visited = []


        self.cities[start].add_coming_from([])
        self.cities[start].weighted_distance = 0
        future.append(self.cities[start])

        while len(future) != 0:
            future.sort(key=lambda x: x.weighted_distance)

            future[0].mark_as_visited()
            next = future.pop(0)

            if next.name == end:
                return next.coming_from

            parent_distance = next.weighted_distance  # parent's distance
            for suc in next.get_connections():
                suc = suc['city']

                aux = (parent_distance
                       + self.connections[(next.name, suc.name)]['distance'] * 0.4
                       + self.connections[(next.name, suc.name)]['duration'] * 0.6
                       + (len(suc.coming_from) - 1) * 1000)  # modifier

                reset = False
                if suc in future:
                    if aux >= suc.weighted_distance:
                        continue

                elif suc in visited:
                    if aux >= suc.weighted_distance:
                        continue
                    reset = True
                    suc.un_visit()
                    visited.remove(suc)
                    future.append(suc)

                else:
                    future.append(suc)

                suc.weighted_distance = aux
                if len(suc.coming_from) > 1:
                    reset = True
                suc.add_coming_from(next.coming_from, reset)
            visited.append(next)
        return None

    def printResults(self, results):
        total_distance = 0
        for i, j in pairwise(results):
            total_distance += self.connections[i.name, j.name]['distance']

        print("total distance: ", total_distance, "m")

        if results is not None:
            for s in results:
                print(s.name)
        else:
            print("there isn't a path to that city from where you are!")


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)