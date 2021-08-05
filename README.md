# Conway's Game of Life
Implementation of John Conway's game of life in python  
by [Debashish Gogoi](https://github.com/Devzard)

To run
> python main.py

Initial states are defined in 'shapes.py'.  
To create your own initial shape create a 2D numpy array with activate boxes denoted as 1 and inactive boxes as 0.  

To change the initial shape change <mark>shapes.< new-shape-name ></mark> to the new shape defined in 'shapes.py' in 'main.py' at
```python
def main():
    ...
    grid = initGrid(gridSize=(100,100),initConfig=shapes.getPattern(shapes.FPENTOMINOaACORN,xshift=50,yshift=50))
    ...
```