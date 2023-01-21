import readMaze

maze = readMaze.read_maze('mazes/challenge_maze.txt')
for row in maze:
    print(row)