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
        A = [[float(matrix_entries[i][j].get()) for j in range(int(cols.get()))] for i in range(int(rows.get()))]
        b = [float(rhs_entries[i].get()) for i in range(int(rows.get()))]
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

tk.Label(root, text="Enter number of columns:").pack()
cols = tk.Entry(root)
cols.pack()

tk.Label(root, text="Enter coefficient matrix:").pack()
matrix_frame = tk.Frame(root)
matrix_frame.pack()

matrix_entries = []
rhs_entries = []

def create_matrix_inputs():
    for widget in matrix_frame.winfo_children():
        widget.destroy()
    
    matrix_entries.clear()
    rhs_entries.clear()
    for i in range(int(rows.get())):
        row_entries = []
        for j in range(int(cols.get())):
            entry = tk.Entry(matrix_frame, width=5)
            entry.grid(row=i, column=j)
            row_entries.append(entry)
        matrix_entries.append(row_entries)
        rhs_entry = tk.Entry(matrix_frame, width=5)
        rhs_entry.grid(row=i, column=int(cols.get()))
        rhs_entries.append(rhs_entry)

tk.Button(root, text="Generate Matrix Inputs", command=create_matrix_inputs).pack()
tk.Button(root, text="Solve", command=on_solve).pack()

root.mainloop()

