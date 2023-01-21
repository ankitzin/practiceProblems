def read_maze(file):
    try:
        with open(f'{file}', 'r') as f:
            maze = [[char for char in line.strip('\n')] for line in f]
        number_cols_top_row = len(maze[0])
        for row in maze:
            if len(row) != number_cols_top_row:
                print("Maze is not complete rectangular.")
                raise SystemError
        return maze
    except Exception as error:
        print(str(error))


if __name__ == '__main__':
    maze = read_maze('mazes/modest_maze.txt')
    for row in maze:
        print(row)
