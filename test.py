import tkinter as tk
from tkinter import font
from tkinter import ttk

class FontTesterApp:
    def __init__(self, master):
        self.master = master
        master.title("Font Tester")

        self.font_families = list(font.families())
        self.font_families.sort()

        self.font_family_var = tk.StringVar(value=self.font_families[0])

        self.font_box = ttk.Combobox(master, textvariable=self.font_family_var, values=self.font_families, state="readonly")
        self.font_box.pack()

        self.sample_text = tk.Text(master, height=10, width=50)
        self.sample_text.pack()
        self.sample_text.insert(tk.END, "Sample text to test different fonts.")

        self.update_button = ttk.Button(master, text="Update Font", command=self.update_font)
        self.update_button.pack()

        # Initialize with the first font in the list
        self.update_font()

    def update_font(self):
        selected_font_family = self.font_family_var.get()
        self.sample_text.config(font=(selected_font_family, 12))

def main():
    root = tk.Tk()
    app = FontTesterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
