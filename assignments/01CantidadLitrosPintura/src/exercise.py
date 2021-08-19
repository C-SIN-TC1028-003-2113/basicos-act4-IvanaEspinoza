def main():
    #escribe tu código abajo de esta línea
    area=float(input('Area a pintar en metros: '))
    rendim=float(input('Rendimiento (m2/l): '))
    comprar=round(area/rendim)

    print('Litros a comprar: '+str(comprar))

if __name__ == '__main__':
    main()
