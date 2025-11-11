import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def perform_transfer():
    """Validates and processes the fund transfer."""
    
    from_account = combo_from_account.get()
    to_beneficiary = combo_to_beneficiary.get()
    amount_str = entry_amount.get()
    remarks = entry_remarks.get()
    
    # --- 1. Validation ---
    if not from_account or not to_beneficiary:
        messagebox.showerror("Error", "Please select 'From Account' and 'To Beneficiary'.")
        return

    if from_account == to_beneficiary:
        messagebox.showerror("Error", "'From Account' and 'To Beneficiary' cannot be the same.")
        return

    if not amount_str:
        messagebox.showerror("Error", "Please enter an 'Amount'.")
        return

    try:
        # Try to convert amount to a float
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError("Amount must be positive")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid, positive 'Amount'.")
        return
        
    # --- 2. Confirmation Dialog ---
    confirm_message = (
        f"Please confirm the transfer details:\n\n"
        f"From: {from_account}\n"
        f"To: {to_beneficiary}\n"
        f"Amount: ${amount:.2f}\n\n"
        f"Proceed with the transfer?"
    )
    
    is_confirmed = messagebox.askyesno("Confirm Transfer", confirm_message)
    
    if not is_confirmed:
        messagebox.showinfo("Cancelled", "The transfer was cancelled.")
        return

    # --- 3. Process Transfer (Simulation) ---
    # In a real app, this is where you would call your
    # backend API, interact with a database, etc.
    print(f"Processing transfer: {from_account} -> {to_beneficiary}, ${amount:.2f}, Remarks: {remarks}")
    
    # Simulate success
    messagebox.showinfo("Success", f"Transfer of ${amount:.2f} to {to_beneficiary} was successful!")
    
    # Clear the form
    clear_form()

def clear_form():
    """Resets the form fields."""
    combo_from_account.set('')
    combo_to_beneficiary.set('')
    entry_amount.delete(0, tk.END)
    entry_remarks.delete(0, tk.END)

# --- 1. Main Application Window ---
root = tk.Tk()
root.title("Fund Transfer")
root.geometry("450x380")
root.resizable(False, False)

style = ttk.Style(root)
style.theme_use('clam')

# Main frame
main_frame = ttk.Frame(root, padding="15")
main_frame.pack(fill=tk.BOTH, expand=True)

# --- 2. Title ---
title_label = ttk.Label(main_frame, text="Fund Transfer", font=("Helvetica", 18, "bold"))
title_label.pack(pady=(0, 15))

# --- 3. Transfer Details Form ---
form_frame = ttk.LabelFrame(main_frame, text="Transfer Details", padding="15")
form_frame.pack(fill="x", expand=True)
form_frame.columnconfigure(1, weight=1) # Make widgets expand

# --- Dummy Data for Comboboxes ---
my_accounts = ["Savings (..1234)", "Checking (..5678)"]
beneficiaries = ["Alex Johnson (..4321)", "Maria Garcia (..8765)", "Sam Lee (..1122)"]

# From Account
ttk.Label(form_frame, text="From Account:").grid(row=0, column=0, sticky="w", padx=5, pady=8)
combo_from_account = ttk.Combobox(form_frame, values=my_accounts, state="readonly")
combo_from_account.grid(row=0, column=1, sticky="ew", padx=5, pady=8)

# To Beneficiary
ttk.Label(form_frame, text="To Beneficiary:").grid(row=1, column=0, sticky="w", padx=5, pady=8)
combo_to_beneficiary = ttk.Combobox(form_frame, values=beneficiaries, state="readonly")
combo_to_beneficiary.grid(row=1, column=1, sticky="ew", padx=5, pady=8)

# Amount
ttk.Label(form_frame, text="Amount ($):").grid(row=2, column=0, sticky="w", padx=5, pady=8)
entry_amount = ttk.Entry(form_frame)
entry_amount.grid(row=2, column=1, sticky="ew", padx=5, pady=8)

# Remarks
ttk.Label(form_frame, text="Remarks:").grid(row=3, column=0, sticky="w", padx=5, pady=8)
entry_remarks = ttk.Entry(form_frame)
entry_remarks.grid(row=3, column=1, sticky="ew", padx=5, pady=8)

# --- 4. Action Buttons ---
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill="x", pady=(15, 0))
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

# Cancel Button
style.configure('Cancel.TButton', foreground='red')
btn_cancel = ttk.Button(button_frame, text="Cancel", command=root.destroy, style='Cancel.TButton')
btn_cancel.grid(row=0, column=0, sticky="e", padx=(0, 5))

# Transfer Button
style.configure('Transfer.TButton', font=('Helvetica', 10, 'bold'), foreground='green')
btn_transfer = ttk.Button(button_frame, text="Transfer Funds", command=perform_transfer, style='Transfer.TButton')
btn_transfer.grid(row=0, column=1, sticky="w", padx=(5, 0))


# --- 5. Run the Application ---
root.mainloop()