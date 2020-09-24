from os import system
from time import sleep
from rich.progress import track
system('title [Tools] - Dsa Terminal')
def do_step(set, time):
    sleep(time)
def auto_get_ProgressBar(time):
    for step in track(range(100)):
        do_step(step, time)
system('cls')
print('Bem-vindo as ferramentas de controle de Terminal')
print('1 - Limpar tela   2 - Nano   3 - GUI   4 - Sair')
while True:
    try:
        p = int(input('> '))
        if p == 1:
            system('cls')
            print('Bem-vindo as ferramentas de controle de Terminal')
            print('1 - Limpar tela   2 - Nano   3 - GUI   4 - Sair')
        elif p == 2:
            system(r'nano')
            continue
        elif p == 3:
            pass
        elif p == 4:
            break
    except:
        continue