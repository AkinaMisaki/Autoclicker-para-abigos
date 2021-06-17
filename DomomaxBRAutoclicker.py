# IMPORTS
import time  # Import delay stuff
from pynput.keyboard import Controller as KeyboardController  # Imports keyboard presses
from pynput.mouse import Button, Controller as MouseController  # Imports mouse presses

keyboard = KeyboardController()
mouse = MouseController()

# VARIABLES - Leave all those at the defined values
Version = 1.2
WillClick = 0
menu = -1
delay = 0
Clicked = 0
coutnumber = 0


# FUNCTIONS
def countdown():
    countnumber = 5
    while countnumber >= 1:
        print(countnumber)
        countnumber -= 1
        time.sleep(1)

#def cls():
#    print('\n' * 100)
#CLS used to clear the screen

# MENU
print('Selecione o tipo de autoclicker')
while True:
    menu = input('1 - Instaclicks; 2 - Clicks a cada x segundos; 0 - Sair; -1 - Informações sobre autoclicker ')
    try:
        menu = int(menu)
    except ValueError:
        print('Não é um número, por favor coloque um número válido.')
        continue
    if menu == 1:
        WillClick = input('Coloque um número de cliques que você quer: ')
        try:
            WillClick = int(WillClick)
        except ValueError:
            print('Não é um número, por favor coloque um número válido.')
        if type(WillClick) == int:
            countdown()
            mouse.click(Button.left, int(WillClick))
    elif menu == 2:
        delay = input('Delay entre cliques: ')
        try:
            delay = int(delay)
        except ValueError:
            print('Não é um número, por favor coloque um número válido.')
            continue
        if delay == int(delay):
            WillClick = input('Número de cliques: ')
            try:
                WillClick = int(WillClick)
            except ValueError:
                print('Não é um número, por favor coloque um número válido.')
                continue
            while WillClick >= Clicked:
                mouse.click(Button.left, 1)
                time.sleep(delay)
                Clicked += 1
    elif menu == 0:
        print("Obrigado por usar DomomaxBR's autoclicker. Fechando...")
        time.sleep(3)
        exit()
    elif menu == -1:
        print('Versão atual:', Version)
        print('''Feito por DomomaxBR
        
        Link do canal: https://www.youtube.com/channel/UCWlSYfK4mHtn4XyFdAiu_ng
        Link do github: https://github.com/DomomaxBR/Autoclicker-para-abigos
        ''')
        print('Isso é um projeto open-source, você pode modificar e ver o código,')
        print('porém não tem permissão pra postar o código como se fosse seu.')
