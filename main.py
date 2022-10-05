import requests
import json

import PySimpleGUI as sg

layout =[ [sg.Text('moeda'),sg.Input(key='moeda')],
[sg.Button("confirmar")],
[sg.Output(size=(30,30))]]


janela =sg.Window("dados").layout(layout)

while True:
  try:
    button, values = janela.Read()        
    moeda = values['moeda'].upper()

    cotacao=requests.get("https://economia.awesomeapi.com.br/json/last/"+moeda+"-BRL").json()                        

    print(cotacao[moeda+"BRL"]["high"])
  except:
    print("moeda não encontrada")

