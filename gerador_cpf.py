import requests
from tkinter import *

def gerar_cpf():
    from random import randint
    numero = str(randint(100000000, 999999999))

    novo_cpf = numero                   # 9 números aleatórios
    reverso = 10                        # Contador reverso
    total = 0                           # O total das multiplicações

    # Loop do CPF
    for index in range(19):
        if index > 8:                   # Primeiro índice vai de 0 a 9,
            index -= 9                  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1                    # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                   # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0                   # Zera o total
            novo_cpf += str(d)          # Concatena o digito gerado no novo cpf
    texto = f'''
        CPF Gerado: {novo_cpf}'''

    texto_cotacoes['text'] = texto  # editando o parâmetro text dentro do texto_cotacoes

      
janela = Tk()
janela.title('Gerador de CPF')
janela.geometry('400x400')

texto_orientacao = Label(janela, text='Clique no botão para gerar cpf')
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text='Gerar CPF', command=gerar_cpf)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)


janela.mainloop()

