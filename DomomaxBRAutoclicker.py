#Autoclicker
#Script made by DomomaxBR
#Channel: https://www.youtube.com/channel/UCWlSYfK4mHtn4XyFdAiu_ng

#IMPORTS
import time  # Import delay stuff
from pynput.keyboard import Controller as KeyboardController  # Imports keyboard presses
from pynput.mouse import Button, Controller as MouseController  # Imports mouse presses

keyboard = KeyboardController()
mouse = MouseController()

#VARIABLES
clicks = 0  # Leave this at 0

#FUNCTIONS
def Countdown():
    print(5)
    time.sleep(1)
    print(4)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)

def Instaclick():
    while True:
        clicks = input('Coloque um número de cliques que você quer: ')
        try:
            clicks = int(clicks)
        except ValueError:
            print('Não é um número, por favor coloque um número válido.')
            continue
        if type(clicks) == int:
            Countdown()
            mouse.click(Button.left, int(clicks))

#MENU
menu = input('1-Instaclicks; 0-Sair')
if menu == 1:
    Instaclick()
elif menu == 0:
    print("Obrigado por usar DomomaxBR's autoclicker. Fechando...")
    time.sleep(5)
    exit()