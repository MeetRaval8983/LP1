import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def process_signup():
    """Handles the sign-up button click event."""
    
    full_name = entry_name.get()
    email = entry_email.get()
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    
    # --- 1. Basic Validation ---
    if not full_name or not email or not username or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required.")
        return
        
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return
        
    # --- 2. Process the Sign-up (Simulation) ---
    # In a real app, you would:
    # - Hash the password
    # - Check if the username or email already exists in the database
    # - Save the new user to the database
    
    print("--- New User Sign-up ---")
    print(f"Full Name: {full_name}")
    print(f"Email: {email}")
    print(f"Username: {username}")
    print(f"Password: [HIDDEN]")
    
    # Show success message and close the window
    messagebox.showinfo("Success", f"Account for '{username}' created successfully!")
    root.destroy()


# --- 1. Main Application Window ---
root = tk.Tk()
root.title("Create New Account")
root.geometry("450x400")
root.resizable(False, False)

style = ttk.Style(root)
style.theme_use('clam')

# Main frame
main_frame = ttk.Frame(root, padding="15")
main_frame.pack(fill=tk.BOTH, expand=True)

# --- 2. Title ---
title_label = ttk.Label(main_frame, text="Sign Up", font=("Helvetica", 18, "bold"))
title_label.pack(pady=(0, 20))

# --- 3. Sign-up Form ---
form_frame = ttk.LabelFrame(main_frame, text="Enter Your Details", padding="15")
form_frame.pack(fill="x", expand=True)
form_frame.columnconfigure(1, weight=1) # Make entry widgets expand

# Full Name
ttk.Label(form_frame, text="Full Name:").grid(row=0, column=0, sticky="w", padx=5, pady=8)
entry_name = ttk.Entry(form_frame)
entry_name.grid(row=0, column=1, sticky="ew", padx=5, pady=8)

# Email
ttk.Label(form_frame, text="Email:").grid(row=1, column=0, sticky="w", padx=5, pady=8)
entry_email = ttk.Entry(form_frame)
entry_email.grid(row=1, column=1, sticky="ew", padx=5, pady=8)

# Username
ttk.Label(form_frame, text="Username:").grid(row=2, column=0, sticky="w", padx=5, pady=8)
entry_username = ttk.Entry(form_frame)
entry_username.grid(row=2, column=1, sticky="ew", padx=5, pady=8)

# Password
ttk.Label(form_frame, text="Password:").grid(row=3, column=0, sticky="w", padx=5, pady=8)
entry_password = ttk.Entry(form_frame, show="*") # Hide password text
entry_password.grid(row=3, column=1, sticky="ew", padx=5, pady=8)

# Confirm Password
ttk.Label(form_frame, text="Confirm Password:").grid(row=4, column=0, sticky="w", padx=5, pady=8)
entry_confirm_password = ttk.Entry(form_frame, show="*") # Hide password text
entry_confirm_password.grid(row=4, column=1, sticky="ew", padx=5, pady=8)

# --- 4. Action Buttons ---
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill="x", pady=(20, 0))
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

# Cancel Button
style.configure('Cancel.TButton', foreground='red')
btn_cancel = ttk.Button(button_frame, text="Cancel", command=root.destroy, style='Cancel.TButton')
btn_cancel.grid(row=0, column=0, sticky="ew", padx=(0, 5))

# Sign Up Button
style.configure('Signup.TButton', font=('Helvetica', 10, 'bold'), foreground='green')
btn_signup = ttk.Button(button_frame, text="Sign Up", command=process_signup, style='Signup.TButton')
btn_signup.grid(row=0, column=1, sticky="ew", padx=(5, 0))


# --- 5. Run the Application ---
root.mainloop()