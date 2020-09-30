import sys
sys.path.append("..")

import tkinter.filedialog
import tkinter as tk
from Logic import process as p

def main():
  ##Canvas
  root = tk.Tk()
  root.title("Traductor de Ensamblador a Binario")
  root.geometry("1280x720")

  ##Code Frame
  frameCode = tk.Frame(root)
  frameCode.pack()

  ##Assembly Input
  codeLabel = tk.Label(frameCode, text="Código Ensamblador")
  codeLabel.grid(row=0, column=0)

  codeInput = tk.Text(frameCode, width = 60, height = 30)
  codeInput.grid(row=1, column=0)

  ##Binary Output
  codeLabel1 = tk.Label(frameCode, text="Código Binario")
  codeLabel1.grid(row=0, column=1)

  codeOutput = tk.Text(frameCode, width = 60, height = 30)
  codeOutput.grid(row=1, column=1)

  ##Buttons
  frameButtons = tk.Frame(root)
  frameButtons.pack()

  def loadASMCode():
    root.fileName = tk.filedialog.askopenfilename(filetypes=(("Assembly Code", ".ASM"), ("All files", "*.*")))
    fileText = open(root.fileName).read()
    codeInput.insert(1.0, fileText)

  def translateInput():
    codeOutput.delete(1.0, tk.END)
    #codeOutput.insert(tk.INSERT, codeInput.get(1.0, tk.END))
    ##Once we get the assembly code we proceed to translate it

    instructions = codeInput.get(1.0, tk.END)

    outputProcess = p.process(instructions)

    codeOutput.insert(tk.INSERT, outputProcess)

    ##Logical Part
  
  def clearInput():
    codeInput.delete(1.0, tk.END)
    codeOutput.delete(1.0, tk.END)

  clearButton = tk.Button(frameButtons, text="Limpiar código", command = clearInput, bd = 5)
  clearButton.grid(row = 0, column = 0, pady = 5, padx=5)

  clearButton = tk.Button(frameButtons, text="Cargar archivo...", command = loadASMCode, bd = 5)
  clearButton.grid(row = 0, column = 1, pady = 5, padx=5)

  translateButton = tk.Button(frameButtons, text="Traducir", command = translateInput, bd = 5)
  translateButton.grid(row=0, column = 2, pady = 5, padx = 5)

  ##Canvas Call
  root.mainloop()