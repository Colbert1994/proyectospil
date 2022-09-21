# Una compañera propuso que hagamos un programa que calcule el proximo service para un auto usando el kilometraje

# Funciones
def recibir_matricula():
    """Esta funcion recibe matriculas

    Returns:
        string: recibe el numero de patente ingresada por teclado
    """
    patente = input('Ingrese la patente del vehiculo: ')
    return patente

def pat_exist(matr):
    """Esta funcion es para saber si la patente ingresada existe en la base de datos

    Args:
        matr (int): patente
        flag (bool): bandera

    Returns:
        boolean: devuelve una bandera para saber si la matricula existe en la base de datos o no
    """
    flag = False
    mat_asoc = {
        'Patente_registrada': 'JKI203',
        'K.M': 1000,
        'Fecha de ultimo service': '10-08-2022',
        'Modelo': 'Peugot 206',
        'Año': 2010,
        'Marca de aceite y filtro utilizado': 'Marca Ejemplo'
    }
    if matr == mat_asoc['Patente_registrada']:
        flag = True
        print('Este es una patente asociada, pasamos a mostrar los detalles: ')
        print('-------------------------------------------------------------------------------------------------------------------------')
        print(mat_asoc)
        print('-----------------------------------------------------------------------------------------------------------------------------')
        prox = calc_prox_serv(mat_asoc['K.M'])
        print('El proximo service lo necesita a los: ', prox, 'km.')
    else:
        
        print('Cliente nuevo')
        print('-------------------------------------------------------------------------------------------------------------------------')
    return flag

def cliente_nuevo(x):
    """Funcion para ingreso de nuevo cliente

    Args:
        x (int): patente
        km(int): cantidad de kilometraje del vehiculo
        ultimo_service (str): la ultima fecha del service
        modelo (str): modelo del auto
        servicio (str): el servicio que se le realizo
        nuevo_auto (diccionario): contiene el auto agregado

    Returns:
        _type_: _description_
    """
    nuevo_auto = {}
    patente = x
    km = int(input('Ingrese el kilometraje del vehiculo: '))
    ultimo_service = input('Ingrese la ultima fecha de service en formato dd/mm/aa: ')
    modelo = input('Ingrese el modelo del auto y el año: ')
    servicio = input('Ingrese el servicio que se realizo: ')
    nuevo_auto = {
        'Patente:': patente,
        'Km: ': km,
        'Fecha de ultimo service: ':ultimo_service,
        'Modelo: ': modelo,
        'Marca de aceite y filtro utilzado: ': servicio
    }
    print('-----------------------------------------------------------------------------------------------------------------------------------')
    print('Guardando datos.......')
    print('Datos guardados con exito.')
    print(nuevo_auto)
    return nuevo_auto['Km: ']
def calc_prox_serv(x):
    """Funcion para calcular el proximo servicio a partir del kilometraje

    Args:
        x (int): recibe km

    Returns:
        int: el proximo servicio a partir del calculo que realizamos
    """
    nuevo_service = x + 15000
    print('El proximo servicio es a los : ',nuevo_service,'km.')
    return nuevo_service

# Ciclos y llamados de funciones.
opc = 0
while opc != 2:
    opc = int(input('Ingrese 1 para ingresar un vehiculo o 2 para terminar: '))
    if opc == 1:
        pat = recibir_matricula()
        z = pat_exist(pat)
        if z == False:
            q = cliente_nuevo(pat)
            p = calc_prox_serv(q)
    else:
        print('Gracias..')
        