# mazesolver

MazeSolver is a Python-based application that generates and solves mazes using a graphical interface built with the `tkinter` library. The project demonstrates concepts such as maze generation, pathfinding, and visualization techniques.

## Features

- **Maze Generation**: Randomly generates mazes of varying sizes using a recursive backtracking algorithm.
- **Maze Visualization**: Displays the maze and its walls using a graphical interface.
- **Pathfinding**: Solves the maze by finding a path from the start to the end, with a visual representation of the solution.

## How It Works

1. **Maze Generation**:
   - The maze is represented as a grid of cells.
   - Walls are created between cells, and a recursive backtracking algorithm is used to "break" walls and create a solvable maze.

2. **Maze Solving**:
   - A depth-first search (DFS) algorithm is used to find a path from the top-left corner to the bottom-right corner of the maze.
   - The solution path is visualized in real-time.
   - The algorithm marks the path taken and backtracks when it encounters dead ends.

3. **Visualization**:
   - The `tkinter` library is used to draw the maze, walls, and solution path on a canvas.

## Project Structure

- **`main.py`**: Contains the core logic for maze generation, solving, and visualization.
- **`tests.py`**: Includes unit tests for validating the functionality of the maze generation and solving algorithms.

## How to Run

1. Ensure you have Python 3 installed on your system.
2. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/IrishBanga/mazesolver.git
   cd mazesolver
   ```
3. Run the application:
   ```bash
   python main.py
   ```
4. A window will open displaying the generated maze. Watch as the maze is solved in real-time!

## Dependencies

- Python 3.x
- `tkinter`

## Testing

To run the unit tests, execute the following command:
```bash
python tests.py
```