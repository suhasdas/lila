import tkinter as tk
from tkinter import ttk
from random import choice
from PIL import Image, ImageTk
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

def update_details(event):
    selected_piece = piece_var.get()
    description = piece_descriptions.get(selected_piece, "Select a chess piece to see its description.")
    description_label.config(text=description)
    
    piece_abbreviations = {
        'Pawn': 'P', 'Knight': 'N', 'Bishop': 'B',
        'Rook': 'R', 'Queen': 'Q', 'King': 'K'
    }
    
    color_initial = choice(['w', 'b'])
    piece_abbr = piece_abbreviations.get(selected_piece, '')
    
    image_path = os.path.join(script_dir 'images', 'california', f"{color_initial}{piece_abbr}.png")
    
    try:
        photo = ImageTk.PhotoImage(Image.open(image_path))
        piece_image_label.config(image=photo)
        piece_image_label.image = photo
    except Exception as e:
        print(f"Failed to load image: {e}")
        description_label.config(text="Failed to load image.")

root = tk.Tk()
root.title("Chess Piece Bios")

piece_descriptions = {
    "Pawn": "Pawns move forward one square, but capture diagonally. On its first move, it can advance two squares. When a pawn moves two squares and is now next to an enemy pawn, the enemy pawn can capture the pawn as if the other pawn moved one square.",
    "Knight": "Knights move in an L-shape: two squares in one direction and then one square perpendicular.",
    "Bishop": "Bishops move diagonally on the board, for any number of squares.",
    "Rook": "Rooks move horizontally or vertically, for any number of squares.",
    "Queen": "The Queen can move any number of squares along a row, column, or diagonal.",
    "King": "The King moves one square in any direction."
}

piece_var = tk.StringVar()
piece_selector = ttk.Combobox(root, textvariable=piece_var, values=list(piece_descriptions.keys()))
piece_selector.bind("<<ComboboxSelected>>", update_details)
piece_selector.grid(column=0, row=0, padx=10, pady=10)

description_label = tk.Label(root, text="Select a chess piece to see its description.", wraplength=400)
description_label.grid(column=0, row=1, padx=10, pady=10)

piece_image_label = tk.Label(root)
piece_image_label.grid(column=0, row=2, padx=10, pady=10)

root.mainloop()
