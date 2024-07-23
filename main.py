#!/usr/bin/python3

import tkinter as tk
from ping_devices import sn_ping


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Opciones de escaneo")
        self.config(width=450, height=90)
        self.geometry("450x190")
        self.w_second = None
        self.create_main_view()

    def hidden(self):
        self.deiconify()
        if self.w_second:
            self.w_second.withdraw()

    def show_second_view(self, action):
        self.withdraw()  # Ocultar ventana principal
        if self.w_second is None:
            self.w_second = tk.Toplevel(self)
            self.w_second.title("Menu de usuario")
            self.w_second.geometry("600x200")

            label = tk.Label(self.w_second,
                             text="Ingrese direccion IP/Dominio")

            addr = tk.Entry(self.w_second, justify=tk.LEFT)

            btn_ok = tk.Button(self.w_second, text="Ok",
                               command=lambda: self.perfom_action(action,
                                                                  addr))

            btn_volver = tk.Button(self.w_second, text="Cancelar",
                                   command=lambda: self.hidden())

            label.grid(column=0, row=0)
            addr.grid(column=1, row=0, padx=4)
            btn_ok.grid(column=0, row=1, pady=12, padx=4, sticky=tk.W + tk.E)
            btn_volver.grid(column=1, row=1, pady=12, padx=4,
                            sticky=tk.W + tk.E)
        else:
            self.w_second.deiconify()

    def perfom_action(self, method, addr):
        ip_addr = addr.get()
        if method == "p":
            sn_ping(ip_addr)

    def create_main_view(self):
        self.grid()

        btn_ping = tk.Button(self, text="Ping", foreground="purple",
                             command=lambda: self.show_second_view("p"))

        btn_ping.grid(column=0, row=0, padx=10)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
