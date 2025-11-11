import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

# --- 1. Quiz Data ---
# A list of dictionaries, where each dictionary is a question.
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "correct_index": 2,
    },
    {
        "question": "What does 'CPU' stand for?",
        "options": ["Central Processing Unit", "Computer Personal Unit", "Central Program Unit", "Control Process Unit"],
        "correct_index": 0,
    },
    {
        "question": "Which of these is NOT a programming language?",
        "options": ["Python", "Java", "HTML", "C++"],
        "correct_index": 2,
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "correct_index": 2,
    }
]

# --- 2. Global Variables ---
current_question_index = 0
user_answers = []
score = 0

# --- 3. Functions ---

def start_quiz():
    """Starts the quiz after the terms are accepted."""
    if var_terms.get() == 0:
        messagebox.showerror("Error", "You must accept the terms to start the quiz.")
        return
    
    # Hide welcome frame, show quiz frame
    welcome_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    
    # Load the first question
    show_question(current_question_index)

def show_question(index):
    """Displays the question and options for the given index."""
    global current_question_index
    current_question_index = index
    
    # Clear previous selection
    selected_option.set(-1) 
    
    # Get question data
    question_data = quiz_data[index]
    
    # Update question labels
    question_number_label.config(text=f"Question {index + 1} of {len(quiz_data)}")
    question_label.config(text=question_data["question"])
    
    # Update radio button options
    for i, option in enumerate(question_data["options"]):
        option_radios[i].config(text=option, value=i)
        
    # Update button text on the last question
    if index == len(quiz_data) - 1:
        next_button.config(text="Submit")
    else:
        next_button.config(text="Next Question")

def handle_next_click():
    """Handles the 'Next' or 'Submit' button click."""
    
    # Validate that an option was selected
    if selected_option.get() == -1:
        messagebox.showerror("Error", "Please select an answer.")
        return
        
    # Store the user's answer
    user_answers.append(selected_option.get())
    
    # Check if quiz is over
    if current_question_index < len(quiz_data) - 1:
        # Move to the next question
        show_question(current_question_index + 1)
    else:
        # Quiz is finished, show results
        show_results()

def show_results():
    """Calculates score and displays the results screen."""
    global score
    score = 0
    
    # Hide quiz frame, show results frame
    quiz_frame.pack_forget()
    results_frame.pack(fill="both", expand=True)
    
    # Enable writing to the Text widget
    results_text.config(state="normal")
    results_text.delete("1.0", tk.END)
    
    # Add a title to the results
    results_text.insert(tk.END, "--- Your Quiz Results ---\n\n", "Title")
    
    # Calculate score and build results string
    for i, question_data in enumerate(quiz_data):
        user_answer_index = user_answers[i]
        correct_answer_index = question_data["correct_index"]
        
        question_str = f"Q{i+1}: {question_data['question']}\n"
        your_answer_str = f"  Your Answer: {question_data['options'][user_answer_index]}\n"
        
        if user_answer_index == correct_answer_index:
            score += 1
            results_text.insert(tk.END, question_str, "Question")
            results_text.insert(tk.END, your_answer_str, "Correct")
            results_text.insert(tk.END, "  Result: Correct!\n\n", "Correct")
        else:
            correct_answer_str = f"  Correct Answer: {question_data['options'][correct_answer_index]}\n"
            results_text.insert(tk.END, question_str, "Question")
            results_text.insert(tk.END, your_answer_str, "Incorrect")
            results_text.insert(tk.END, correct_answer_str, "Incorrect")
            results_text.insert(tk.END, "  Result: Incorrect\n\n", "Incorrect")

    # Disable writing to the Text widget
    results_text.config(state="disabled")
    
    # Update final score label
    score_label.config(text=f"Your Final Score: {score} / {len(quiz_data)}")

def restart_quiz():
    """Resets all variables and returns to the welcome screen."""
    global current_question_index, user_answers, score
    current_question_index = 0
    user_answers = []
    score = 0
    
    # Reset terms checkbox
    var_terms.set(0)
    
    # Hide results frame, show welcome frame
    results_frame.pack_forget()
    welcome_frame.pack(fill="both", expand=True)

# --- 4. Main Application Window Setup ---
root = tk.Tk()
root.title("Online Quiz Application")
root.geometry("550x500")

style = ttk.Style(root)
style.theme_use('clam')

# --- 5. Welcome Frame ---
welcome_frame = ttk.Frame(root, padding="20")
welcome_frame.pack(fill="both", expand=True)

welcome_label = ttk.Label(welcome_frame, text="Welcome to the Python Quiz!", font=("Helvetica", 18, "bold"))
welcome_label.pack(pady=20)

instructions_label = ttk.Label(
    welcome_frame, 
    text="You will be asked {len(quiz_data)} multiple-choice questions.\nSelect one answer for each question and click 'Next'.\n\nGood luck!", 
    font=("Helvetica", 11),
    justify="center"
)
instructions_label.pack(pady=20)

# Checkbutton requirement
var_terms = tk.IntVar()
terms_check = ttk.Checkbutton(
    welcome_frame, 
    text="I have read and agree to the terms and conditions.",
    variable=var_terms
)
terms_check.pack(pady=20)

start_button = ttk.Button(welcome_frame, text="Start Quiz", command=start_quiz)
start_button.pack(pady=10, ipady=5, ipadx=10)


# --- 6. Quiz Frame ---
quiz_frame = ttk.Frame(root, padding="20")
# (This frame is packed later by start_quiz)

question_number_label = ttk.Label(quiz_frame, text="Question X of Y", font=("Helvetica", 12, "italic"))
question_number_label.pack(pady=(0, 10))

question_label = ttk.Label(quiz_frame, text="This is the question text", font=("Helvetica", 14, "bold"), wraplength=500)
question_label.pack(pady=20)

# Frame to hold radio buttons
options_frame = ttk.Frame(quiz_frame)
options_frame.pack(pady=10)

selected_option = tk.IntVar(value=-1) # Use -1 to represent 'no selection'
option_radios = []

for i in range(4):
    radio = ttk.Radiobutton(options_frame, text=f"Option {i+1}", variable=selected_option, value=i)
    radio.pack(anchor="w", pady=5, padx=20)
    option_radios.append(radio)

next_button = ttk.Button(quiz_frame, text="Next Question", command=handle_next_click)
next_button.pack(pady=20, ipady=5, ipadx=10)

# --- 7. Results Frame ---
results_frame = ttk.Frame(root, padding="20")
# (This frame is packed later by show_results)

results_title_label = ttk.Label(results_frame, text="Quiz Completed!", font=("Helvetica", 18, "bold"))
results_title_label.pack(pady=20)

score_label = ttk.Label(results_frame, text="Your Final Score: X / Y", font=("Helvetica", 14))
score_label.pack(pady=10)

# Text widget requirement
results_text = ScrolledText(results_frame, wrap="word", width=60, height=15, font=("Helvetica", 10))
results_text.pack(pady=10, fill="both", expand=True)

# Configure tags for formatting in the Text widget
results_text.tag_configure("Title", font=("Helvetica", 14, "bold"), justify="center")
results_text.tag_configure("Question", font=("Helvetica", 10, "bold"))
results_text.tag_configure("Correct", foreground="green")
results_text.tag_configure("Incorrect", foreground="red")

results_text.config(state="disabled") # Make it read-only

restart_button = ttk.Button(results_frame, text="Restart Quiz", command=restart_quiz)
restart_button.pack(pady=20, ipady=5, ipadx=10)

# --- 8. Run the Application ---
root.mainloop()