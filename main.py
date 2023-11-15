#!/usr/bin/env python3
def main():
    print('Scegli l\'operazione da effettuare:\n1.Somma\n2.Sottrazione\n3.Moltiplicazione\n4.Divisione')
    while True:
        request=input('Scelta (per uscire scrivi q): ')
        if request in ('1','2','3','4'):
            try:
                num1 = float(input('Inserisci il primo numero: '))
                num2 = float(input('Inserisci il secondo numero: '))
            except:
                print('Input non valido, riprova')
                continue
            if request == '1':
                print(num1, '+', num2, '=', num1+num2)
            elif request == '2':
                print(num1, '-', num2, '=', num1-num2)
            elif request == '3':
                print(num1, '*', num2, '=', num1*num2)
            elif request == '4':
                print(num1, '/', num2, '=', num1/num2)
        elif request == 'q':
            break
        else:
            print('Selezione non valida, riprova')


# Execute
if __name__ == '__main__':
    main()