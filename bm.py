from PySimpleGUI import PySimpleGUI as sg # gui
import rpc # rich presence
import time
from time import mktime
from abc import ABCMeta, abstractmethod
import os


sg.theme('BrownBlue')
layout = [
    [sg.Text('Key'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Button('Entrar')]
]


boostmc = sg.Window('Boost Mc 1.3.1', layout)

while True:
    eventos, key = boostmc.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if key['senha'] == 'bm_23i4': 

            boostmc.hide()

            client_id = '837342292573552680' # id do client

            rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) 
            
            start_time = mktime(time.localtime())
            while True:
                activity = {
                    "state": "menu", 
                        "timestamps": {
                            "start": start_time # tempo decorrido
                        },
                        "assets": {
                            "large_text": "B.M v1.1.3", 
                            "large_image": "boostmc" #,
#                           "small_text": "texto pequeno",
#                           "small_image": "imagem_pequena"
                        }
                    }
                rpc_obj.set_activity(activity)
                os.system("cls") # clear
                os.system("boostmc.exe") # iniciando o programa 