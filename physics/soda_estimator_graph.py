import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def estimate_soda_packs_per_truck(trailer_volume, trailer_weight_limit, pallet_volume, pallet_weight_limit, soda_pack_weight):
    num_pallets_by_volume = trailer_volume // pallet_volume
    num_pallets_by_weight = trailer_weight_limit // pallet_weight_limit
    num_pallets = min(num_pallets_by_volume, num_pallets_by_weight)
    soda_packs_per_pallet = pallet_weight_limit // soda_pack_weight
    total_soda_packs_per_truck = num_pallets * soda_packs_per_pallet
    return total_soda_packs_per_truck

def calculate_trucks_needed(soda_demand_packs, trailer_volume, trailer_weight_limit, pallet_volume, pallet_weight_limit, soda_pack_weight):
    soda_packs_per_truck = estimate_soda_packs_per_truck(trailer_volume, trailer_weight_limit, pallet_volume, pallet_weight_limit, soda_pack_weight)
    num_trucks_needed = -(-soda_demand_packs // soda_packs_per_truck)
    return num_trucks_needed, soda_packs_per_truck

def on_calculate():
    try:
        trailer_length = float(entry_trailer_length.get())
        trailer_width = float(entry_trailer_width.get())
        trailer_height = float(entry_trailer_height.get())
        trailer_weight_limit = float(entry_trailer_weight_limit.get())
        pallet_length = float(entry_pallet_length.get())
        pallet_width = float(entry_pallet_width.get())
        pallet_height = float(entry_pallet_height.get())
        pallet_weight_limit = float(entry_pallet_weight_limit.get())
        soda_pack_weight = float(entry_soda_pack_weight.get())
        soda_demand_packs = int(entry_soda_demand_packs.get())

        trailer_volume = trailer_length * trailer_width * trailer_height
        pallet_volume = pallet_length * pallet_width * pallet_height

        num_trucks_needed, soda_packs_per_truck = calculate_trucks_needed(
            soda_demand_packs, trailer_volume, trailer_weight_limit,
            pallet_volume, pallet_weight_limit, soda_pack_weight
        )

        messagebox.showinfo("Result", f"Number of trucks needed: {num_trucks_needed}\n"
                                      f"Soda packs per truck: {soda_packs_per_truck}")

        plot_data(num_trucks_needed, soda_packs_per_truck, soda_demand_packs)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def plot_data(num_trucks_needed, soda_packs_per_truck, soda_demand_packs):
    figure = Figure(figsize=(6, 4), dpi=100)
    ax = figure.add_subplot(111)
    labels = ['Trucks Needed', 'Soda Packs per Truck', 'Soda Demand Packs']
    values = [num_trucks_needed, soda_packs_per_truck, soda_demand_packs]
    ax.bar(labels, values, color=['blue', 'green', 'red'])
    ax.set_title('Soda Shipping Estimation')
    ax.set_ylabel('Count')

    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

window = tk.Tk()
window.title("Soda Shipping Estimation")

tk.Label(window, text="Trailer Length (ft):").pack()
entry_trailer_length = tk.Entry(window)
entry_trailer_length.pack()

tk.Label(window, text="Trailer Width (ft):").pack()
entry_trailer_width = tk.Entry(window)
entry_trailer_width.pack()

tk.Label(window, text="Trailer Height (ft):").pack()
entry_trailer_height = tk.Entry(window)
entry_trailer_height.pack()

tk.Label(window, text="Trailer Weight Limit (lbs):").pack()
entry_trailer_weight_limit = tk.Entry(window)
entry_trailer_weight_limit.pack()

tk.Label(window, text="Pallet Length (in):").pack()
entry_pallet_length = tk.Entry(window)
entry_pallet_length.pack()

tk.Label(window, text="Pallet Width (in):").pack()
entry_pallet_width = tk.Entry(window)
entry_pallet_width.pack()

tk.Label(window, text="Pallet Height (in):").pack()
entry_pallet_height = tk.Entry(window)
entry_pallet_height.pack()

tk.Label(window, text="Pallet Weight Limit (lbs):").pack()
entry_pallet_weight_limit = tk.Entry(window)
entry_pallet_weight_limit.pack()

tk.Label(window, text="Soda Pack Weight (lbs):").pack()
entry_soda_pack_weight = tk.Entry(window)
entry_soda_pack_weight.pack()

tk.Label(window, text="Soda Demand Packs:").pack()
entry_soda_demand_packs = tk.Entry(window)
entry_soda_demand_packs.pack()

tk.Button(window, text="Calculate", command=on_calculate).pack()

window.mainloop()

