from tkinter import messagebox
from Model import Model
from View import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def show_error(self, message):
        self.view.show_error_message(message)

    def send_calculate(self, event=None):
        try:
            side_a = float(self.view.entry_a.get())
            height_h = float(self.view.entry_h.get())

            if side_a <= 0 and height_h <= 0:
                self.show_error("Küljepikkus ja kõrgus peavad olema positiivsed!")
                return
            elif height_h > side_a:
                self.show_error("Kõrgus ei saa küljepikkusest suurem olla!")
                return

            perimeter, area, diagonal = self.model.calculate_romb(side_a, height_h)
            self.view.display_results(side_a, height_h, perimeter, area, diagonal)

            self.view.entry_a.delete(0, 'end')
            self.view.entry_h.delete(0, 'end')

            self.view.entry_a.focus()

        except ValueError:
            self.show_error("Sisesta arvulised väärtused!")

    def run(self):
        self.view.mainloop()

    def on_close(self):
        if messagebox.askokcancel("Rakendusest väljumine", 'Soovid väljuda?'):
            self.view.destroy()
