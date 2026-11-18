import tkinter as tk
from tkinter import messagebox

class TextFightApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TEXT_FIGHT")
        self.geometry("350x260")
        self.configure(bg="#1e1e2e")

        self.attributes("-fullscreen", True)

        menu_box = tk.Frame(
            self,
            bg="#2a2a3c",
            bd=2,
            relief="ridge",
            padx=20,
            pady=20
        )
        menu_box.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        title = tk.Label(
            menu_box,
            text="=== TEXT_FIGHT ===",
            font=("Consolas", 14, "bold"),
            fg="#f9e2af",
            bg="#2a2a3c"
        )
        title.pack(pady=(0, 15))

        tk.Button(
            menu_box,
            text="New Game",
            width=20,
            bg="#a6e3a1",
            fg="#11111b",
            font=("Consolas", 11, "bold"),
            command=self.new_game
        ).pack(pady=4)

        tk.Button(
            menu_box,
            text="Load Game",
            width=20,
            bg="#89b4fa",
            fg="#11111b",
            font=("Consolas", 11, "bold"),
            command=self.load_game
        ).pack(pady=4)

        tk.Button(
            menu_box,
            text="Exit",
            width=20,
            bg="#f38ba8",
            fg="#11111b",
            font=("Consolas", 11, "bold"),
            command=self.destroy
        ).pack(pady=4)

    def new_game(self):
        messagebox.showinfo("Text_Fight", "Starting Gew Game...")

    def load_game(self):
        messagebox.showwarning("Text_Fight", "No save file yet!")


if __name__ == "__main__":
    app = TextFightApp()
    app.mainloop()
