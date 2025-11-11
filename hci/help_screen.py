import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def send_support_message():
    """Placeholder function for sending a support message."""
    
    name = entry_name.get()
    email = entry_email.get()
    message = text_message.get("1.0", tk.END).strip()
    
    if not name or not email or not message:
        messagebox.showerror("Error", "Please fill all fields (Name, Email, Message).")
        return
        
    # --- In a real app, send this data to a support system ---
    print("--- Support Message Sent ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")
    print("------------------------------")
    
    messagebox.showinfo("Message Sent", "Your support request has been sent! We will get back to you shortly.")
    
    # Clear the form
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    text_message.delete("1.S", tk.END)

# --- 1. Set up the Main Window ---
root = tk.Tk()
root.title("Help & Support")
root.geometry("550x450")
root.minsize(450, 350)

style = ttk.Style(root)
style.theme_use('clam')

# --- 2. Create Main Title ---
title_label = ttk.Label(root, text="Help & Support", font=("Helvetica", 18, "bold"), padding=(10, 10))
title_label.pack()

# --- 3. Create the Notebook (Tabbed Interface) ---
notebook = ttk.Notebook(root, padding=(10, 10))
notebook.pack(fill="both", expand=True)

# --- 4. Create "FAQ" Tab ---
faq_frame = ttk.Frame(notebook, padding="15")
notebook.add(faq_frame, text="   FAQ   ")

# --- Content for FAQ Tab ---
# We use a read-only Text widget to make it easy to add/format text
faq_text = tk.Text(faq_frame, wrap="word", height=15, width=50, font=("Helvetica", 10), relief="flat", background=root.cget('bg'))
faq_text.pack(fill="both", expand=True)

# Define tags for formatting
faq_text.tag_configure("question", font=("Helvetica", 11, "bold"), spacing1=10)
faq_text.tag_configure("answer", font=("Helvetica", 10), spacing3=10, lmargin1=15)

# Insert FAQ content
faq_text.insert(tk.END, "How do I reset my password?\n", "question")
faq_text.insert(tk.END, "Go to the 'Settings' menu and click on 'Reset Password'. You will receive an email with instructions.\n", "answer")

faq_text.insert(tk.END, "Where can I find my subscription details?\n", "question")
faq_text.insert(tk.END, "Visit the 'Account' > 'Subscription' page to see your current plan and billing history.\n", "answer")

faq_text.insert(tk.END, "How do I update the app?\n", "question")
faq_text.insert(tk.END, "The application checks for updates automatically. If an update is available, you will be notified on the main screen.\n", "answer")

# Make the text widget read-only
faq_text.config(state="disabled")

# --- 5. Create "Contact Support" Tab ---
contact_frame = ttk.Frame(notebook, padding="15")
notebook.add(contact_frame, text=" Contact Support ")

contact_frame.columnconfigure(1, weight=1) # Make entry widgets expand

# Contact Form
ttk.Label(contact_frame, text="Send us a message:", font=("Helvetica", 12, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

ttk.Label(contact_frame, text="Your Name:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_name = ttk.Entry(contact_frame)
entry_name.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

ttk.Label(contact_frame, text="Your Email:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_email = ttk.Entry(contact_frame)
entry_email.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

ttk.Label(contact_frame, text="Message:").grid(row=3, column=0, sticky="nw", padx=5, pady=5)
text_message = tk.Text(contact_frame, height=6, width=40)
text_message.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

btn_send = ttk.Button(contact_frame, text="Send Message", command=send_support_message)
btn_send.grid(row=4, column=1, sticky="e", padx=5, pady=10)

# --- 6. Create Close Button ---
close_button = ttk.Button(root, text="Close", command=root.destroy)
close_button.pack(pady=10)

# --- 7. Run the Application ---
root.mainloop()