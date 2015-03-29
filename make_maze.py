import sys
import random

def Step(x, y):
    maze[x][y] = 1
    random_neighbours = random.sample(neighbouring_nodes, len(neighbouring_nodes))
    for d in random_neighbours:
        nx = x + d[0]; ny = y + d[1]
        if (nx in range(n) and ny in range(n)):
            if (maze[nx][ny] == 0):
                edges.append(((x, y), (nx, ny)))
                maze[nx][ny] = 1
                Step(nx, ny)

if (len(sys.argv) == 6):
    n = int(sys.argv[1])
    if (n > 30):
        n = 30
    start_x = int(sys.argv[2])
    start_y = int(sys.argv[3])
    seed = int(sys.argv[4])
    output_file = sys.argv[5]

    maze = [[0 for x in range(n)] for y in range(n)]
    edges = []

    neighbouring_nodes = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    random.seed(input_seed)

    Step(start_x, start_y)

    file = open(output_file, "w")
    for edge in edges:
        file.write("({0}, {1}), ({2}, {3})\n".format(edge[0][0], edge[0][1], edge[1][0], edge[1][1]))
    file.close()
