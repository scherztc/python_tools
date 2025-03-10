import numpy as np
import tkinter as tk
from tkinter import messagebox

def compute_eigenvalues_and_vectors(A):
    """
    Computes the eigenvalues and eigenvectors of a square matrix A.
    """
    A = np.array(A, dtype=float)
    
    if A.shape[0] != A.shape[1]:
        return "Eigenvalues are only defined for square matrices."
    
    try:
        eigenvalues, eigenvectors = np.linalg.eig(A)
        return eigenvalues, eigenvectors
    except np.linalg.LinAlgError:
        return "Error computing eigenvalues. Ensure matrix is square."

def compute_svd(A):
    """
    Computes the Singular Value Decomposition (SVD) of a matrix A.
    """
    A = np.array(A, dtype=float)
    U, S, Vt = np.linalg.svd(A)
    return U, S, Vt

def power_series(A, n):
    """
    Computes the power series sum I + A + A^2 + ... + A^n for square matrices.
    """
    A = np.array(A, dtype=float)
    if A.shape[0] != A.shape[1]:
        return "Power series computation is only valid for square matrices."
    
    I = np.eye(A.shape[0])
    result = I.copy()
    temp = I.copy()
    
    for _ in range(n):
        temp = np.dot(temp, A)
        result += temp
    
    return result

def check_completeness(eigenvectors):
    """
    Checks if the set of eigenvectors forms a complete basis (linear independence).
    """
    rank = np.linalg.matrix_rank(eigenvectors)
    return rank == eigenvectors.shape[0]

def check_superposition(A, eigenvectors):
    """
    Verifies the principle of superposition by reconstructing A from its eigen decomposition.
    """
    try:
        D = np.diag(np.linalg.eigvals(A))
        A_reconstructed = eigenvectors @ D @ np.linalg.inv(eigenvectors)
        return np.allclose(A, A_reconstructed)
    except np.linalg.LinAlgError:
        return False

def on_compute():
    try:
        rows = int(rows_entry.get())
        cols = int(cols_entry.get())
        n = int(series_terms.get())
        A = [[float(matrix_entries[i][j].get()) for j in range(cols)] for i in range(rows)]
        A = np.array(A)
        
        result = "Real-World Analysis:\n"
        
        if A.shape[0] == A.shape[1]:
            eigenvalues, eigenvectors = compute_eigenvalues_and_vectors(A)
            series_result = power_series(A, n)
            completeness = check_completeness(eigenvectors)
            superposition = check_superposition(A, eigenvectors)
            
            result += "\nEigenvalues:\n" + "\n".join(map(str, eigenvalues))
            result += "\n\nEigenvectors:\n" + "\n".join(map(str, eigenvectors.T))
            result += "\n\nPower Series Approximation:\n" + "\n".join([str(row) for row in series_result])
            result += f"\n\nCompleteness Check: {'Yes' if completeness else 'No'}"
            result += f"\nSuperposition Check: {'Valid' if superposition else 'Invalid'}"
        else:
            U, S, Vt = compute_svd(A)
            result += "\nSingular Value Decomposition (SVD):\n"
            result += "\nU:\n" + "\n".join([str(row) for row in U])
            result += "\n\nSingular Values:\n" + "\n".join(map(str, S))
            result += "\n\nVt:\n" + "\n".join([str(row) for row in Vt])
        
        messagebox.showinfo("Results", result)
    except Exception as e:
        messagebox.showerror("Input Error", "Invalid input format. Please enter numeric values correctly.")

root = tk.Tk()
root.title("Real-World Matrix Calculator")

tk.Label(root, text="Enter number of rows (n):").pack()
rows_entry = tk.Entry(root)
rows_entry.pack()

tk.Label(root, text="Enter number of columns (m):").pack()
cols_entry = tk.Entry(root)
cols_entry.pack()

tk.Label(root, text="Enter number of terms for power series (only for square matrices):").pack()
series_terms = tk.Entry(root)
series_terms.pack()

tk.Label(root, text="Enter matrix values:").pack()
matrix_frame = tk.Frame(root)
matrix_frame.pack()

matrix_entries = []

def create_matrix_inputs():
    for widget in matrix_frame.winfo_children():
        widget.destroy()
    
    matrix_entries.clear()
    rows = int(rows_entry.get())
    cols = int(cols_entry.get())
    
    for i in range(rows):
        row_entries = []
        for j in range(cols):
            entry = tk.Entry(matrix_frame, width=5)
            entry.grid(row=i, column=j)
            row_entries.append(entry)
        matrix_entries.append(row_entries)

tk.Button(root, text="Generate Matrix Inputs", command=create_matrix_inputs).pack()
tk.Button(root, text="Compute", command=on_compute).pack()

root.mainloop()

