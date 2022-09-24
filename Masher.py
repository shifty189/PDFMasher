from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename


def openFile():
    global PDF1, oneText, oneLabel
    PDF1 = askopenfilename()
    if PDF1[-4:] == ".pdf" or PDF1[-4:] == ".PDF":
        oneText.set(PDF1)
        oneLabel['bg'] = "Green"
    else:
        oneText.set('Only PDF files are supported')
        oneLabel['bg'] = "Red"


def openFile2():
    global PDF2, twoText, twoLabel
    PDF2 = askopenfilename()
    if PDF2[-4:] == ".pdf" or PDF2[-4:] == ".PDF":
        twoText.set(PDF2)
        twoLabel['bg'] = "Green"
    else:
        twoText.set('Only PDF files are supported')
        twoLabel['bg'] = "Red"


def PDFCheck():
    global oneText, twoText
    one = oneText.get()
    two = twoText.get()
    if one[-4:] == ".PDF":
        if two[-4:] == ".PDF":
            return True
        elif two[-4:] == ".pdf":
            return True
    elif one[-4:] == ".pdf":
        if two[-4:] == ".PDF":
            print("true " + two[-4:])
            return True
        elif two[-4:] == ".pdf":
            print("true " + two[-4:])
            return True
    return False


def mash():
    global mashText, mashLabel, oneText, twoText
    if PDFCheck():
        mashLabel['bg'] = "Green"
        types = [('PDF', "*.pdf")]
        filename = asksaveasfilename(filetypes=types, defaultextension=str(types))
        mashText.set(filename)
        merger = PdfMerger()
        try:
            merger.append(PDF1)
        except:
            mashLabel["bg"] = "Red"
            mashText.set("Something went wrong :(")
        try:
            merger.append(PDF2)
        except NotImplementedError:
            mashLabel["bg"] = "Red"
            mashText.set("You must slect 2 PDF files")
        try:
            merger.write(filename)
        except:
            mashLabel["bg"] = "Red"
            mashText.set("Something went wrong :(")
    else:
        mashLabel['bg'] = "Red"



PDF1 = ""
PDF2 = ""

root = tk.Tk()
root.title('PDF Masher!')
version = "1.0"
InfoFrame = tk.Frame(width=75, height=250)
InfoFrame.grid(row=0, columnspan=2)
explainLabel = tk.Label(InfoFrame, text=f"Load 2 PDF's using the buttons below, press the Mash! button in order"
                                        f"to combine 2 PDF files into one.")
explainLabel.grid(row=0, column=0)

oneFrame = tk.Frame()
oneFrame.grid(row=1, columnspan=2)
open_button1 = tk.Button(oneFrame, text=f'Open PDF', command=openFile)
open_button1.grid(row=0, column=0)
oneText = tk.StringVar(oneFrame, value="No PDF selected yet")
oneLabel = tk.Label(oneFrame, textvariable=oneText, background="White")
oneLabel.grid(row=0, column=1)

twoFrame = tk.Frame()
twoFrame.grid(row=2, columnspan=2)
open_button2 = tk.Button(twoFrame, text=f'Open second PDF', command=openFile2)
open_button2.grid(row=0, column=0)
twoText = tk.StringVar(twoFrame, value='No PDF selected yet')
twoLabel = tk.Label(twoFrame, textvariable=twoText, background="White")
twoLabel.grid(row=0, column=1)

mashFrame = tk.Frame()
mashFrame.grid(row=3, columnspan=2)
MashButton = tk.Button(mashFrame, text=f"Mash!", command=mash)
MashButton.grid(row=0, column=0)
mashText = tk.StringVar(mashFrame, value='No files Mashed yet')
mashLabel = tk.Label(mashFrame, textvariable=mashText, background="White")
mashLabel.grid(row=0, column=1)

root.mainloop()
