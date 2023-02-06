# 104 Yash Chanchani Yash Chanchani. The code below uses the Tkinter library to display an app with an image and a PDF reader. Used tutorial by "python simplified" on youtube
# added element: you can now type into the textbox and it will save it to a pdf, basically the reverse. 

import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter import END
from tkinter.filedialog import askopenfile
# necessary saving pdf libraries
from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
root = tk.Tk()

# initializing canvas
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# logo
logo = Image.open('scene.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instructions = tk.Label(root, text="Select a PDF file on your computer to extract all its text", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)


# open file is from tutorial, for the browse button
def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        # text box
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")

# browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=0, row=2)

#text box for entering text to save to a pdf
text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
text_box.grid(column=1, row=3)


# added this whole function, takes in the textbox contect
def save_pdf():
    text_content = text_box.get("1.0", END)
    print(text_content)
    # setting pdf to standard size
    canvas = Canvas("output.pdf", pagesize=LETTER)

    # Set font to Times New Roman with 12-point size
    canvas.setFont("Times-Roman", 12)

    # putting the text on the proper area in the pdf
    canvas.drawString(1 * inch, 10 * inch, text_content)

    # Save the PDF file
    canvas.save()

    # showing user it is saved
    save_text.set("Saved!")


#save pdf button
save_text = tk.StringVar()
save_btn = tk.Button(root, textvariable=save_text, command=lambda:save_pdf(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
save_text.set("Save PDF")

save_btn.grid(column=2, row=2)

root.mainloop()