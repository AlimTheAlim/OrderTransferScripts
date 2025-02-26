from cx_Freeze import setup, Executable

# Build options
build_options = {
    "packages": ["os", "sys", "PyPDF2", "selenium","re","shutil","tkinter"],  # Add any packages you need
    "excludes": [],
    "include_files": [],  # Add any files you want to include
}

# Executable configuration
executables = [
    Executable("main.py", base=None)
]

# Setup cx_Freeze with configuration
setup(
    name="Order Auto Processor",
    version="1.0",
    description="Process Flores And Foley Orders into OIS",
    options={"build_exe": build_options},
    executables=executables
)
