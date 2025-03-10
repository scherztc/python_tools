import numpy as np
import tkinter as tk
from tkinter import messagebox

def solve_linear_system(A, b):
    """
    Solves the linear system Ax = b for x.
    :param A: Coefficient matrix (n x m)
    :param b: Right-hand side vector (n x 1)
    :return: Solution vector x
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)
    
    try:
        if A.shape[0] == A.shape[1]:  # Square matrix
            x = np.linalg.solve(A, b)
        else:
            x = np.linalg.lstsq(A, b, rcond=None)[0]  # Least squares solution
        
        return x.flatten()
    except np.linalg.LinAlgError:
        return "No unique solution exists. The system may be singular or inconsistent."

def check_linear_independence(A):
    """
    Checks if the rows of matrix A are linearly independent.
    :param A: Coefficient matrix (n x m)
    :return: True if independent, False otherwise
    """
    A = np.array(A, dtype=float)
    rank = np.linalg.matrix_rank(A)
    return rank == min(A.shape)

def on_solve():
    try:
        A = [list(map(float, entry_A.get().split(','))) for _ in range(int(rows.get()))]
        b = list(map(float, entry_b.get().split(',')))
        solution = solve_linear_system(A, b)
        independent = check_linear_independence(A)
        
        if isinstance(solution, str):
            messagebox.showerror("Error", solution)
        else:
            result = "\n".join([f"x{i+1} = {val:.4f}" for i, val in enumerate(solution)])
            result += f"\n\nLinear Independence: {'Yes' if independent else 'No'}"
            messagebox.showinfo("Solution", result)
    except Exception as e:
        messagebox.showerror("Input Error", "Invalid input format. Please enter numeric values correctly.")

root = tk.Tk()
root.title("Linear System Solver")

tk.Label(root, text="Enter number of rows:").pack()
rows = tk.Entry(root)
rows.pack()

tk.Label(root, text="Enter coefficient matrix (comma-separated rows):").pack()
entry_A = tk.Entry(root, width=50)
entry_A.pack()

tk.Label(root, text="Enter right-hand side values (comma-separated):").pack()
entry_b = tk.Entry(root, width=50)
entry_b.pack()

tk.Button(root, text="Solve", command=on_solve).pack()

root.mainloop()

