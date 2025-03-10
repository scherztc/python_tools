import numpy as np
import tkinter as tk
from tkinter import messagebox

def compute_eigenvalues_and_vectors(A):
    """
    Computes the eigenvalues and eigenvectors of matrix A.
    :param A: Square matrix (n x n)
    :return: Eigenvalues and eigenvectors
    """
    A = np.array(A, dtype=float)
    
    try:
        eigenvalues, eigenvectors = np.linalg.eig(A)
        return eigenvalues, eigenvectors
    except np.linalg.LinAlgError:
        return "Error computing eigenvalues. Ensure matrix is square."

def power_series(A, n):
    """
    Computes the power series sum I + A + A^2 + ... + A^n.
    :param A: Square matrix (n x n)
    :param n: Number of terms in the series
    :return: Summed matrix
    """
    A = np.array(A, dtype=float)
    I = np.eye(A.shape[0])
    result = I.copy()
    temp = I.copy()
    
    for _ in range(n):
        temp = np.dot(temp, A)
        result += temp
    
    return result

def on_compute():
    try:
        A = [[float(matrix_entries[i][j].get()) for j in range(int(size.get()))] for i in range(int(size.get()))]
        n = int(series_terms.get())
        eigenvalues, eigenvectors = compute_eigenvalues_and_vectors(A)
        series_result = power_series(A, n)
        
        result = "Eigenvalues:\n" + "\n".join(map(str, eigenvalues))
        result += "\n\nEigenvectors:\n" + "\n".join(map(str, eigenvectors.T))
        result += "\n\nPower Series Result:\n" + "\n".join([str(row) for row in series_result])
        
        messagebox.showinfo("Results", result)
    except Exception as e:
        messagebox.showerror("Input Error", "Invalid input format. Please enter numeric values correctly.")

root = tk.Tk()
root.title("Eigenvalues & Power Series Calculator")

tk.Label(root, text="Enter matrix size (n x n):").pack()
size = tk.Entry(root)
size.pack()

tk.Label(root, text="Enter number of terms for power series:").pack()
series_terms = tk.Entry(root)
series_terms.pack()

tk.Label(root, text="Enter square matrix:").pack()
matrix_frame = tk.Frame(root)
matrix_frame.pack()

matrix_entries = []

def create_matrix_inputs():
    for widget in matrix_frame.winfo_children():
        widget.destroy()
    
    matrix_entries.clear()
    for i in range(int(size.get())):
        row_entries = []
        for j in range(int(size.get())):
            entry = tk.Entry(matrix_frame, width=5)
            entry.grid(row=i, column=j)
            row_entries.append(entry)
        matrix_entries.append(row_entries)

tk.Button(root, text="Generate Matrix Inputs", command=create_matrix_inputs).pack()
tk.Button(root, text="Compute", command=on_compute).pack()

root.mainloop()

