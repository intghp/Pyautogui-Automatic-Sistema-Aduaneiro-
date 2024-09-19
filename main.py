import pyautogui
from time import sleep


with open('arquivo.csv', 'r') as arquivo:
    for linha in arquivo:
        id = linha.split(',')[0]
        tipo = linha.split(',')[1]
        status = linha.split(',')[2]
        descricao = linha.split(',')[3]

        pyautogui.click(251,180, duration=1)
        pyautogui.write(id)

        pyautogui.click(271,220, duration=1)
        pyautogui.write(tipo)

        pyautogui.click(260,266, duration=1)
        pyautogui.write(status)

        pyautogui.click(262,310, duration=1)
        pyautogui.write(descricao)

        #Coordenada do Botão
        pyautogui.click(248,358, duration=1)
        sleep(1)


