import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as FuncAnimation
import shapes

ON = 100
OFF = 0


def calculateNeighbours(r,c,height,width,newGrid):
    neighbour = 0
    if r == 0 and c == 0:
        neighbour += newGrid[r,c+1]
        neighbour += newGrid[r+1,c+1]
        neighbour += newGrid[r+1,c]
    elif r == 0 and c == width-1:
        neighbour += newGrid[r+1,c]
        neighbour += newGrid[r+1,c-1]
        neighbour += newGrid[r,c-1]
    elif r == height-1 and c == width-1:
        neighbour += newGrid[r,c-1]
        neighbour += newGrid[r-1,c-1]
        neighbour += newGrid[r-1,c]
    elif r == height-1 and c == 0:
        neighbour += newGrid[r,c+1]
        neighbour += newGrid[r-1,c]
        neighbour += newGrid[r-1,c+1]
    elif r == 0:
        neighbour += newGrid[r,c+1]
        neighbour += newGrid[r+1,c+1]
        neighbour += newGrid[r+1,c]
        neighbour += newGrid[r+1,c-1]
        neighbour += newGrid[r,c-1]
    elif r == height-1:
        neighbour += newGrid[r,c+1]
        neighbour += newGrid[r,c-1]
        neighbour += newGrid[r-1,c-1]
        neighbour += newGrid[r-1,c]
        neighbour += newGrid[r-1,c+1]
    elif c == 0:
        neighbour += newGrid[r,c+1]
        neighbour += newGrid[r+1,c+1]
        neighbour += newGrid[r+1,c]
        neighbour += newGrid[r-1,c]
        neighbour += newGrid[r-1,c+1]
    elif c == width-1:
        neighbour += newGrid[r+1,c]
        neighbour += newGrid[r+1,c-1]
        neighbour += newGrid[r,c-1]
        neighbour += newGrid[r-1,c-1]
        neighbour += newGrid[r-1,c]
    else:
        neighbour += newGrid[r,c+1]
        neighbour += newGrid[r+1,c+1]
        neighbour += newGrid[r+1,c]
        neighbour += newGrid[r+1,c-1]
        neighbour += newGrid[r,c-1]
        neighbour += newGrid[r-1,c-1]
        neighbour += newGrid[r-1,c]
        neighbour += newGrid[r-1,c+1]
    return neighbour//ON


def switchCell(r,c,neighbourCount,newGrid):
    if neighbourCount == 3:
        newGrid[r,c] = ON
    elif neighbourCount > 3 or neighbourCount < 2:
        newGrid[r,c] = OFF
    return newGrid


def initGrid(gridSize = (100,100), initConfig = []):
    grid = np.zeros((gridSize))
    if len(initConfig) > 0:
        for pt in initConfig:
            grid[pt[0], pt[1]] = ON
    return grid


def calculateNextGeneration(index, img, grid):
    newGrid = np.copy(grid)
    height, width = newGrid.shape
    for r in range(len(newGrid)):
        for c in range(len(newGrid[r])):
            neighbourCount = calculateNeighbours(r,c,height,width,newGrid)
            grid = switchCell(r,c,neighbourCount,grid)
    img.set_data(grid)
    return img


def main():
    print(">> Program initialised")
    grid = initGrid(gridSize=(100,100),initConfig=shapes.getPattern(shapes.FPENTOMINOaACORN,xshift=50,yshift=50))
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = FuncAnimation.FuncAnimation(fig, 
        calculateNextGeneration, fargs=(img, grid),
        frames=11,
        interval=100,
        save_count=50)
    plt.show()
    print(">> Program terminated")


if __name__ == "__main__":
    main()