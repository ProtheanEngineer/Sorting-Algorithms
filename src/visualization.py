import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import tkinter as tk
from tkinter import ttk
from .bubble_sort import bubble_sort
from .merge_sort import merge_sort
from .quick_sort import quick_sort

def generate_random_data(num_bars):
    return [random.randint(1, 100) for _ in range(num_bars)]

def visualize_sorting_algorithm(algorithm, input_data, algorithm_name):
    # Define a figure and axis for the plot
    fig, ax = plt.subplots()
    # Bar chart initialization
    bars = ax.bar(range(len(input_data)), input_data, align='edge')
    
    start_time = time.time()

    # Function to update the plot for each animation frame
    def update(frame):
        if frame < len(input_data):
            # Perform a sorting step and update the bars
            sorted_data = algorithm(input_data[:frame+1])
            for bar, value in zip(bars, sorted_data):
                bar.set_height(value)

    # Function to update the title with the running time
    def update_title():
        # if frame == len(input_data):
        end_time = time.time()
        duration = end_time - start_time
        ax.set_title(f"{algorithm_name} - Time running: {duration:.6f} seconds")

    # Create the animation
    anim = animation.FuncAnimation(fig, update, frames=len(input_data)+1, repeat=False)
    anim.event_source.add_callback(update_title)

    # Show the plot
    plt.show()
    
def on_algorithm_selected(*args):
    selected_algorithm = algorithm_var.get()
    sorting_algorithm = algorithms[selected_algorithm]

    # Generate random data for the specified number of bars
    input_data = generate_random_data(num_bars.get())

    # Visualize the sorting algorithm
    visualize_sorting_algorithm(sorting_algorithm, input_data)

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
