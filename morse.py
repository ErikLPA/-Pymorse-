import tkinter as tk
from tkinter import messagebox, scrolledtext
import keyboard
import time
import threading

morse_inverse = {
    '.-': 'A', '-...': 'B', '-.-.': 'C',
    '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I',
    '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U',
    '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8',
    '----.': '9'
}

morse_dict = {v: k for k, v in morse_inverse.items()}

class MorsePracticeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Practicador Morse con Teclas Personalizadas")
        self.geometry("600x500")
        self.resizable(False, False)

        self.punto_key = tk.StringVar(value="a")
        self.raya_key = tk.StringVar(value="s")

        self.codigo_actual = ""
        self.last_press = time.time()
        self.punto_presionado = False
        self.raya_presionado = False
        self.running = False
        self.thread = None

        self.create_widgets()

    def create_widgets(self):
        frame_teclas = tk.LabelFrame(self, text="Configura tus teclas")
        frame_teclas.pack(padx=10, pady=10, fill="x")

        tk.Label(frame_teclas, text="Tecla para PUNTO (.)").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tk.Entry(frame_teclas, textvariable=self.punto_key, width=10).grid(row=0, column=1, padx=5)

        tk.Label(frame_teclas, text="Tecla para RAYA (-)").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        tk.Entry(frame_teclas, textvariable=self.raya_key, width=10).grid(row=1, column=1, padx=5)

        btn_start = tk.Button(frame_teclas, text="Iniciar práctica", command=self.start_practice)
        btn_start.grid(row=2, column=0, columnspan=2, pady=10)

        frame_mostrar = tk.LabelFrame(self, text="Alfabeto Morse")
        frame_mostrar.pack(padx=10, pady=5, fill="both", expand=True)

        self.text_alfabeto = tk.scrolledtext.ScrolledText(frame_mostrar, height=10, state='disabled')
        self.text_alfabeto.pack(fill="both", expand=True, padx=5, pady=5)

        frame_practica = tk.LabelFrame(self, text="Práctica")
        frame_practica.pack(padx=10, pady=5, fill="x")

        # Aquí cambiamos a Label no editable, fondo blanco, con borde sunken
        self.label_codigo = tk.Label(frame_practica, text="Código actual: ", font=("Consolas", 14), bg="white", relief="sunken", anchor="w", width=30)
        self.label_codigo.pack(anchor="w", padx=5, pady=5)

        self.label_resultado = tk.Label(frame_practica, text="Letra detectada: ", font=("Consolas", 18, "bold"))
        self.label_resultado.pack(anchor="w", padx=5, pady=5)

        self.btn_stop = tk.Button(frame_practica, text="Detener práctica", state='disabled', command=self.stop_practice)
        self.btn_stop.pack(pady=10)

        self.mostrar_alfabeto()

    def mostrar_alfabeto(self):
        self.text_alfabeto.config(state='normal')
        self.text_alfabeto.delete(1.0, tk.END)
        self.text_alfabeto.insert(tk.END, "Letra : Código Morse\n")
        self.text_alfabeto.insert(tk.END, "-"*25 + "\n")
        for letra in sorted(morse_dict.keys()):
            self.text_alfabeto.insert(tk.END, f"{letra} : {morse_dict[letra]}\n")
        self.text_alfabeto.config(state='disabled')

    def start_practice(self):
        punto = self.punto_key.get().strip().lower()
        raya = self.raya_key.get().strip().lower()

        if not punto or not raya:
            messagebox.showerror("Error", "Debes ingresar ambas teclas para punto y raya")
            return

        if punto == raya:
            messagebox.showerror("Error", "Las teclas para punto y raya deben ser diferentes")
            return

        self.codigo_actual = ""
        self.label_codigo.config(text="Código actual: ")
        self.label_resultado.config(text="Letra detectada: ")
        self.btn_stop.config(state='normal')

        self.punto_key_val = punto
        self.raya_key_val = raya

        self.running = True
        self.thread = threading.Thread(target=self.loop_practice, daemon=True)
        self.thread.start()

    def stop_practice(self):
        self.running = False
        self.btn_stop.config(state='disabled')
        self.label_resultado.config(text="Práctica detenida.")
        self.label_codigo.config(text="Código actual: ")

    def loop_practice(self):
        self.punto_presionado = False
        self.raya_presionado = False
        self.last_press = time.time()

        while self.running:
            ahora = time.time()

            if keyboard.is_pressed(self.punto_key_val):
                if not self.punto_presionado:
                    self.codigo_actual += '.'
                    self.last_press = ahora
                    self.update_codigo()
                    self.punto_presionado = True
            else:
                self.punto_presionado = False

            if keyboard.is_pressed(self.raya_key_val):
                if not self.raya_presionado:
                    self.codigo_actual += '-'
                    self.last_press = ahora
                    self.update_codigo()
                    self.raya_presionado = True
            else:
                self.raya_presionado = False

            if self.codigo_actual and (ahora - self.last_press > 0.8):
                letra = morse_inverse.get(self.codigo_actual, '¿?')
                self.update_resultado(letra)
                self.codigo_actual = ""
                self.update_codigo()
                self.last_press = ahora

            time.sleep(0.01)

    def update_codigo(self):
        self.label_codigo.config(text=f"Código actual: {self.codigo_actual}")

    def update_resultado(self, letra):
        self.label_resultado.config(text=f"Letra detectada: {letra}")


if __name__ == "__main__":
    app = MorsePracticeApp()
    app.mainloop()
