import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def calculate_lens_properties():
    try:
        n = float(entry_n.get())
        R1 = float(entry_R1.get())
        R2 = float(entry_R2.get())
        d = float(entry_d.get())
        
        f = (n-1)*(1/R1-1/R2)
        fd = (n-1)*(1/R1-1/R2+(n-1)*d/(n*R1*R2))
        K = (fd-f)/fd

        result_text = ""
        if K > .01:
            result_text += 'This is not a thin lens\n'
        else:
            result_text += 'This is a thin lens\n'
            S1 = R1/(n-1)
            S2 = -R2/(n-1)
            M0 = -S2/S1

            if (f > 0 and M0 < 0):
                result_text += 'The converging system produces an upside-down real image\n'
            elif (f > 0 and M0 > 0):
                result_text += 'The converging system produces an upright virtual image\n'
            elif (f < 0 and M0 < 0):
                result_text += 'The diverging system produces an upside-down real image\n'
            elif (f < 0 and M0 > 0):
                result_text += 'The diverging system produces an upright virtual image\n'

            if (abs(M0) > 1):
                result_text += 'The image is bigger than the object\n'
            elif (abs(M0) < 1):
                result_text += 'The image is smaller than the object\n'
            else:
                result_text += 'The image is the same size as the object\n'

        messagebox.showinfo("Lens Properties", result_text)
        
        plot_lens_graph(R1, R2, f)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

def plot_lens_graph(R1, R2, f):
    fig, ax = plt.subplots()
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

    lens_x = [-R1, 0, R2]
    lens_y = [0, 0, 0]
    ax.plot(lens_x, lens_y, 'bo-', label="Lens Surfaces")

    # Drawing a simple ray diagram
    ray_x = [R1, 0, R2]
    ray_y = [2, 0, -2]
    ax.plot(ray_x, ray_y, 'r--', label="Ray Path")

    ax.set(xlabel='Position', ylabel='Height',
           title='Lens and Ray Diagram')
    ax.legend()

    plt.show()

# Create the GUI window
root = tk.Tk()
root.title("Lens Property Calculator")

tk.Label(root, text="Refraction index of the lens material (n)").grid(row=0)
tk.Label(root, text="First radius of curvature of the lens surface (R1)").grid(row=1)
tk.Label(root, text="Second radius of curvature of the lens surface (R2)").grid(row=2)
tk.Label(root, text="Thickness of the lens (d)").grid(row=3)

entry_n = tk.Entry(root)
entry_R1 = tk.Entry(root)
entry_R2 = tk.Entry(root)
entry_d = tk.Entry(root)

entry_n.grid(row=0, column=1)
entry_R1.grid(row=1, column=1)
entry_R2.grid(row=2, column=1)
entry_d.grid(row=3, column=1)

tk.Button(root, text='Calculate', command=calculate_lens_properties).grid(row=4, column=1, pady=4)

root.mainloop()

