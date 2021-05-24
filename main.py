from dataParser import parse_data
from Algorithms.AStar import AStar
from Algorithms.CSP import  CSP
import timeit

def main():

    while True:
        cities, connections = parse_data()
        city1 = input("What is your starting city? ")
        if city1 not in cities:
            print("the city ", city1, " is not in the data set")
            continue
        city2 = input("What is the destination? ")
        if city2 not in cities:
            print("the city ", city2, " is not in the data set")
            continue

        print("1. A*")
        print("2. CSP")
        select_algo = int(input("which algorithm would you like to search with? "))
        if select_algo == 1:
            algo = AStar(cities, connections)
        elif select_algo == 2:
            algo = CSP(cities, connections)
        else:
            print("invalid algorithm")
            continue

        time_start = timeit.default_timer()
        solution = algo.find_minimum_distance(city1, city2)

        print("-------- time consumed in seconds is : ", (timeit.default_timer() - time_start), " --------")
        algo.printResults(solution)

        exit = input("Would you like to find another route? (y/n) ")
        if exit.lower() == "n":
            break


if __name__ == '__main__':
    main()
