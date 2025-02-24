import tkinter as tk
from tkinter import messagebox
import pyodbc

# Database Connection
def connect_db():
    try:
        conn = pyodbc.connect(
            "DRIVER={SQL Server};"
            "SERVER=DESKTOP-05EUAEF\SQLEXPRESS;"  # Replace with your SQL Server name
            "DATABASE=cv_database;"
            "Trusted_Connection=yes;"
        )
        return conn
    except Exception as e:
        messagebox.showerror("Database Error", f"Failed to connect: {str(e)}")
        return None

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    education = education_entry.get()
    experience = experience_entry.get()
    skills = skills_entry.get()
    
    if not name or not email or not phone:
        messagebox.showwarning("Warning", "Please fill in all required fields!")
        return
    
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO cv (name, email, phone, education, experience, skills) VALUES (?, ?, ?, ?, ?, ?)",
                (name, email, phone, education, experience, skills)
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "CV saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Database Error: {str(e)}")

# Create main window
root = tk.Tk()
root.title("CV Form")
root.geometry("400x400")

# Labels and Entries
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Phone:").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Education:").pack()
education_entry = tk.Entry(root)
education_entry.pack()

tk.Label(root, text="Experience:").pack()
experience_entry = tk.Entry(root)
experience_entry.pack()

tk.Label(root, text="Skills:").pack()
skills_entry = tk.Entry(root)
skills_entry.pack()

# Submit Button
tk.Button(root, text="Submit", command=submit_form).pack()

# Run application
root.mainloop()
