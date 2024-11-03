import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12, include_uppercase=True, include_digits=True, include_special=True):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    digits = string.digits if include_digits else ""
    special = string.punctuation if include_special else ""
    
    all_characters = lowercase + uppercase + digits + special
    
    # Ensure at least one character from each selected type is included
    password = [
        random.choice(lowercase),
        random.choice(uppercase) if include_uppercase else '',
        random.choice(digits) if include_digits else '',
        random.choice(special) if include_special else ''
    ]
    
    # Fill the rest of the password
    password += random.choices(all_characters, k=length - len(password))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        include_uppercase = uppercase_var.get()
        include_digits = digits_var.get()
        include_special = special_var.get()
        
        if length < 1:
            messagebox.showerror("Invalid Input", "Password length should be at least 1.")
            return
        
        password = generate_password(length, include_uppercase, include_digits, include_special)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")

# Set up the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Title Label
title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Password Length
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.insert(0, "12")  # Default length
length_entry.pack()

# Checkbox Options
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.pack()

digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.pack()

special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_check.pack()

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Generated Password:", font=("Arial", 12))
result_label.pack(pady=10)

# Run the main loop
root.mainloop()
