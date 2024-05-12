def calculadorPaneles():

    #Creación de variables con medidas solicitadas por input 
    a = int(input('Ingrese el Ancho de los PANELES SOLARES: '))
    b = int(input('Ingrese el Largo de los PANELES SOLARES: '))
    x = int(input('Ingrese el Ancho del TECHO: '))
    y = int(input('Ingrese el Largo del TECHO: ')) 

    # Se creó la variable de forma global dado que si no pasa por
    # la validación se mantiene el valor en 0
    
    totalPaneles = 0

    if(a>x or b>y):
        exit
    else:
        areaTecho = x*y
        areaPaneles = a*b
        totalPaneles = areaTecho/areaPaneles 

    print("El total de PANELES que caben en su TECHO son: ", int(totalPaneles))
    
calculadorPaneles()