import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

# IPL data (can be replaced or loaded dynamically)
ipl_data = {
    "Mumbai Indians": 5,
    "Chennai Super Kings": 5,
    "Kolkata Knight Riders": 2,
    "Sunrisers Hyderabad": 1,
    "Rajasthan Royals": 1,
    "Deccan Chargers": 1,
    "Gujarat Titans": 1,
    "Lucknow Super Giants": 0,
    "Royal Challengers Bangalore": 0,
    "Delhi Capitals": 0,
    "Punjab Kings": 0
}

# Graph display function
def show_graph():
    teams = list(ipl_data.keys())
    wins = list(ipl_data.values())

    colors = ['#004ba0', '#f1c40f', '#6a1b9a', '#e67e22', '#3498db', '#1abc9c', '#e74c3c',
              '#34495e', '#8e44ad', '#2ecc71', '#d35400']

    plt.figure(figsize=(12, 6))
    plt.bar(teams, wins, color=colors[:len(teams)])
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Trophies Won")
    plt.title("IPL Titles Won by Teams")
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# ---------------- GUI ----------------
root = tk.Tk()
root.title("IPL Dashboard 2025")
root.geometry("600x400")
root.config(bg="#1f1f2e")

# Heading
title = tk.Label(root, text="IPL Dashboard 2025", font=("Helvetica", 22, "bold"), fg="#f5f5f5", bg="#1f1f2e")
title.pack(pady=30)

# Button
style = ttk.Style()
style.configure('TButton', font=('Arial', 14), padding=10)

show_button = ttk.Button(root, text="Show IPL Graph 📊", command=show_graph)
show_button.pack(pady=20)

# Footer
footer = tk.Label(root, text="Made with ❤ by Python", font=("Arial", 10), fg="lightgray", bg="#1f1f2e")
footer.pack(side="bottom", pady=10)

root.mainloop()