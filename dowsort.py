import os
import shutil
import tkinter as tk
from tkinter import scrolledtext

# Define path
download_folder = os.path.expanduser("~/Downloads")

# Define target folders
folders = {
    "Photos": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".heic"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Installers": [".dmg", ".pkg", ".exe", ".msi"],
    "Compressed Files": [".zip", ".rar", ".tar", ".gz", ".7z"]
}

# Function to ensure target folders exist
def create_folders():
    for folder in folders:
        path = os.path.join(download_folder, folder)
        if not os.path.exists(path):
            os.makedirs(path)

# Function to move files and update the display
def move_files(text_widget):
    files_moved = False
    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            for folder, extensions in folders.items():
                if file_ext in extensions:
                    target_folder = os.path.join(download_folder, folder)
                    shutil.move(file_path, target_folder)
                    text_widget.insert(tk.END, f"Moved {filename} to {folder}\n")
                    text_widget.see(tk.END)
                    text_widget.update()
                    files_moved = True

    if files_moved:
        text_widget.insert(tk.END, "\nFiles successfully sorted!\n")
    else:
        text_widget.insert(tk.END, "\nNo files to sort!\n")
    
    text_widget.see(tk.END)
    text_widget.update()

def show_message():
    root = tk.Tk()
    root.title("DowSort - File Organizer")

    # screen in center
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 600
    window_height = 500
    position_x = (screen_width // 2) - (window_width // 2)
    position_y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    root.configure(bg="black")

    # Bring window to the front
    root.lift()
    root.attributes('-topmost', True)
    root.after(1000, lambda: root.attributes('-topmost', False))

    text_widget = scrolledtext.ScrolledText(root, width=70, height=25, font=("Arial", 12), bg="black", fg="green")
    text_widget.pack(pady=10)

    # Run the function to move files and update the display
    move_files(text_widget)

    # Add a close button to exit the application
    close_button = tk.Button(root, text="Close", command=root.quit, bg="black", fg="green", font=("Arial", 12))
    close_button.pack(pady=10)

    # Start the Tkinter main loop
    root.mainloop()

# Create folders (only if they don't already exist)
create_folders()

# success message
show_message()