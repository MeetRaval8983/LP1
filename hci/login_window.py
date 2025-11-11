import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def process_login():
    """Validates the login credentials."""
    
    username = entry_username.get()
    password = entry_password.get()
    
    # --- 1. Basic Validation ---
    if not username or not password:
        messagebox.showerror("Login Failed", "Please enter both username and password.")
        return
        
    # --- 2. Authenticate (Simulation) ---
    # In a real app, you would check this against a database.
    # We'll simulate a successful login for a specific user.
    
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        # In a real app, you would close this window (root.destroy())
        # and open your main application.
        root.destroy()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def open_signup_window():
    """
    Placeholder function.
    In a real app, this would close the login window
    and open the sign-up window you created.
    """
    messagebox.showinfo("Sign Up", "This would open the Sign-Up window.")
    # You could destroy this root and launch the signup_app.py
    # or use a more advanced structure like Toplevel.

# --- 1. Main Application Window ---
root = tk.Tk()
root.title("Login")
root.geometry("400x350")
root.resizable(False, False)

style = ttk.Style(root)
style.theme_use('clam')

# Main frame
main_frame = ttk.Frame(root, padding="15")
main_frame.pack(fill=tk.BOTH, expand=True)

# --- 2. Title ---
title_label = ttk.Label(main_frame, text="User Login", font=("Helvetica", 18, "bold"))
title_label.pack(pady=(0, 20))

# --- 3. Login Form ---
form_frame = ttk.LabelFrame(main_frame, text="Enter Your Credentials", padding="15")
form_frame.pack(fill="x", expand=True)
form_frame.columnconfigure(1, weight=1) # Make entry widgets expand

# Username
ttk.Label(form_frame, text="Username:").grid(row=0, column=0, sticky="w", padx=5, pady=8)
entry_username = ttk.Entry(form_frame)
entry_username.grid(row=0, column=1, sticky="ew", padx=5, pady=8)

# Password
ttk.Label(form_frame, text="Password:").grid(row=1, column=0, sticky="w", padx=5, pady=8)
entry_password = ttk.Entry(form_frame, show="*") # Hide password text
entry_password.grid(row=1, column=1, sticky="ew", padx=5, pady=8)

# --- 4. Action Buttons ---
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill="x", pady=(20, 0))
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

# Cancel Button
style.configure('Cancel.TButton', foreground='red')
btn_cancel = ttk.Button(button_frame, text="Cancel", command=root.destroy, style='Cancel.TButton')
btn_cancel.grid(row=0, column=0, sticky="ew", padx=(0, 5))

# Login Button
style.configure('Login.TButton', font=('Helvetica', 10, 'bold'), foreground='green')
btn_login = ttk.Button(button_frame, text="Login", command=process_login, style='Login.TButton')
btn_login.grid(row=0, column=1, sticky="ew", padx=(5, 0))

# --- 5. Sign-up Link ---
# Using a "Toolbutton" style to make it look like a link
style.configure('Link.TButton', font=('Helvetica', 9, 'underline'), foreground='blue')
# Remove all padding/borders to make it look like text
style.map('Link.TButton',
    background=[('active', '!disabled', 'SystemButtonFace')],
    bordercolor=[('active', 'SystemButtonFace')],
    lightcolor=[('active', 'SystemButtonFace')],
    darkcolor=[('active', 'SystemButtonFace')],
    relief=[('active', 'flat')]
)

signup_button = ttk.Button(
    main_frame, 
    text="Need an account? Sign Up", 
    style='Link.TButton', 
    command=open_signup_window
)
signup_button.pack(pady=(15, 0))

# --- 6. Run the Application ---
root.mainloop()
