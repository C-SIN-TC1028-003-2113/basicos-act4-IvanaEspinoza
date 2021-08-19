import math
def main():
    #escribe tu código abajo de esta línea

    num=float(input('Número: '))
    decimal=int(input('Decimales a mostrar: '))
    varphi=float((1.0 + math.sqrt(5))/2)
    resultado=varphi*num

    print('Razón áurea: '+str(round(resultado,decimal)))

if __name__ == '__main__':
    main()
