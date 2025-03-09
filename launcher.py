import tkinter as tk
from tkinter import ttk  # Importă ttk pentru Progressbar
import subprocess
import time
from threading import Thread


def run_progress():
    # Ascunde butonul și afișează textul "Running..."
    run_button.place_forget()  # Ascunde butonul "Run"
    progress_label.place(x=150, y=100)  # Afișează textul "Running..."

    # Afișează progresul
    for i in range(1, 11):
        progress_var.set(i * 10)  # Setează progresul la fiecare 10%
        time.sleep(1)  # Așteaptă 1 secundă pentru fiecare pas

    # După ce progresul ajunge la 100%, rulează jocul
    subprocess.run(["py", "maingame.py"])


def on_run_click():
    # Pornește progresul în thread separat pentru a nu bloca UI-ul
    progress_thread = Thread(target=run_progress)
    progress_thread.start()


# Creează fereastra principală
root = tk.Tk()
root.title("Game Launcher")
root.geometry("400x200")

# Adaugă un buton 'Run'
run_button = tk.Button(root, text="Run", font=("Arial", 20), command=on_run_click)
run_button.pack(pady=20)

# Etichetă pentru progres
progress_label = tk.Label(root, text="Running...", font=("Arial", 16))
progress_label.place_forget()  # La început nu se afișează textul

# Bara de progres
progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, length=300, variable=progress_var, maximum=100)  # Folosește ttk.Progressbar
progress_bar.pack(pady=10)

root.mainloop()
