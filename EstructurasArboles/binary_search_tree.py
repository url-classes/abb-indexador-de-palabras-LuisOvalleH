import tkinter as tk
from tkinter import filedialog, Canvas
import os
import shutil
from EstructurasArboles.node import Node
import re
from typing import Optional, TypeVar, Generic

T = TypeVar("T")

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    # FUNCION  PARA CALCULAR LA ALTURA DEL ARBOl
    def altura(self,subtree: Node[T]):

        if subtree is None:
            return 0

        return 1 + max(self.altura(subtree.left), self.altura(subtree.right))

    def insert(self, root, data):
        if root is None:
            return Node(data)  # Crea un nodo si el dato no existe en el árbol
        else:
            if data < root.data:
                root.left = self.insert(root.left, data)
            elif data > root.data:
                root.right = self.insert(root.right, data)
        return root  # Si la palabra ya existe, no hace nada y retorna el nodo sin cambios

    def draw_tree(self, root, canvas, x, y, step=0):
        step = 35 * self.altura(root)
        if root is not None:
            node_radius = 20 
            canvas.create_oval(x - node_radius, y - node_radius, x + node_radius, y + node_radius, fill="white")
            canvas.create_text(x, y, text=root.data, font=('Helvetica', '9')) 
            new_step = step + 40
            if root.left is not None:
                canvas.create_line(x - node_radius, y + node_radius, x - step, y + 100, arrow=tk.LAST)
                self.draw_tree(root.left, canvas, x - step, y + 100, step * 0.5)
            if root.right is not None:
                canvas.create_line(x + node_radius, y + node_radius, x + step, y + 100, arrow=tk.LAST)
                self.draw_tree(root.right, canvas, x + step, y + 100, step * 0.5)


