import tkinter as tk
from tkinter import filedialog, Canvas, Scrollbar, Frame
from EstructurasArboles.binary_search_tree import BinarySearchTree
import os
import shutil
import re

def cargar_archivo():
    # Directorio para guardar los archivos
    directorio = 'archivos'
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    # Abre un cuadro de diálogo para seleccionar un archivo .txt
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filepath:
        # Copia el archivo al directorio 'archivos'
        destino = os.path.join(directorio, os.path.basename(filepath))
        shutil.copy(filepath, destino)
        print(f"Archivo guardado en: {destino}")
    else:
        print("No se seleccionó ningún archivo")
        
def crear_arbol():
    directorio = 'archivos'
    bst = BinarySearchTree()
    palabra_dict = {}
    for filename in os.listdir(directorio):
        if filename.endswith('.txt'):
            with open(os.path.join(directorio, filename), 'r', encoding='utf-8') as file:
                texto = file.read()
                palabras = re.findall(r'\b\w+\b', texto)
                for palabra in palabras:
                    palabra = palabra.lower()
                    if palabra not in palabra_dict:
                        palabra_dict[palabra] = 1
                    else:
                        palabra_dict[palabra] += 1
                    if palabra_dict[palabra] == 1:  # Inserta solo si es la primera vez
                        bst.root = bst.insert(bst.root, palabra)
    conteo_palabras = ["Conteo de palabras:"]
    counter = 0
    for k, v in palabra_dict.items():
        conteo_palabras.append(f"{k}: {v}")
        counter += 1
        if counter % 10 == 0:
            conteo_palabras.append("\n")  # Inserta un salto de línea cada 10 palabras
    label_text.set(" ".join(conteo_palabras))  # Usa espacios para unir y mantener el formato en el label
    # Crear ventana para el canvas con barras de desplazamiento
    new_window = tk.Toplevel()
    new_window.title("Visualización del Árbol Binario")
    frame = Frame(new_window)
    frame.pack(fill=tk.BOTH, expand=True)
    canvas = Canvas(frame, bg='white', scrollregion=(0, 0, 5000, 3000))
    hbar = Scrollbar(frame, orient=tk.HORIZONTAL)
    hbar.pack(side=tk.BOTTOM, fill=tk.X)
    hbar.config(command=canvas.xview)
    vbar = Scrollbar(frame, orient=tk.VERTICAL)
    vbar.pack(side=tk.RIGHT, fill=tk.Y)
    vbar.config(command=canvas.yview)
    canvas.config(width=800, height=600, xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    bst.draw_tree(bst.root, canvas, 2500, 50, 200) 
    # Imprimir conteo de palabras
    print("Conteo de palabras:", palabra_dict)

    
# Crea la ventana principal
root = tk.Tk()
root.title("Cargador de Archivos TXT")

btn_cargar = tk.Button(root, text="Cargar archivo", command=cargar_archivo)
btn_cargar.pack(pady=20)
btn_arbol = tk.Button(root, text="Crear Arbol", command=crear_arbol)
btn_arbol.pack(pady=20)

label_text = tk.StringVar()
word_count_label = tk.Label(root, textvariable=label_text)
word_count_label.pack(pady=20)

root.geometry('600x400')
root.mainloop()

