import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class VillenTimpurinkolmioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Villen Timpurinkolmio")
        self.root.configure(bg="#1E1E1E")

        self.label_a = tk.Label(root, text="Syötä ulottuvuus 'a':", fg="#FFFFFF", bg="#1E1E1E", font=("Arial", 14, "bold"))
        self.label_a.pack(pady=20)

        self.entry_a = tk.Entry(root, font=("Arial", 12))
        self.entry_a.pack(pady=5)

        self.calculate_button = ttk.Button(root, text="Laske", command=self.calculate, style="Calc.TButton")
        self.calculate_button.pack(pady=20)

        self.result_label = tk.Label(root, text="", fg="#FFFFFF", bg="#1E1E1E", font=("Arial", 12))
        self.result_label.pack(pady=20)

        self.style = ttk.Style()
        self.style.configure("Calc.TButton", foreground="#FFFFFF", background="#FF4081", font=("Arial", 12, "bold"))

        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.plot_3d = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()

    def calculate(self):
        try:
            dimension_a = float(self.entry_a.get())
            dimension_b = (4 / 3) * dimension_a
            dimension_c = (5 / 3) * dimension_a

            result_text = f"Ulottuvuus 'b': {dimension_b:.2f}\nUlottuvuus 'c': {dimension_c:.2f}"
            self.result_label.config(text=result_text)

            self.plot_3d.clear()
            self.plot_3d.plot([0, dimension_b], [0, dimension_b], [0, dimension_c], marker='o')
            self.plot_3d.set_xlabel('X')
            self.plot_3d.set_ylabel('Y')
            self.plot_3d.set_zlabel('Z')
            self.canvas.draw()

        except ValueError:
            self.result_label.config(text="Virheellinen syöte. Ole hyvä ja anna kelvollinen numero.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VillenTimpurinkolmioApp(root)
    root.mainloop()