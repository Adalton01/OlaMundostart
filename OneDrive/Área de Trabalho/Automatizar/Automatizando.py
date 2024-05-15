import pyautogui
from time import sleep  # pausa alguns segundos

pyautogui.click(969, 621, duration=0.5)
pyautogui.click(969, 543, duration=0.5)
pyautogui.write("Enzo")
pyautogui.click(951, 583, duration=0.5)
pyautogui.write("Enzo1587")
pyautogui.click(841, 625, duration=0.5)
pyautogui.click(969, 543, duration=0.5)
pyautogui.write("Enzo")
pyautogui.click(951, 583, duration=0.5)
pyautogui.write("Enzo1587")
pyautogui.click(829, 623, duration=0.5)

with open("produtos.txt", "r") as arquivo: #vai ler o arquivo por isso este "r" //vai da o nome de arquivo
    for linha in arquivo:
        produto = linha.split(",")[0]  # split representa dividir a cada linha encontrada
        quantidade = linha.split(",")[1]
        preço = linha.split(',')[2]

        # Preencher campos com dados do arquivo
        pyautogui.click(586, 513, duration=0.5)
        pyautogui.write(produto)
        pyautogui.click(577, 558, duration=0.5)
        pyautogui.write(quantidade)
        pyautogui.click(578, 598, duration=0.5)
        pyautogui.write(preço)
        pyautogui.click(413, 838, duration=0.5)
        sleep(0.1)# Pausa entre iterações
