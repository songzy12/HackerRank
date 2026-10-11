# https://www.hackerrank.com/challenges/the-quickest-way-up/problem?isFullScreen=true
#
# Build a graph representing the board, where each node is a square and edges
# represent possible moves.
#
# Then, run shortest path algorithm on the graph. That is, BFS.
#
# With the snakes and ladders, we need to account for teleportation and
# blackholes in the BFS.
# Note it seems the assumption is:
# 1. The starting point of snakes and ladders are not counted as reachable.
# 2. We only go one step at the snakes and ladders, so no need to follow chains.

import os
from collections import deque, defaultdict


def buildGraph(start, end, dice):
    graph = defaultdict(list)
    for i in range(start, end + 1):
        for j in range(1, dice + 1):
            if i + j <= end:
                graph[i].append(i + j)
    return graph


def buildTeleportAndBlackhole(ladders, snakes):
    ladders_snakes = dict(ladders + snakes)

    teleport = {}
    blackhole = set()
    for start in ladders_snakes:
        end = ladders_snakes[start]
        # while end in ladders_snakes:
        #     if end == start:
        #         blackhole.add(start)
        #         break
        #     end = ladders_snakes[end]
        teleport[start] = end
    return teleport, blackhole


def bfs(graph, start, teleport, blackhole):
    visited = set()
    distance = {}

    queue = deque([start])
    visited.add(start)
    distance[start] = 0

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor in visited:
                continue

            visited.add(neighbor)
            if neighbor in blackhole:
                distance[neighbor] = -1
                continue

            if neighbor in teleport:
                neighbor = teleport[neighbor]
                visited.add(neighbor)
            distance[neighbor] = distance[node] + 1
            queue.append(neighbor)

    return distance


def quickestWayUp(ladders, snakes):
    start = 1
    end = 100
    dice = 6

    graph = buildGraph(start, end, dice)
    teleport, blackhole = buildTeleportAndBlackhole(ladders, snakes)
    # print("teleport:", teleport)
    # print("blackhole:", blackhole)

    distance = bfs(graph, start, teleport, blackhole)
    return distance.get(end, -1)


if __name__ == "__main__":
    with open(os.environ["OUTPUT_PATH"], "w") as fptr:
        t = int(input().strip())
        for t_itr in range(t):
            n = int(input().strip())
            ladders = []
            for _ in range(n):
                ladders.append(list(map(int, input().rstrip().split())))
            m = int(input().strip())
            snakes = []
            for _ in range(m):
                snakes.append(list(map(int, input().rstrip().split())))

            result = quickestWayUp(ladders, snakes)

            fptr.write(str(result) + "\n")
