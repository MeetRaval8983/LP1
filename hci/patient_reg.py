import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText # For a scrollable text widget

def submit_patient_form():
    """Gathers data from the form and displays a summary."""
    
    # --- 1. Get Patient Details ---
    first_name = entry_fname.get()
    last_name = entry_lname.get()
    dob = entry_dob.get()
    gender = combo_gender.get()
    blood_type = combo_blood.get()
    
    # --- 2. Get Contact Details ---
    phone = entry_phone.get()
    email = entry_email.get()
    address = text_address.get("1.0", tk.END).strip()
    
    # --- 3. Get Medical History (Checkbuttons) ---
    history = []
    if var_allergies.get():
        history.append("Allergies")
    if var_diabetes.get():
        history.append("Diabetes")
    if var_hypertension.get():
        history.append("Hypertension")
    
    other_conditions = entry_other_conditions.get()
    if other_conditions:
        history.append(f"Other: {other_conditions}")
        
    history_str = ", ".join(history) if history else "None specified"
    
    # --- 4. Get Visit Details (Listbox) ---
    try:
        selected_indices = listbox_reason.curselection()
        if not selected_indices:
            raise IndexError("No selection")
        visit_reason = listbox_reason.get(selected_indices[0])
    except IndexError:
        messagebox.showerror("Error", "Please select a 'Reason for Visit' from the list.")
        return

    # --- 5. Validation ---
    if not first_name or not last_name or not dob or not phone:
        messagebox.showerror("Error", "Please fill all required fields:\n- First Name\n- Last Name\n- Date of Birth\n- Phone")
        return
        
    # --- 6. Format and Display Summary ---
    summary = f"""--- Patient Registration Summary ---
    
Name: {first_name} {last_name}
Date of Birth: {dob}
Gender: {gender}
Blood Type: {blood_type}

Phone: {phone}
Email: {email}
Address: {address}

Medical History: {history_str}
Reason for Visit: {visit_reason}
"""
    
    messagebox.showinfo("Registration Successful", summary)
    print(summary) # Also print to console
    clear_form()

def clear_form():
    """Clears all entry fields and resets widgets."""
    
    # Clear Entry and Combobox widgets
    entry_fname.delete(0, tk.END)
    entry_lname.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    combo_gender.set('')
    combo_blood.set('')
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_other_conditions.delete(0, tk.END)
    
    # Clear Text widget
    text_address.delete("1.0", tk.END)
    
    # Uncheck Checkbuttons
    var_allergies.set(0)
    var_diabetes.set(0)
    var_hypertension.set(0)
    
    # Deselect Listbox
    listbox_reason.selection_clear(0, tk.END)

# --- Main Application Window ---
root = tk.Tk()
root.title("Patient Registration Form")
root.geometry("600x750")

style = ttk.Style(root)
style.theme_use('clam')

# Main frame to hold content
main_frame = ttk.Frame(root, padding="15")
main_frame.pack(fill=tk.BOTH, expand=True)

# --- Title Label ---
title_label = ttk.Label(main_frame, text="Patient Registration Form", font=("Helvetica", 18, "bold"))
title_label.pack(pady=(0, 15))

# --- Section 1: Patient Details ---
details_frame = ttk.LabelFrame(main_frame, text="Patient Details", padding="10")
details_frame.pack(fill="x", pady=5)
details_frame.columnconfigure(1, weight=1)
details_frame.columnconfigure(3, weight=1)

ttk.Label(details_frame, text="First Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_fname = ttk.Entry(details_frame)
entry_fname.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

ttk.Label(details_frame, text="Last Name:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
entry_lname = ttk.Entry(details_frame)
entry_lname.grid(row=0, column=3, sticky="ew", padx=5, pady=5)

ttk.Label(details_frame, text="Date of Birth:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_dob = ttk.Entry(details_frame)
entry_dob.insert(0, "DD/MM/YYYY")
entry_dob.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

ttk.Label(details_frame, text="Gender:").grid(row=1, column=2, sticky="w", padx=5, pady=5)
combo_gender = ttk.Combobox(details_frame, values=["Male", "Female", "Other"])
combo_gender.grid(row=1, column=3, sticky="ew", padx=5, pady=5)

ttk.Label(details_frame, text="Blood Type:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
combo_blood = ttk.Combobox(details_frame, values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
combo_blood.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

# --- Section 2: Contact Information ---
contact_frame = ttk.LabelFrame(main_frame, text="Contact Information", padding="10")
contact_frame.pack(fill="x", pady=5)
contact_frame.columnconfigure(1, weight=1)

ttk.Label(contact_frame, text="Phone:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_phone = ttk.Entry(contact_frame)
entry_phone.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

ttk.Label(contact_frame, text="Email:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_email = ttk.Entry(contact_frame)
entry_email.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

# --- Using Text widget for Address ---
ttk.Label(contact_frame, text="Address:").grid(row=2, column=0, sticky="nw", padx=5, pady=5)
text_address = tk.Text(contact_frame, height=4, width=40)
text_address.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

# --- Section 3: Medical History (Checkbuttons) ---
medical_frame = ttk.LabelFrame(main_frame, text="Medical History", padding="10")
medical_frame.pack(fill="x", pady=5)

ttk.Label(medical_frame, text="Known Conditions:").grid(row=0, column=0, sticky="w", padx=5, pady=5)

# Frame to hold checkbuttons horizontally
check_frame = ttk.Frame(medical_frame)
check_frame.grid(row=0, column=1, sticky="w")

var_allergies = tk.IntVar()
var_diabetes = tk.IntVar()
var_hypertension = tk.IntVar()

chk_allergies = ttk.Checkbutton(check_frame, text="Allergies", variable=var_allergies)
chk_allergies.pack(side="left", padx=5)
chk_diabetes = ttk.Checkbutton(check_frame, text="Diabetes", variable=var_diabetes)
chk_diabetes.pack(side="left", padx=5)
chk_hypertension = ttk.Checkbutton(check_frame, text="Hypertension", variable=var_hypertension)
chk_hypertension.pack(side="left", padx=5)

ttk.Label(medical_frame, text="Other:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_other_conditions = ttk.Entry(medical_frame)
entry_other_conditions.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

# --- Section 4: Reason for Visit (Listbox) ---
visit_frame = ttk.LabelFrame(main_frame, text="Reason for Visit", padding="10")
visit_frame.pack(fill="x", pady=5)

# Using a standard tk.Listbox
listbox_reason = tk.Listbox(visit_frame, height=5, exportselection=False)
listbox_reason.pack(fill="x", expand=True, padx=5, pady=5)

# Populate the Listbox
reasons = ["General Check-up", "Consultation", "Follow-up", "New Symptoms", "Emergency", "Specialist Referral"]
for reason in reasons:
    listbox_reason.insert(tk.END, reason)

# Add a scrollbar to the Listbox
scrollbar = ttk.Scrollbar(listbox_reason, orient="vertical", command=listbox_reason.yview)
scrollbar.pack(side="right", fill="y")
listbox_reason.config(yscrollcommand=scrollbar.set)

# --- Section 5: Action Buttons ---
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill="x", pady=10)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

style.configure('Clear.TButton', foreground='red')
btn_clear = ttk.Button(button_frame, text="Clear Form", command=clear_form, style='Clear.TButton')
btn_clear.grid(row=0, column=0, sticky="e", padx=(0, 10))

style.configure('Submit.TButton', foreground='green')
btn_submit = ttk.Button(button_frame, text="Submit Registration", command=submit_patient_form, style='Submit.TButton')
btn_submit.grid(row=0, column=1, sticky="w", padx=(10, 0))

# --- Run the Application ---
root.mainloop()