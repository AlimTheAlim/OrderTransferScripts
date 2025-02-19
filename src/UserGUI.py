import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from WebIntefaceInteract import webInteractor

# Function to clear the contents of the temp directory
def clear_temp_directory():
    temp_dir = os.path.join(os.path.dirname(__file__), '..', 'temp')
    if os.path.exists(temp_dir):
        for filename in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Error while deleting file {file_path}: {e}")
    else:
        os.makedirs(temp_dir)  # Create the temp directory if it doesn't exist

# Function to open file dialog and get file path
def browse_file():
    file_path = filedialog.askopenfilename(title="Select a file")  # Open file dialog
    if file_path:
        file_path_label.config(text=file_path)  # Display file path on the label

# Function to move the selected file to ../temp and call webinteractor
def submit_file():
    file_path = file_path_label.cget("text")
    if file_path != "No file selected":
        # Clear the temp directory
        clear_temp_directory()

        # Move the file to ../temp directory
        temp_dir = os.path.join(os.path.dirname(__file__), '..', 'temp')
        try:
            # Move the file to ../temp
            shutil.copy(file_path, temp_dir)
            messagebox.showinfo("File Uploaded", f"File '{file_path}' uploaded successfully to '../temp'.")
        except Exception as e:
            messagebox.showerror("Error", f"Error while uploading file: {e}")
            return
        
        # Call the webinteractor() function
        webInteractor()
    else:
        messagebox.showwarning("No File", "Please select a file first.")

# Sample webinteractor function (replace with your own logic)
# Create main Tkinter window
root = tk.Tk()
root.title("File Upload Interface")

# Set window size
root.geometry("400x200")

# Label to show selected file path
file_path_label = tk.Label(root, text="No file selected", width=40, anchor="w")
file_path_label.pack(pady=10)

# Browse button to select file
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=5)

# Submit button to submit the file
submit_button = tk.Button(root, text="Submit", command=submit_file)
submit_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
