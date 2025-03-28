import tkinter as tk
from tkinter import font

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Python")
        self.root.geometry("300x450")
        self.root.resizable(False, False)
        
        # Variáveis
        self.expressao = ""
        self.entrada_texto = tk.StringVar()
        
        # Frame para a tela
        frame_tela = tk.Frame(root, height=100, bg="#f0f0f0")
        frame_tela.pack(expand=True, fill="both")
        
        # Configuração da fonte
        fonte = font.Font(size=24)
        
        # Tela da calculadora
        tela = tk.Entry(
            frame_tela, 
            textvariable=self.entrada_texto, 
            font=fonte, 
            bg="#f0f0f0", 
            fg="#000",
            bd=0,
            justify="right"
        )
        tela.pack(expand=True, fill="both", padx=10, pady=20)
        
        # Frame para os botões
        frame_botoes = tk.Frame(root)
        frame_botoes.pack(expand=True, fill="both")
        
        # Layout dos botões
        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        # Criação dos botões
        linha, coluna = 1, 0
        for botao in botoes:
            comando = lambda x=botao: self.clique_botao(x)
            if botao == '=':
                tk.Button(
                    frame_botoes,
                    text=botao,
                    bg="#4CAF50",
                    fg="white",
                    font=fonte,
                    bd=0,
                    command=comando
                ).grid(row=linha, column=coluna, sticky="nsew", padx=1, pady=1)
            elif botao == 'C':
                tk.Button(
                    frame_botoes,
                    text=botao,
                    bg="#f44336",
                    fg="white",
                    font=fonte,
                    bd=0,
                    command=comando
                ).grid(row=linha, column=coluna, sticky="nsew", padx=1, pady=1)
            else:
                tk.Button(
                    frame_botoes,
                    text=botao,
                    bg="#e0e0e0",
                    font=fonte,
                    bd=0,
                    command=comando
                ).grid(row=linha, column=coluna, sticky="nsew", padx=1, pady=1)
            
            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1
        
        # Configurar expansão das linhas e colunas
        for i in range(5):
            frame_botoes.grid_rowconfigure(i, weight=1)
            frame_botoes.grid_columnconfigure(i, weight=1)
    
    def clique_botao(self, valor):
        if valor == 'C':
            self.expressao = ""
            self.entrada_texto.set(self.expressao)
        elif valor == '=':
            try:
                resultado = str(eval(self.expressao))
                self.entrada_texto.set(resultado)
                self.expressao = resultado
            except:
                self.entrada_texto.set("Erro")
                self.expressao = ""
        else:
            self.expressao += str(valor)
            self.entrada_texto.set(self.expressao)

# Criar e executar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()