#!/usr/bin/env python3

import os


def clear():
    # controllo la famiglia del sistema operativo per utilizzare la syscall corretta
    if os.name == 'nt':
        #per windows
        _ = os.system('cls')
    else:
        #per i sistemi posix compliant
        _ = os.system('clear')


def main():
    while True:
        print('Scegli l\'operazione da effettuare:\n1.Somma\n2.Sottrazione\n3.Moltiplicazione\n4.Divisione\nq.Uscita')
        request = input('Scelta: ')
        if request in ('1', '2', '3', '4'):
            try:
                num1 = float(input('Inserisci il primo numero: '))
                num2 = float(input('Inserisci il secondo numero: '))
            except:
                clear()
                print('Input non valido, riprova...')
                continue
            if request == '1':
                print(num1, '+', num2, '=', num1 + num2)
            elif request == '2':
                print(num1, '-', num2, '=', num1 - num2)
            elif request == '3':
                print(num1, '*', num2, '=', num1 * num2)
            elif request == '4':
                try:
                    print(num1, '/', num2, '=', num1 / num2)
                except:
                    print('Divisione per zero, operazione non consentita')
        elif request == 'q':
            break
        else:
            print('Selezione non valida, riprova')
        input()
        clear()


# Execute
if __name__ == '__main__':
    main()
