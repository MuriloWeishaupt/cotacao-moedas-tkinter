import requests
import tkinter as tk
from tkinter import ttk

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

    texto = f'''
Dólar: R$ {float(cotacao_dolar):.2f}
Euro: € {float(cotacao_euro):.2f}
Bitcoin: ₿ {float(cotacao_btc):.2f}
'''
    texto_cotacoes["text"] = texto


janela = tk.Tk()
janela.title("💰 Cotação Atual das Moedas")
janela.geometry("350x250")
janela.configure(bg="#f2f2f2")


style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TLabel", font=("Segoe UI", 11), background="#f2f2f2")


texto_orientacao = ttk.Label(janela, text="Clique no botão para ver as cotações:")
texto_orientacao.pack(pady=(20, 10))


botao = ttk.Button(janela, text="🔍 Buscar cotações", command=pegar_cotacoes)
botao.pack(pady=10)


texto_cotacoes = ttk.Label(janela, text="", font=("Consolas", 12), justify="center")
texto_cotacoes.pack(pady=20)

janela.mainloop()
