import os
import shutil
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog, messagebox
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

# OrderExtractor function that reads the PDF in the temp folder


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
            
            # Verify the file in the temp directory
            temp_file_path = os.path.join(temp_dir, os.path.basename(file_path))
            print(f"File uploaded: {temp_file_path}")
            
            # Ensure the file exists in the temp folder
            if os.path.exists(temp_file_path):
                # Call webInteractor (assuming it's responsible for processing)
                print(f"File is ready for processing: {temp_file_path}")
                  # Pass the correct file path to webInteractor
                

            else:
                messagebox.showerror("Error", "File upload failed. Please try again.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error while uploading file: {e}")
            return
    else:
        messagebox.showwarning("No File", "Please select a file first.")
        
def enter_order():
    webInteractor()
    return

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

enter_order = tk.Button(root, text="Enter Order", command=enter_order)
enter_order.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
