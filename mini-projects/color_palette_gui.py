import tkinter as tk
import random
import pyperclip

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def generate_palette():
    for widget in palette_frame.winfo_children():
        widget.destroy()

    for _ in range(5):
        color = random_color()
        color_box = tk.Frame(palette_frame, bg=color, width=60, height=60)
        color_box.pack(side="left", padx=10, pady=10)

        hex_label = tk.Label(palette_frame, text=color, bg="white", fg="black", font=("Arial", 10, "bold"))
        hex_label.place(in_=color_box, relx=0.5, rely=1.1, anchor="center")

        def copy_hex(c=color):
            pyperclip.copy(c)
            status_label.config(text=f"Copied {c} to clipboard!")

        color_box.bind("<Button-1>", lambda event, c=color: copy_hex(c))

# GUI setup
root = tk.Tk()
root.title("🎨 Color Palette Generator")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Heading
title = tk.Label(root, text="🎨 Color Palette Generator", font=("Arial", 16, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Button
generate_btn = tk.Button(root, text="✨ Generate Palette", command=generate_palette, bg="#4CAF50", fg="white", font=("Arial", 12))
generate_btn.pack(pady=10)

# Palette Frame
palette_frame = tk.Frame(root, bg="#f0f0f0")
palette_frame.pack(pady=10)

# Status
status_label = tk.Label(root, text="", font=("Arial", 10), bg="#f0f0f0", fg="blue")
status_label.pack(pady=5)

# Start
generate_palette()
root.mainloop()
