## En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

## En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.



import time
hora = time.strftime('%H')
minutos = time.strftime('%M')

def main():
    if int(hora) >= 19:
        print ("Es hora de irse a casa")
    else:
        print ("Quedan {} horas y {} minutos para irnos a casa".format(18- int(hora), 59-int(minutos)))


if __name__ == '__main__':
    main()
