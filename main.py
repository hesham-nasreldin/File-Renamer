import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os


def number_files_in_folder(folder_path, start_number=1):
    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", f"Folder not found at '{folder_path}'")
        return
    try:
        files = [
            f
            for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
        ]
        files.sort()
    except Exception as e:
        messagebox.showerror(
            "Error", f"An error occurred while reading the directory: {e}"
        )
        return

    messagebox.showinfo("Info", f"Found {len(files)} files to rename.")

    current_number = start_number
    renamed = []
    for old_filename in files:
        name, extension = os.path.splitext(old_filename)
        new_filename = f"{str(current_number).zfill(2)}{extension}"

        old_file_path = os.path.join(folder_path, old_filename)
        new_file_path = os.path.join(folder_path, new_filename)

        try:
            os.rename(old_file_path, new_file_path)
            renamed.append(f"Renamed: '{old_filename}' -> '{new_filename}'")
            current_number += 1
        except Exception as e:
            messagebox.showerror(
                "Error", f"Could not rename '{old_filename}'. Error: {e}"
            )

    if renamed:
        messagebox.showinfo("Success", "Renaming process complete!")
        # To show details, you can add a text box, but for now, just success


root = tk.Tk()
root.title("File Renamer")
root.geometry("400x300")

folder_path = tk.StringVar()
start_number = 1
confirm = tk.BooleanVar()

ttk.Label(root, text="Select Folder:").pack(pady=5)
entry = ttk.Entry(root, textvariable=folder_path, width=50)
entry.pack()


def browse():
    path = filedialog.askdirectory()
    if path:
        folder_path.set(path)


ttk.Button(root, text="Browse", command=browse).pack(pady=5)

check = ttk.Checkbutton(root, text="Is it okay to rename the files?", variable=confirm)
check.pack(pady=10)


def rename():
    if not confirm.get():
        messagebox.showerror(
            "Error", "Please confirm that it's okay to rename the files."
        )
        return
    path = folder_path.get()
    if not path:
        messagebox.showerror("Error", "Please select a folder.")
        return
    number_files_in_folder(path, start_number)


ttk.Button(root, text="Rename Files", command=rename).pack(pady=10)

root.mainloop()
