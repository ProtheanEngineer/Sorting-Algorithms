from tkinter import ttk
import tkinter as tk
from src.bubble_sort import bubble_sort
from src.merge_sort import merge_sort
from src.quick_sort import quick_sort
from src.visualization import generate_random_data, visualize_sorting_algorithm

def on_algorithm_selected(*args):
    selected_algorithm = algorithm_var.get()
    sorting_algorithm = algorithms[selected_algorithm]
    
    # Generate random data for the specified number of bars
    input_data = generate_random_data(num_bars.get())

    # Visualize the sorting algorithm
    visualize_sorting_algorithm(sorting_algorithm, input_data, selected_algorithm)

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    root.title("Sorting Algorithm Visualization")

    # User input for the number of bars
    num_bars = tk.IntVar()
    num_bars.set(10)  # Default number of bars

    # Dropdown for selecting the sorting algorithm
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
    }

    algorithm_var = tk.StringVar()
    algorithm_var.set("Bubble Sort")  # Default sorting algorithm


    algorithm_dropdown = ttk.Combobox(root, textvariable=algorithm_var, values=list(algorithms.keys()))
    algorithm_dropdown.grid(row=0, column=0, padx=10, pady=10)
    algorithm_dropdown.bind("<<ComboboxSelected>>", on_algorithm_selected)

    # Entry for the number of bars
    num_bars_label = tk.Label(root, text="Number of Bars:")
    num_bars_label.grid(row=1, column=0, padx=10, pady=10)

    num_bars_entry = tk.Entry(root, textvariable=num_bars)
    num_bars_entry.grid(row=1, column=1, padx=10, pady=10)

    # Button to start visualization
    visualize_button = tk.Button(root, text="Visualize", command=on_algorithm_selected)
    visualize_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Start the Tkinter event loop
    root.mainloop()
