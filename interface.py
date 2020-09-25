import tkinter as tk

def main():
  ##Lienzo
  root = tk.Tk()
  root.title("Traductor de Ensamblador a Binario")
  root.geometry("1280x720")

  ##Frame para el código
  frameCodigo = tk.Frame(root)
  frameCodigo.pack()

  ##Entrada Ensamblador
  codeLabel = tk.Label(frameCodigo, text="Código Ensamblador")
  codeLabel.grid(row=0, column=0)

  codeInput = tk.Text(frameCodigo, width = 60, height = 30)
  codeInput.grid(row=1, column=0)

  ##Salida Binario
  codeLabel1 = tk.Label(frameCodigo, text="Código Binario")
  codeLabel1.grid(row=0, column=1)

  codeOutput = tk.Text(frameCodigo, width = 60, height = 30)
  codeOutput.grid(row=1, column=1)

  ##Botones
  frameBotones = tk.Frame(root)
  frameBotones.pack()

  def translateInput():
    codeOutput.delete(1.0, tk.END)
    #codeOutput.insert(tk.INSERT, codeInput.get(1.0, tk.END))
    ##Una vez se obtiene el input lo que se procede es a traducir el código

    instructions = codeInput.get(1.0, tk.END)

    ##Logical Part
  
  def clearInput():
    codeInput.delete(1.0, tk.END)
    codeOutput.delete(1.0, tk.END)

  clearButton = tk.Button(frameBotones, text="Limpiar código", command = clearInput, bd = 5)
  clearButton.grid(row = 0, column = 0, pady = 5, padx=5)

  loadButton = tk.Button(frameBotones, text="Traducir", command = translateInput, bd = 5)
  loadButton.grid(row=0, column = 1, pady = 5, padx = 5)

  ##Llamado al lienzo
  root.mainloop()