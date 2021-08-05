import numpy as np


BLINKER = np.array([[1],
                    [1],
                    [1]])
BOAT = np.array([[1,1,0],
                [1,0,1],
                [0,1,0]])
GLIDER = np.array([[1,1,1],
                    [1,0,0],
                    [0,1,0]])
FPENTOMINO = np.array([[0,1,1],
                        [1,1,0],
                        [0,1,0]])
ACORN = np.array([[0,1,0,0,0,0,0],
                    [0,0,0,1,0,0,0],
                    [1,1,0,0,1,1,1]])
FPENTOMINOaACORN = np.array([[0,1,0,0,0,0,0,0,0,0,1,1],
                            [0,0,0,1,0,0,0,0,0,1,1,0],
                            [1,1,0,0,1,1,1,0,0,0,1,0]])


def getPattern(arr,xshift=0,yshift=0):
    pattern = np.array([],dtype='i')
    pattern.shape = (0,2)
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if arr[r,c] == 1:
                pattern = np.append(pattern,[[r+xshift,c+yshift]],axis=0)
    return pattern

if __name__ == "__main__":
    print(getPattern(BLINKER))
