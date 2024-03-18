
mes =['Enero' , 'Febrero' , 'Marzo' , 'Abril' , 'Mayo' , 'Junio' , 'Julio' , 'Agosto' , 'Setiembre' , 'Octubre' , 'Noviembre' , 'Diciembre' ]

def run():
    presupuestos = []
    for i in mes:
        presupuesto = int(input(f'Cuál es el presupuesto para el mes de {i}: '))
        presupuestos.append(presupuesto)

    sumatoria = sum(presupuestos)


    print('El resultado es: ' + str(sumatoria/12))

if __name__ == '__main__':
   run()
