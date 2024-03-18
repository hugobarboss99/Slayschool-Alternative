# Slayschool-Alternative
This concept aims to create a code with the same functionalities as the website "slayschool," but with the added benefit of being completely free and open-source.

# Starting as a PDF to txt converter

This simple Python script allows users to convert PDF files into raw text files, which can be utilized as inputs for various open-source Intelligent Assistants (IAs) like ChatGPT, Gemini, Copilot, etc.

## Usage

1. Ensure you have Python installed on your system.
2. Clone or download this repository.
3. Run the script `pdf_to_txt_converter.py`.
4. Click on the "Open PDF" button to select the PDF file you want to convert.
5. Once selected, the script will extract the text from the PDF file and save it as a TXT file in the same directory.
6. The conversion result will be displayed on the interface.

## Dependencies

- PyPDF2: A Python library for reading and extracting text from PDF files.
- tkinter: Python's standard GUI (Graphical User Interface) toolkit.
- Pillow (PIL): Python Imaging Library to handle images.

## Installation

1. Install Python from [python.org](https://www.python.org/downloads/).
2. Install dependencies using pip:

   ```
   pip install PyPDF2 pillow
   ```
3. Clone or download this repository.

## Supported File Types

- Input: PDF files
- Output: TXT files

## Note

- Ensure that the PDF file you want to convert is in a readable format.
- The script may not work properly with scanned PDFs or PDFs with complex formatting.

## Author

Hugo Barbosa Santana Silva

# Future of the project
The slayschool website has a few core concepts; my main idea is to create a code that can run all the available options on the website. For instance, it should be able to extract a transcript from a YouTube video and generate flashcards, questions, and more. Similarly, it should allow users to choose options like generating flashcards or questions directly from a PDF file within the code GUI itself. However, there are challenges in achieving this, such as the lack of open-source APIs for current popular LLMs or APIs for extracting transcriptions from YouTube videos.
