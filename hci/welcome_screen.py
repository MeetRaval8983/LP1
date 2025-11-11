import tkinter as tk
from tkinter import ttk
import sys

def start_application():
    """
    This function is a placeholder.
    In a real app, you would close this window (root.destroy()) 
    and open your main application window.
    """
    print("Starting the main application...")
    # For this demo, we'll just close the welcome screen.
    root.destroy()

def exit_application():
    """Closes the application."""
    print("Exiting application.")
    root.destroy()

# --- 1. Set up the Main Window ---
root = tk.Tk()
root.title("Welcome")
root.geometry("450x300")  # Set a nice size
root.resizable(False, False) # Keep a fixed window size
root.configure(bg='#f0f0f0') # Set a light background color

# Center the window on the screen
root.eval('tk::PlaceWindow . center')

# --- 2. Configure Styles ---
style = ttk.Style(root)
style.theme_use('clam') # Use a modern theme

# Style for the main frame
style.configure('Main.TFrame', background='#f0f0f0')

# Style for the title label
style.configure('Title.TLabel', 
                background='#f0f0f0', 
                foreground='#333', 
                font=('Helvetica', 26, 'bold'))

# Style for the subtitle label
style.configure('Subtitle.TLabel', 
                background='#f0f0f0', 
                foreground='#555', 
                font=('Helvetica', 12, 'italic'))

# Style for the "Start" button
style.configure('Start.TButton', 
                font=('Helvetica', 12, 'bold'),
                foreground='green',
                padding=10)

# Style for the "Exit" button
style.configure('Exit.TButton', 
                font=('Helvetica', 12),
                padding=10)

# --- 3. Create Widgets ---

# Main frame to hold all content
main_frame = ttk.Frame(root, style='Main.TFrame')
# Use pack to fill the window and allow vertical centering
main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

# --- Top Frame for Labels (to center them) ---
label_frame = ttk.Frame(main_frame, style='Main.TFrame')
label_frame.pack(side=tk.TOP, expand=True)

# Welcome Title
title_label = ttk.Label(label_frame, 
                        text="Welcome!", 
                        style='Title.TLabel')
title_label.pack(pady=(20, 10)) # Add padding (top, bottom)

# Subtitle
subtitle_label = ttk.Label(label_frame, 
                           text="to My Awesome Application", 
                           style='Subtitle.TLabel')
subtitle_label.pack(pady=(0, 20))

# --- Bottom Frame for Buttons ---
button_frame = ttk.Frame(main_frame, style='Main.TFrame')
button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 20))

# Configure button frame columns to make buttons expand equally
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

# "Get Started" Button
start_button = ttk.Button(button_frame, 
                          text="Get Started", 
                          style='Start.TButton',
                          command=start_application)
start_button.grid(row=0, column=0, sticky="ew", padx=(0, 5))

# "Exit" Button
exit_button = ttk.Button(button_frame, 
                         text="Exit",
                         style='Exit.TButton', 
                         command=exit_application)
exit_button.grid(row=0, column=1, sticky="ew", padx=(5, 0))


# --- 4. Run the Application ---
root.mainloop()