import numpy as np
from tkinter import *
from PIL import Image

# maze-picture generator https://keesiemeijer.github.io/maze-generator/

ITERATIVE = 0
A_STAR = 1

# method = ITERATIVE
method = A_STAR

# import maze image
img = Image.open("images/m6.png")
W = 10
rows = img.height
cols = img.width

# get data in form of 2d array from image
maze = np.array(img)
maze = np.delete(maze, 3, axis=2)
maze = np.round(maze.mean(axis=2)/255)

# make canvas
root = Tk()
root.title("Path Finder")
root.resizable(False, False)
cnvs = Canvas(root, bg="white", width=cols *
              W, height=rows*W, borderwidth=0)


# make a drawing function for rectangle
def draw_rect(i, j, clr):
    cnvs.create_rectangle(j*W, i*W, j*W+W, i*W+W, fill=clr, outline='')


# draw the maze on canvas
for j in range(cols):
    for i in range(rows):
        if not maze[i, j]:
            draw_rect(i, j, "black")

start = (0, cols//2-1)
end = (rows-1, cols//2+1)
draw_rect(start[0], start[1], "blue")
draw_rect(end[0], end[1], "green")

path = []

if (method == ITERATIVE):
    ############################## normal path-finder with iterative method #################################
    visited = np.zeros(maze.shape)
    current = start

    def is_available(i, j):
        return i >= 0 and i < rows and j >= 0 and j < cols and maze[i][j] == 1 and not visited[i, j]

    while (current != end):
        # mark current cell as visited
        visited[current[0], current[1]] = 1
        i, j = current

        # add all neighbours if available
        neighbours = []
        if (is_available(i, j+1)):  # bottom
            neighbours.append((i, j+1))
        if (is_available(i, j-1)):  # top
            neighbours.append((i, j-1))
        if (is_available(i+1, j)):  # right
            neighbours.append((i+1, j))
        if (is_available(i-1, j)):  # left
            neighbours.append((i-1, j))

        if (len(neighbours) > 0):  # there are any neighbors
            # add current location to path
            path.append(current)

            # make the first neighbour current cell
            current = neighbours[0]

        else:  # no neighbor available
            # pop the last cell from the path and make it current cell
            current = path.pop()

            if (current == start):  # the current cell is start
                print("path is not available")
                path = []
                break
elif method == A_STAR:
    ############################## A* ##################################

    def heuristic(a, b):
        # return np.sqrt((a.i-b.i)**2 + (a.j-b.j)**2)
        return abs(a.i-b.i) + abs(a.j-b.j)

    def is_available(i, j):
        return i >= 0 and i < rows and j >= 0 and j < cols and maze[i, j] == 1

    # making a class spot which has f-score, g-score and h-score
    class Spot:
        # f-Score represents our current best guess as to how cheap a path could be from start to finish if it goes through n.
        # g-score is the cost of the cheapest path from start to n currently known.
        f = g = h = 0

        # 'previous' is the node immediately preceding it on the cheapest path from start
        previous = None

        def __init__(self, i, j):
            self.i = i
            self.j = j
            self.neighbours = [] 

        def add_neighbours(self):  # adding neighbours
            i, j = self.i, self.j
            if (is_available(i, j+1)):  # bottom
                self.neighbours.append(grid[i, j+1])
            if (is_available(i, j-1)):  # top
                self.neighbours.append(grid[i, j-1])
            if (is_available(i+1, j)):  # right
                self.neighbours.append(grid[i+1, j])
            if (is_available(i-1, j)):  # left
                self.neighbours.append(grid[i-1, j])

    # initializing openset and closedset
    open_set = []
    closed_set = []
    grid = np.full(maze.shape, None)

    # initializing grid of spots
    for i in range(rows):
        for j in range(cols):
            grid[i, j] = Spot(i, j)

    for i in range(rows):
        for j in range(cols):
            grid[i, j].add_neighbours()

    start = grid[start[0], start[1]]
    end = grid[end[0], end[1]]

    open_set.append(start)

    while len(open_set) > 0:
        winner = 0
        for i in range(len(open_set)):
            if open_set[i].f < open_set[winner].f:
                winner = i

        current = open_set[winner]
        if current == end:
            temp = current
            path.append((temp.i, temp.j))
            while temp.previous:
                path.append((temp.previous.i, temp.previous.j))
                temp = temp.previous

            print("Done!")

        open_set.remove(current)
        closed_set.append(current)

        neighbours = current.neighbours

        for neighbour in neighbours:
            if neighbour in closed_set:
                continue

            # temp_g is the distance from start to the neighbor through current
            temp_g = current.g + 1
            if neighbour in open_set:
                if temp_g < neighbour.g:
                    neighbour.g = temp_g
            else:

                neighbour.g = temp_g
                open_set.append(neighbour)

            neighbour.previous = current
            neighbour.h = heuristic(neighbour, end)
            neighbour.f = neighbour.g+neighbour.h

    ############################## draw the path #################################

print("Path length : ", len(path))
for p in path:
    cnvs.create_rectangle(p[1]*W+W*.2, p[0]*W+W*.2,
                          p[1] * W+W*.8, p[0]*W+W*.8, fill="#2908FF", outline='')

cnvs.pack()
mainloop()
