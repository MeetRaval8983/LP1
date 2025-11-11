import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText # Using ScrolledText for the address

def submit_student_form():
    """Gathers all student data from the form and shows a summary."""
    
    # --- 1. Get Personal Details ---
    first_name = entry_fname.get()
    last_name = entry_lname.get()
    dob = entry_dob.get()
    gender = combo_gender.get()
    
    # --- 2. Get Contact Details ---
    phone = entry_phone.get()
    email = entry_email.get()
    # Get address from the Text widget
    address = text_address.get("1.0", tk.END).strip()
    
    # --- 3. Get Course (from Listbox) ---
    try:
        selected_indices = listbox_course.curselection()
        if not selected_indices:
            raise IndexError("No selection")
        course = listbox_course.get(selected_indices[0])
    except IndexError:
        messagebox.showerror("Error", "Please select a 'Course' from the list.")
        return

    # --- 4. Get Extracurriculars (Checkbuttons) ---
    activities = []
    if var_sports.get():
        activities.append("Sports Club")
    if var_music.get():
        activities.append("Music Club")
    if var_art.get():
        activities.append("Art Club")
    if var_debate.get():
        activities.append("Debate Club")
        
    activities_str = ", ".join(activities) if activities else "None"

    # --- 5. Validation ---
    if not first_name or not last_name or not dob or not phone:
        messagebox.showerror("Error", "Please fill all required fields:\n- First Name\n- Last Name\n- Date of Birth\n- Phone")
        return
        
    if not address:
        messagebox.showerror("Error", "Please enter your 'Home Address'.")
        return

    # --- 6. Format and Display Summary ---
    summary = f"""--- Student Registration Summary ---
    
Name: {first_name} {last_name}
Date of Birth: {dob}
Gender: {gender}

Phone: {phone}
Email: {email}
Address: {address}

Selected Course: {course}
Activities: {activities_str}
"""
    
    messagebox.showinfo("Registration Successful", summary)
    print(summary) # Also print to console
    clear_form()

def clear_form():
    """Clears all form fields."""
    
    # Clear Entry and Combobox
    entry_fname.delete(0, tk.END)
    entry_lname.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_dob.insert(0, "DD/MM/YYYY") # Re-add placeholder
    combo_gender.set('')
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    
    # Clear Text widget
    text_address.delete("1.0", tk.END)
    
    # Deselect Listbox
    listbox_course.selection_clear(0, tk.END)
    
    # Uncheck Checkbuttons
    var_sports.set(0)
    var_music.set(0)
    var_art.set(0)
    var_debate.set(0)

# --- Main Application Window ---
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("600x700")

style = ttk.Style(root)
style.theme_use('clam')

# Main frame to hold content
main_frame = ttk.Frame(root, padding="15")
main_frame.pack(fill=tk.BOTH, expand=True)

# --- Title Label ---
title_label = ttk.Label(main_frame, text="Student Registration Form", font=("Helvetica", 18, "bold"))
title_label.pack(pady=(0, 15))

# --- Section 1: Personal Details ---
personal_frame = ttk.LabelFrame(main_frame, text="Personal Details", padding="10")
personal_frame.pack(fill="x", pady=5)
personal_frame.columnconfigure(1, weight=1)
personal_frame.columnconfigure(3, weight=1)

ttk.Label(personal_frame, text="First Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_fname = ttk.Entry(personal_frame)
entry_fname.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

ttk.Label(personal_frame, text="Last Name:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
entry_lname = ttk.Entry(personal_frame)
entry_lname.grid(row=0, column=3, sticky="ew", padx=5, pady=5)

ttk.Label(personal_frame, text="Date of Birth:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_dob = ttk.Entry(personal_frame)
entry_dob.insert(0, "DD/MM/YYYY")
entry_dob.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

ttk.Label(personal_frame, text="Gender:").grid(row=1, column=2, sticky="w", padx=5, pady=5)
combo_gender = ttk.Combobox(personal_frame, values=["Male", "Female", "Other"])
combo_gender.grid(row=1, column=3, sticky="ew", padx=5, pady=5)

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
ttk.Label(contact_frame, text="Home Address:").grid(row=2, column=0, sticky="nw", padx=5, pady=5)
# Using ScrolledText (a better Text widget) for address
text_address = ScrolledText(contact_frame, height=4, width=40, wrap="word")
text_address.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

# --- Section 3: Academic Details (Listbox) ---
academic_frame = ttk.LabelFrame(main_frame, text="Academic Details", padding="10")
academic_frame.pack(fill="x", pady=5)
academic_frame.columnconfigure(0, weight=1)

ttk.Label(academic_frame, text="Select Course / Major:").pack(anchor="w", padx=5)

# Using a standard tk.Listbox
listbox_course = tk.Listbox(academic_frame, height=5, exportselection=False)
listbox_course.pack(fill="x", expand=True, padx=5, pady=5)

# Populate the Listbox
courses = ["Computer Science", "Mechanical Engineering", "Business Administration", "Physics", "Literature", "Fine Arts"]
for course in courses:
    listbox_course.insert(tk.END, course)

# Add a scrollbar to the Listbox
scrollbar = ttk.Scrollbar(listbox_course, orient="vertical", command=listbox_course.yview)
scrollbar.pack(side="right", fill="y")
listbox_course.config(yscrollcommand=scrollbar.set)

# --- Section 4: Extracurriculars (Checkbuttons) ---
activities_frame = ttk.LabelFrame(main_frame, text="Select Activities", padding="10")
activities_frame.pack(fill="x", pady=5)

var_sports = tk.IntVar()
var_music = tk.IntVar()
var_art = tk.IntVar()
var_debate = tk.IntVar()

chk_sports = ttk.Checkbutton(activities_frame, text="Sports Club", variable=var_sports)
chk_sports.grid(row=0, column=0, sticky="w", padx=10, pady=2)
chk_music = ttk.Checkbutton(activities_frame, text="Music Club", variable=var_music)
chk_music.grid(row=0, column=1, sticky="w", padx=10, pady=2)
chk_art = ttk.Checkbutton(activities_frame, text="Art Club", variable=var_art)
chk_art.grid(row=1, column=0, sticky="w", padx=10, pady=2)
chk_debate = ttk.Checkbutton(activities_frame, text="Debate Club", variable=var_debate)
chk_debate.grid(row=1, column=1, sticky="w", padx=10, pady=2)

# --- Section 5: Action Buttons ---
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill="x", pady=10)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

style.configure('Clear.TButton', foreground='red')
btn_clear = ttk.Button(button_frame, text="Clear Form", command=clear_form, style='Clear.TButton')
btn_clear.grid(row=0, column=0, sticky="e", padx=(0, 10))

style.configure('Submit.TButton', foreground='green')
btn_submit = ttk.Button(button_frame, text="Register", command=submit_student_form, style='Submit.TButton')
btn_submit.grid(row=0, column=1, sticky="w", padx=(10, 0))

# --- Run the Application ---
root.mainloop()