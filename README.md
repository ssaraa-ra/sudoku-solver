# 🧩 Sudoku Solver (Backtracking Algorithm)

This project implements a classic **Sudoku solver** in Python using the **backtracking** method. The puzzle is embedded directly in the code, and the program attempts to solve it step by step.

---

##  How It Works

The solver uses the backtracking algorithm.
Each empty cell (represented as `0`) is tested with numbers `1-9`, skipping values that break Sudoku rules. If no number works, the algorithm backtracks and changes the previous guess.

---

## Features

- Solves any 9x9 Sudoku puzzle (as long as it's valid and has a solution)
- Pure Python, no external libraries

---

## Example Puzzle (inside the code)

```python
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 7, 2, 1, 9, 5, 0, 0, 0],
    [1, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 8, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
```
## Running the Solver

1. Clone or download the project.

2. Open sudoku_solver.py.

3. Run the script:

```bash
python sudoku_solver.py
```
It will output the solved puzzle (if solvable) in the terminal.

