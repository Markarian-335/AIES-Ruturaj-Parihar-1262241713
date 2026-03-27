import random

def main():

    n = int(input("Enter number of cities:"))
    tsp = []
    print("Enter the distance matrix row by row:")
    for i in range(n):
        row = list(map(int, input().split()))
        tsp.append(row)
    
    # tsp = [
    # [0, 8, 9, 10],
    # [1, 0, 10, 6],
    # [2, 7, 0, 3],
    # [11, 5, 9, 0],
    # ]

    print(hillClimbing(tsp))

def hillClimbing(tsp):
    currentSolution = randomSolution(tsp)
    currentRouteLength = routeLength(tsp, currentSolution)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)

    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)

    return currentSolution, currentRouteLength

def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity = cities[random.randint(0, len(cities)-1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution

def routeLength(tsp, currentSolution):
    routeLength = 0
    for i in range(len(currentSolution)):
        fromCity = currentSolution[i]
        toCity = currentSolution[(i + 1) % len(currentSolution)]
        routeLength += tsp[fromCity][toCity]
    return routeLength

def getNeighbours(currentSolution):
    neighbours = []
    for i in range(len(currentSolution)):
        for j in range(i + 1, len(currentSolution)):
            neighbour = currentSolution[:]
            neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
            neighbours.append(neighbour)
    return neighbours

def getBestNeighbour(tsp, neighbours):
    bestNeighbour = neighbours[0]
    bestNeighbourRouteLength = routeLength(tsp, bestNeighbour)

    for neighbour in neighbours:
        currentLength = routeLength(tsp, neighbour)
        if currentLength < bestNeighbourRouteLength:
            bestNeighbour = neighbour
            bestNeighbourRouteLength = currentLength

    return bestNeighbour, bestNeighbourRouteLength

if __name__ == "__main__":
    main()