import tkinter as tk
from tkinter import ttk
import random
import time

def find_ride():
    """Simulates finding a ride when the button is clicked."""
    
    # 1. Get values from the input widgets
    pickup = entry_pickup.get()
    drop = entry_drop.get()
    vehicle = vehicle_var.get()
    
    # 2. Clear the output area
    text_output.config(state=tk.NORMAL) # Enable writing
    text_output.delete("1.0", tk.END) # Clear all text
    
    # 3. Validate input
    if not pickup or not drop:
        text_output.insert(tk.END, "Error: Please enter both pickup and drop-off locations.")
        text_output.config(state=tk.DISABLED) # Disable writing
        return

    # 4. Simulate search
    text_output.insert(tk.END, "Finding your ride...\n")
    # Force the UI to update to show the "Finding..." message
    root.update_idletasks() 
    time.sleep(1.5) # Simulate network delay
    
    # 5. --- Simulation ---
    fare = random.randint(80, 450)
    driver_name = random.choice(["Ravi", "Sunita", "Amit", "Priya"])
    
    # 6. Display results
    text_output.delete("1.0", tk.END) # Clear "Finding..." message
    result_text = (
        f"Ride Found!\n"
        f"----------------------------\n"
        f"Driver: {driver_name}\n"
        f"Vehicle: {vehicle}\n"
        f"Estimated Fare: ₹{fare}.00\n"
        f"Booking from '{pickup}' to '{drop}'.\n"
        f"\nDriver is on the way!"
    )
    text_output.insert(tk.END, result_text)
    text_output.config(state=tk.DISABLED) # Disable writing

# --- 1. Set up the Main Window ---
root = tk.Tk()
root.title("Cab/Auto Booking App")
root.geometry("800x500") # Set initial window size
root.minsize(600, 400) # Set minimum window size

# Configure the main window's grid layout
root.columnconfigure(0, weight=1) # Control panel column
root.columnconfigure(1, weight=2) # Map area column
root.rowconfigure(0, weight=1)    # Main row

# --- 2. Create Left Control Frame ---
control_frame = ttk.Frame(root, padding="15")
control_frame.grid(row=0, column=0, sticky="nsew") # Fill the whole cell

# Configure grid layout for the control frame
control_frame.columnconfigure(0, weight=1)
# Add rows as needed, with padding
control_frame.grid_rowconfigure(0, pad=10) # Title
control_frame.grid_rowconfigure(1, pad=5)  # Pickup
control_frame.grid_rowconfigure(2, pad=5)  # Drop
control_frame.grid_rowconfigure(3, pad=10) # Vehicle
control_frame.grid_rowconfigure(4, pad=15) # Button
control_frame.grid_rowconfigure(5, weight=1, pad=10) # Output (expands)

# --- 3. Create Widgets for Control Frame ---

# Title
title_label = ttk.Label(control_frame, text="Cab/Auto Booking", font=("Helvetica", 18, "bold"))
title_label.grid(row=0, column=0, columnspan=2, sticky="w")

# Pickup
pickup_label = ttk.Label(control_frame, text="Pickup:")
pickup_label.grid(row=1, column=0, sticky="w", padx=5)
entry_pickup = ttk.Entry(control_frame, width=30)
entry_pickup.grid(row=1, column=1, sticky="ew", padx=5)

# Drop-off
drop_label = ttk.Label(control_frame, text="Drop-off:")
drop_label.grid(row=2, column=0, sticky="w", padx=5)
entry_drop = ttk.Entry(control_frame, width=30)
entry_drop.grid(row=2, column=1, sticky="ew", padx=5)

# Vehicle Type
vehicle_label = ttk.Label(control_frame, text="Vehicle:")
vehicle_label.grid(row=3, column=0, sticky="w", padx=5)
vehicle_options = ['Auto', 'Cab (Mini)', 'Cab (Sedan)', 'Cab (SUV)']
vehicle_var = tk.StringVar(value=vehicle_options[0])
vehicle_menu = ttk.OptionMenu(control_frame, vehicle_var, *vehicle_options)
vehicle_menu.grid(row=3, column=1, sticky="ew", padx=5)

# Find Ride Button
find_ride_button = ttk.Button(control_frame, text="Find Ride", command=find_ride)
find_ride_button.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=10)

# Output Text Area
output_label = ttk.Label(control_frame, text="Ride Details:")
output_label.grid(row=5, column=0, columnspan=2, sticky="nw", padx=5)

text_output = tk.Text(control_frame, height=10, state=tk.DISABLED, wrap="word", relief="solid", borderwidth=1)
text_output.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=5)

# --- 4. Create Right Map Frame (Placeholder) ---
map_frame = ttk.Frame(root, relief="solid", borderwidth=2)
map_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

map_label = ttk.Label(map_frame, text="Map Placeholder", font=("Helvetica", 14, "italic"), foreground="gray")
map_label.place(relx=0.5, rely=0.5, anchor="center") # Center the label

# --- 5. Start the Application ---
root.mainloop()