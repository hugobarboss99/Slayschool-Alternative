import PyPDF2
import tkinter as tk
from tkinter import filedialog
from PIL import Image 

def open_file():
    """Opens the file explorer and retrieves the selected PDF file path."""
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select PDF File",
        filetypes=(( "PDF files", "*.pdf" ), ("All files", "*.*"))
    )
    if filename:
        convert_pdf_to_txt(filename)

def convert_pdf_to_txt(filename):
    """Extracts text from the PDF and saves it to a TXT file with page numbers."""
    try:
        # Open the PDF file in read binary mode
        with open(filename, "rb") as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Create an empty string to store the text
            text = ""

            # Loop through each page in the PDF
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]  # Access page using pages attribute

                # Add page number header
                text += f"\npage {page_num + 1}:\n"  # Start page numbering from 1

                # Extract text from the current page and append to the string
                text += page.extract_text()

            # Create a new TXT file and write the extracted text
            with open(f"{filename[:-4]}.txt", "w", encoding="utf-8") as txt_file:
                txt_file.write(text)

            # Display success message
            label_result.config(text="Conversion successful!")
    except FileNotFoundError:
        # Handle file not found error
        label_result.config(text="Error: File not found!")
    except Exception as e:
        # Handle other potential errors
        label_result.config(text=f"Error: {e}")

# Create the main window
window = tk.Tk()
window.title("PDF to TXT Converter")

# Load the image file (please, place the image is in the same directory)
try:
    image = Image.open('converter.png')  # Open the image you want to use as the icon
    photo = tk.PhotoImage(file='converter.png')  # Specify the correct file name
    window.iconphoto(True, photo)  # Set for all future top-level windows
except FileNotFoundError:
    print("Error: Icon file not found. Using default icon.")

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Get window width and height (assuming you have a fixed size window)
window_width = 400
window_height = 300

# Calculate x and y coordinates to center the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the window geometry with calculated coordinates
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a button to open the file explorer
button_open = tk.Button(window, text="Open PDF", command=open_file)
button_open.pack(pady=10)

# Label to display conversion result
label_result = tk.Label(window, text="")
label_result.pack()

# Run the main event loop
window.mainloop()
