import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def submit_form():
    """Gathers all data from the form and shows a summary."""
    
    # --- Get Personal Info ---
    full_name = entry_name.get()
    age = spin_age.get()
    gender = combo_gender.get()
    
    # --- Get Contact Info ---
    phone = entry_phone.get()
    email = entry_email.get()
    address = text_address.get("1.0", tk.END).strip() # Get text from 1st char to end
    emergency_name = entry_emergency_name.get()
    emergency_phone = entry_emergency_phone.get()
    
    # --- Get Sports Info ---
    sports = []
    if var_cricket.get():
        sports.append("Cricket")
    if var_football.get():
        sports.append("Football")
    if var_tennis.get():
        sports.append("Tennis")
    if var_swimming.get():
        sports.append("Swimming")
        
    skill_level = var_skill.get()
    medical_notes = entry_medical.get()
    
    # --- Basic Validation ---
    if not full_name or not age or not phone or not sports:
        messagebox.showerror("Error", "Please fill all required fields:\n- Full Name\n- Age\n- Phone\n- At least one sport")
        return
        
    # --- Format the Output Message ---
    sports_str = ", ".join(sports) if sports else "None"
    
    summary = f"""--- Registration Successful ---
    
Full Name: {full_name}
Age: {age}
Gender: {gender}

Phone: {phone}
Email: {email}
Address: {address}

Emergency Contact: {emergency_name} ({emergency_phone})

Selected Sport(s): {sports_str}
Skill Level: {skill_level}
Medical Notes: {medical_notes}
"""
    
    # --- Show Summary in Messagebox ---
    # (In a real app, you'd send this to a database)
    print(summary) # Also print to console for debugging
    messagebox.showinfo("Registration Successful", "Your registration has been submitted!")
    
    # Clear the form after successful submission
    clear_form()

def clear_form():
    """Resets all form fields to their default state."""
    
    # Clear text/entry widgets
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_emergency_name.delete(0, tk.END)
    entry_emergency_phone.delete(0, tk.END)
    entry_medical.delete(0, tk.END)
    
    # Reset spinbox and combobox
    spin_age.set(5) # Set back to minimum age
    combo_gender.set('') # Clear selection
    
    # Clear text widget
    text_address.delete("1.0", tk.END)
    
    # Uncheck all checkbuttons
    var_cricket.set(0)
    var_football.set(0)
    var_tennis.set(0)
    var_swimming.set(0)
    
    # Reset radio button to default
    var_skill.set("Beginner")


# --- Main Application Window Setup ---
root = tk.Tk()
root.title("Sports Academy Registration")
root.geometry("550x700") # Set a good size
root.resizable(False, False) # Don't allow resizing

# Apply a theme
style = ttk.Style(root)
style.theme_use('clam') # 'clam', 'alt', 'default', 'classic'

# Main frame to hold all widgets
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# --- 1. Personal Information Section ---
personal_frame = ttk.LabelFrame(main_frame, text="Personal Information", padding="15")
personal_frame.pack(fill="x", pady=10)
personal_frame.columnconfigure(1, weight=1) # Make entry widgets expand

# Full Name
ttk.Label(personal_frame, text="Full Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_name = ttk.Entry(personal_frame)
entry_name.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

# Age
ttk.Label(personal_frame, text="Age:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
spin_age = ttk.Spinbox(personal_frame, from_=5, to=99, width=5)
spin_age.grid(row=1, column=1, sticky="w", padx=5, pady=5)

# Gender
ttk.Label(personal_frame, text="Gender:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
combo_gender = ttk.Combobox(personal_frame, values=["Male", "Female", "Other", "Prefer not to say"])
combo_gender.grid(row=2, column=1, sticky="w", padx=5, pady=5)

# --- 2. Contact Information Section ---
contact_frame = ttk.LabelFrame(main_frame, text="Contact Details", padding="15")
contact_frame.pack(fill="x", pady=10)
contact_frame.columnconfigure(1, weight=1)

# Phone
ttk.Label(contact_frame, text="Phone:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_phone = ttk.Entry(contact_frame)
entry_phone.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

# Email
ttk.Label(contact_frame, text="Email:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_email = ttk.Entry(contact_frame)
entry_email.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

# Address
ttk.Label(contact_frame, text="Address:").grid(row=2, column=0, sticky="nw", padx=5, pady=5)
text_address = tk.Text(contact_frame, height=3, width=30)
text_address.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

# Emergency Contact Name
ttk.Label(contact_frame, text="Emergency Name:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
entry_emergency_name = ttk.Entry(contact_frame)
entry_emergency_name.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

# Emergency Contact Phone
ttk.Label(contact_frame, text="Emergency Phone:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
entry_emergency_phone = ttk.Entry(contact_frame)
entry_emergency_phone.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

# --- 3. Sports Details Section ---
sports_frame = ttk.LabelFrame(main_frame, text="Sports Details", padding="15")
sports_frame.pack(fill="x", pady=10)
sports_frame.columnconfigure(1, weight=1)

# Sport Selection (Checkbuttons)
ttk.Label(sports_frame, text="Sport(s):").grid(row=0, column=0, sticky="nw", padx=5, pady=5)
check_frame = ttk.Frame(sports_frame)
check_frame.grid(row=0, column=1, sticky="w")

var_cricket = tk.IntVar()
var_football = tk.IntVar()
var_tennis = tk.IntVar()
var_swimming = tk.IntVar()

chk_cricket = ttk.Checkbutton(check_frame, text="Cricket", variable=var_cricket)
chk_cricket.pack(side="left", padx=5)
chk_football = ttk.Checkbutton(check_frame, text="Football", variable=var_football)
chk_football.pack(side="left", padx=5)
chk_tennis = ttk.Checkbutton(check_frame, text="Tennis", variable=var_tennis)
chk_tennis.pack(side="left", padx=5)
chk_swimming = ttk.Checkbutton(check_frame, text="Swimming", variable=var_swimming)
chk_swimming.pack(side="left", padx=5)

# Skill Level (Radiobuttons)
ttk.Label(sports_frame, text="Skill Level:").grid(row=1, column=0, sticky="nw", padx=5, pady=5)
radio_frame = ttk.Frame(sports_frame)
radio_frame.grid(row=1, column=1, sticky="w")

var_skill = tk.StringVar(value="Beginner") # Set a default value

rad_beginner = ttk.Radiobutton(radio_frame, text="Beginner", variable=var_skill, value="Beginner")
rad_beginner.pack(side="left", padx=5)
rad_intermediate = ttk.Radiobutton(radio_frame, text="Intermediate", variable=var_skill, value="Intermediate")
rad_intermediate.pack(side="left", padx=5)
rad_advanced = ttk.Radiobutton(radio_frame, text="Advanced", variable=var_skill, value="Advanced")
rad_advanced.pack(side="left", padx=5)

# Medical Notes
ttk.Label(sports_frame, text="Medical Notes:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_medical = ttk.Entry(sports_frame)
entry_medical.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
ttk.Label(sports_frame, text="(Optional: allergies, conditions, etc.)", font=("Arial", 8, "italic")).grid(row=3, column=1, sticky="w", padx=5)


# --- 4. Submit and Clear Buttons ---
button_frame = ttk.Frame(main_frame, padding="10")
button_frame.pack(fill="x")

# Configure the frame to push buttons to the right
button_frame.columnconfigure(0, weight=1) 
button_frame.columnconfigure(1, weight=1) 

# Clear Button
style.configure('TButton', font=('Helvetica', 12))
style.configure('Clear.TButton', foreground='red') # Custom style
btn_clear = ttk.Button(button_frame, text="Clear", command=clear_form, style='Clear.TButton')
btn_clear.grid(row=0, column=0, sticky="e", padx=10)

# Submit Button
style.configure('Submit.TButton', foreground='green') # Custom style
btn_submit = ttk.Button(button_frame, text="Register", command=submit_form, style='Submit.TButton')
btn_submit.grid(row=0, column=1, sticky="e")


# --- Run the Application ---
root.mainloop()