import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerador de senha (Version 1.0)")
        self.resizable(False, False)

    def main_window(self):
        def gerador():
            try:
                output.delete(0, 'end')
            except:
                pass

            lista = [op1.get(), op2.get(), op3.get(), op4.get()]
            if list != [0, 0, 0, 0]:
                try:
                    qtd = opt_menu.get()
                    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    lower = "abcdefghijklmnopqrstuvwxyz"
                    number = "0123456789101112"
                    carac = "!@#$%&*+<>,.:;?"
                    total = ''      

                    if 1 in lista:
                        total += upper
                    if 2 in lista:
                        total += lower
                    if 3 in lista:
                        total += number
                    if 4 in lista:
                        total += carac

                    output.insert(0, "".join(random.sample(total, qtd)))

                except:
                    messagebox.showerror('Erro', 'Quantidade não selecionada.')
            else:
                messagebox.showerror('Erro', 'Não foi possível gerar a senha pois nenhuma opção foi marcada.')

        lb_frame_1 = ttk.LabelFrame(self, text="Opções de senhas")
        lb_frame_1.grid(row=0, column=0, sticky='W', padx=5, pady=5)

        op1 = tk.IntVar()
        op2 = tk.IntVar()
        op3 = tk.IntVar()
        op4 = tk.IntVar()
        opt_menu = tk.IntVar()

        tb_1 = ttk.Checkbutton(lb_frame_1, text='Letras maiúsculas', variable=op1, onvalue=1, offvalue=0)
        tb_1.grid(row=0, column=0, sticky='W')
        tb_2 = ttk.Checkbutton(lb_frame_1, text='Letras minúsculas', variable=op2, onvalue=2, offvalue=0)
        tb_2.grid(row=1, column=0, sticky='W')
        tb_3 = ttk.Checkbutton(lb_frame_1, text='Números', variable=op3, onvalue=3, offvalue=0)
        tb_3.grid(row=2, column=0, sticky='W')
        tb_4 = ttk.Checkbutton(lb_frame_1, text='Caracteres especiais', variable=op4, onvalue=4, offvalue=0)
        tb_4.grid(row=3, column=0, sticky='W')  
        
        options_list = [0, 4, 6, 8, 12]
        opt_menu.set("Selecione a quantidade de caracteres.")
        option_menu = ttk.OptionMenu(lb_frame_1, opt_menu, *options_list)
        option_menu.grid(row=4, column=0, padx=5, pady=5)

        lb_frame_2 = ttk.LabelFrame(self, text="Gerar senha")
        lb_frame_2.grid(row=0, column=1, sticky='W', padx=5, pady=5)

        lb = ttk.Label(lb_frame_2, text='Senha gerada: ')
        lb.grid(row=0, column=1, padx=5, pady=5)

        output = ttk.Entry(lb_frame_2, width=33)
        output.grid(row=0, column=2, padx=5, pady=5)

        bt = ttk.Button(lb_frame_2, text='Gerar', command=gerador)
        bt.grid(row=1, column=2, sticky='E', padx=5, pady=5)


if __name__ == "__main__":
    gerador_de_senha = App()
    gerador_de_senha.main_window()
    gerador_de_senha.mainloop()
