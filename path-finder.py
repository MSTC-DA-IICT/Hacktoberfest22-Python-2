import numpy as np
from tkinter import *
from PIL import Image
import time


img = Image.open("images/m2.png")
W = 10
rows = img.height
cols = img.width

maze = np.array(img)
maze = np.delete(maze, 3, axis=2)
maze = np.round(maze.mean(axis=2)/255)

root = Tk()
root.resizable(False, False)
cnvs = Canvas(root, bg="white", width=cols *
              W, height=rows*W, borderwidth=0)


def draw_rect(i, j, clr):
    cnvs.create_rectangle(j*W, i*W, j*W+W, i*W+W, fill=clr, outline='')


for j in range(cols):
    for i in range(rows):
        if not maze[i, j]:
            draw_rect(i, j, "black")

start = (0, cols//2-1)
end = (rows-1, cols//2+1)
draw_rect(start[0], start[1], "blue")
draw_rect(end[0], end[1], "green")


path = []
visited = np.zeros(maze.shape)
current = start


def is_available(i, j):
    return i >= 0 and i < rows and j >= 0 and j < cols and maze[i][j] == 1


while (current != end):
    visited[current[0], current[1]] = 1
    neighbours = []
    i, j = current

    if (is_available(i, j+1) and not visited[i, j+1]):
        neighbours.append((i, j+1))
    if (is_available(i, j-1) and not visited[i, j-1]):
        neighbours.append((i, j-1))
    if (is_available(i+1, j) and not visited[i+1, j]):
        neighbours.append((i+1, j))
    if (is_available(i-1, j) and not visited[i-1, j]):
        neighbours.append((i-1, j))

    # print(len(neighbours))
    if (len(neighbours) > 0):
        path.append(current)
        n = neighbours[0]
        current = n
    else:
        current = path.pop()

for p in path:
    cnvs.create_rectangle(p[1]*W+W*.2, p[0]*W+W*.2, p[1]*W+W*.8, p[0]*W+W*.8, fill="#2908FF", outline='')


cnvs.pack()
mainloop()
