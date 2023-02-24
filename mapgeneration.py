import random

def make_maze(width,height,entrance,exit):
    status = True
    while status:
        # create an empty 20 x 20 grid
        maze = [['1']*width for i in range(height)]

        # generate a list of all the walls
        walls = []
        for i in range(1,height-1):
            for j in range(1,width-1):
                walls.append((i,j,'down'))
                walls.append((i,j,'right'))
                walls.append((i,j,'left'))
                walls.append((i,j,'up'))

        # shuffle the walls
        random.shuffle(walls)

        # initialize a set to keep track of the visited cells
        visited = set()

        # run the Randomized Kruskal Algorithm
        for wall in walls:
            i, j, direction = wall
            if direction == 'down':
                if (i,j) not in visited and (i,j+1) not in visited:
                    maze[i][j] = '_'
                    visited.add((i,j))
                    visited.add((i,j+1))
            elif direction == 'right':
                if (i,j) not in visited and (i+1,j) not in visited:
                    maze[i][j] = '_'
                    visited.add((i,j))
                    visited.add((i+1,j))
            elif direction == 'up':
                if (i,j) not in visited and (i,j-1) not in visited:
                    maze[i][j] = '_'
                    visited.add((i,j))
                    visited.add((i,j-1))
            elif direction == 'left':
                if (i,j) not in visited and (i-1,j) not in visited:
                    maze[i][j] = '_'
                    visited.add((i,j))
                    visited.add((i-1,j))

        # add the entrance and exit
        maze[entrance[0]][entrance[1]] = '_'
        maze[exit[0]][exit[1]] = '_'
        if is_path(maze,entrance, exit):
            status = False
            break
    return maze

def is_path(maze, entrance, exit):
    # find the entrance and exit coordinates

    # initialize a set to keep track of visited cells
    visited = set()

    # define a recursive DFS function to search for a path
    def dfs(row, col):
        # if the current cell is the exit, return True
        if (row, col) == exit:
            return True
        # mark the current cell as visited
        visited.add((row, col))
        # search all adjacent cells that are not walls and not visited
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and \
                maze[new_row][new_col] == '_' and (new_row, new_col) not in visited:
                # if a path is found, return True
                if dfs(new_row, new_col):
                    return True
        # if no path is found, return False
        return False

    # start the search from the entrance
    return dfs(entrance[0], entrance[1])
