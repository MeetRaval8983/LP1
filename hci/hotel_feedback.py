import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText # Use ScrolledText for comments

def submit_feedback():
    """Gathers all data from the form and shows a summary."""
    
    # --- 1. Get Customer Details ---
    full_name = entry_name.get()
    room_number = entry_room.get()
    visit_date = entry_date.get()
    meal_type = combo_meal.get()
    
    # --- 2. Get Ratings ---
    overall_rating = var_rating.get()
    
    # --- 3. Get Items Tried (Checkbuttons) ---
    items_tried = []
    if var_appetizer.get():
        items_tried.append("Appetizers")
    if var_main_course.get():
        items_tried.append("Main Course")
    if var_dessert.get():
        items_tried.append("Dessert")
    if var_beverages.get():
        items_tried.append("Beverages")
        
    items_str = ", ".join(items_tried) if items_tried else "None specified"

    # --- 4. Get Comments (Text) ---
    positive_comments = text_positive.get("1.0", tk.END).strip()
    improvement_comments = text_improve.get("1.0", tk.END).strip()
    
    # --- 5. Validation ---
    if not full_name:
        messagebox.showerror("Error", "Please enter your Full Name.")
        return
        
    if overall_rating == 0: # 0 is the default "unset" value
        messagebox.showerror("Error", "Please select an Overall Rating.")
        return

    # --- 6. Format and Display Summary ---
    summary = f"""--- Feedback Submitted ---
    
Name: {full_name}
Room #: {room_number}
Date: {visit_date}
Meal: {meal_type}

Overall Rating: {overall_rating} / 5
Items Tried: {items_str}

Positive Feedback:
{positive_comments}

Areas for Improvement:
{improvement_comments}
"""
    
    messagebox.showinfo("Thank You!", "Your feedback has been successfully submitted!")
    print(summary) # Also print to console
    clear_form()

def clear_form():
    """Clears all form fields."""
    entry_name.delete(0, tk.END)
    entry_room.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_date.insert(0, "DD/MM/YYYY") # Re-add placeholder
    
    combo_meal.set('')
    var_rating.set(0) # Reset radio button
    
    var_appetizer.set(0)
    var_main_course.set(0)
    var_dessert.set(0)
    var_beverages.set(0)
    
    text_positive.delete("1.0", tk.END)
    text_improve.delete("1.0", tk.END)

# --- Main Application Window ---
root = tk.Tk()
root.title("Hotel Food Feedback Form")
root.geometry("550x700")

style = ttk.Style(root)
style.theme_use('clam')

# --- Main Frame ---
main_frame = ttk.Frame(root, padding="15")
main_frame.pack(fill=tk.BOTH, expand=True)

# --- Title Label ---
title_label = ttk.Label(main_frame, text="Food Feedback Form", font=("Helvetica", 18, "bold"))
title_label.pack(pady=(0, 15))

# --- Section 1: Customer Details ---
details_frame = ttk.LabelFrame(main_frame, text="Your Details", padding="10")
details_frame.pack(fill="x", pady=5)
details_frame.columnconfigure(1, weight=1)

ttk.Label(details_frame, text="Full Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_name = ttk.Entry(details_frame)
entry_name.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

ttk.Label(details_frame, text="Room #:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_room = ttk.Entry(details_frame)
entry_room.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

ttk.Label(details_frame, text="Date of Visit:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_date = ttk.Entry(details_frame)
entry_date.insert(0, "DD/MM/YYYY")
entry_date.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

# --- Section 2: Meal & Rating ---
meal_frame = ttk.LabelFrame(main_frame, text="Meal Details", padding="10")
meal_frame.pack(fill="x", pady=5)
meal_frame.columnconfigure(1, weight=1)

ttk.Label(meal_frame, text="Meal Type:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
combo_meal = ttk.Combobox(meal_frame, values=["Breakfast", "Lunch", "Dinner", "Room Service", "Other"])
combo_meal.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

ttk.Label(meal_frame, text="Overall Rating:").grid(row=1, column=0, sticky="w", padx=5, pady=5)

# Frame to hold radio buttons
radio_frame = ttk.Frame(meal_frame)
radio_frame.grid(row=1, column=1, sticky="ew")

var_rating = tk.IntVar()
for i in range(1, 6): # Create 5 radio buttons (1 to 5)
    rb = ttk.Radiobutton(radio_frame, text=str(i), variable=var_rating, value=i)
    rb.pack(side="left", padx=5)

# --- Section 3: Items Tried (Checkbuttons) ---
items_frame = ttk.LabelFrame(main_frame, text="What did you try? (Check all that apply)", padding="10")
items_frame.pack(fill="x", pady=5)

var_appetizer = tk.IntVar()
var_main_course = tk.IntVar()
var_dessert = tk.IntVar()
var_beverages = tk.IntVar()

chk_appetizer = ttk.Checkbutton(items_frame, text="Appetizers", variable=var_appetizer)
chk_appetizer.grid(row=0, column=0, sticky="w", padx=10)
chk_main_course = ttk.Checkbutton(items_frame, text="Main Course", variable=var_main_course)
chk_main_course.grid(row=0, column=1, sticky="w", padx=10)
chk_dessert = ttk.Checkbutton(items_frame, text="Dessert", variable=var_dessert)
chk_dessert.grid(row=1, column=0, sticky="w", padx=10)
chk_beverages = ttk.Checkbutton(items_frame, text="Beverages", variable=var_beverages)
chk_beverages.grid(row=1, column=1, sticky="w", padx=10)

# --- Section 4: Comments (Text) ---
comments_frame = ttk.LabelFrame(main_frame, text="Your Comments", padding="10")
comments_frame.pack(fill="both", expand=True, pady=5)
comments_frame.columnconfigure(0, weight=1)
comments_frame.rowconfigure(1, weight=1) # Make text boxes expand
comments_frame.rowconfigure(3, weight=1)

ttk.Label(comments_frame, text="What did you like?").grid(row=0, column=0, sticky="w", padx=5, pady=(0,5))
text_positive = ScrolledText(comments_frame, height=5, width=50, wrap="word")
text_positive.grid(row=1, column=0, sticky="nsew", padx=5)

ttk.Label(comments_frame, text="What can we improve?").grid(row=2, column=0, sticky="w", padx=5, pady=(10,5))
text_improve = ScrolledText(comments_frame, height=5, width=50, wrap="word")
text_improve.grid(row=3, column=0, sticky="nsew", padx=5)

# --- Section 5: Action Buttons ---
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill="x", pady=(10, 0))
button_frame.columnconfigure(0, weight=1) # Spacer

style.configure('Clear.TButton', foreground='red')
btn_clear = ttk.Button(button_frame, text="Clear", command=clear_form, style='Clear.TButton')
btn_clear.grid(row=0, column=1, sticky="e", padx=5)

style.configure('Submit.TButton', foreground='green')
btn_submit = ttk.Button(button_frame, text="Submit Feedback", command=submit_feedback, style='Submit.TButton')
btn_submit.grid(row=0, column=2, sticky="e", padx=5)

# --- Run the Application ---
root.mainloop()