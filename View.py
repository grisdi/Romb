from tkinter import Tk, Frame, font, Label, Entry, Button, Text, messagebox, END


class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.__width = 700
        self.__height = 500
        self.default_font = font.Font(family="Verdana", size=14)

        self.title('Rombi ümbermõõdu, pindala, pikema diagonaali arvutamine')
        self.center_window(self.__width, self.__height)

        self. top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        (self.entry_a, self.entry_h, self.btn_calculate, self.text_box) = self.create_frame_widgets()

        self.bind('<Return>', self.controller.send_calculate)
        self.bind('<Escape>', self.on_close)
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_top_frame(self):
        frame = Frame(self, bg='light blue', height=15)
        frame.pack(expand=True, fill='both')
        return frame

    def create_bottom_frame(self):
        frame = Frame(self, bg='light yellow')
        frame.pack(expand=True, fill='both')
        return frame

    def create_frame_widgets(self):
        lbl_a = Label(self.top_frame, text='Sisesta rombi küljepikkus:', font=self.default_font, bg='light blue')
        lbl_a.grid(row=0, column=0, padx=10, pady=5, sticky='ew')

        entry_a = Entry(self.top_frame, font=self.default_font)
        entry_a.grid(row=0, column=1, padx=10, pady=5)

        lbl_h = Label(self.top_frame, text='Sisesta rombi kõrgus:', font=self.default_font, bg='light blue')
        lbl_h.grid(row=1, column=0, padx=10, pady=5, sticky='ew')

        entry_h = Entry(self.top_frame, font=self.default_font)
        entry_h.grid(row=1, column=1, padx=10, pady=5)

        btn_calculate = Button(self.top_frame, text='Arvuta', font=self.default_font,
                               command=self.controller.send_calculate)
        btn_calculate.grid(row=0, column=2, rowspan=2, padx=10, pady=10)

        text_box = Text(self.bottom_frame, height=17, width=56, font=self.default_font)
        text_box.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

        return entry_a, entry_h, btn_calculate, text_box

    def display_results(self, side_a, height_h, perimeter, area, diagonal):
        results_text = f'Rombi laius: {side_a:.1f}\n'
        results_text += f'Rombi kõrgus: {height_h:.1f}\n'
        results_text += f'Ümbermõõt: {perimeter}\n'
        results_text += f'Pindala: {area}\n'
        results_text += f'Pikem diagonaal: {diagonal}\n'

        self.text_box.config(state='normal')  # Tekstikasti saab kirjutada
        self.text_box.delete('1.0', END)
        self.text_box.insert('insert', results_text + '\n')
        self.text_box.config(state='disabled')

    def on_close(self, event=None):
        # Kui akent üritatakse sulgeda
        if messagebox.askokcancel('Välju rakendusest', 'Kas soovid tõesti rakendusest väljuda?'):
            self.destroy()

    def show_error_message(self, message):
        messagebox.showerror('Viga', message)
