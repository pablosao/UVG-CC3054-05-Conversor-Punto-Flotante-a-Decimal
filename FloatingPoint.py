'''
@Created: 17/02/2018
@author: Pablo Sao
@version: 1.0
@Descripcion: Convierte binarios de punto flotante a decimal
'''

from configparser import ConfigParser
import numexpr

def getSection(file_name='conf.ini', section=''):
    """
    Read configuration file and return a dictionary of the data
    :param filename: path and name of the ini file
    :param section: section in the ini filw
    :return: a dictionary of database parameters
    """
    parser = ConfigParser()
    parser.read(file_name)

    data = {}

    # Comprobamos que exista la sección que deseamos
    if parser.has_section(section):

        # Obtenemos los items que existen dentro de la seccion
        items = parser.items(section)

        for item in items:
            data[item[0]] = item[1]
    else:
        raise Exception('{0} no fue encontrado en el archivo {1}'.format(section, file_name))

    return data

def getFraction(data=""):
    """
    Sección de la fracción del punto flotante
    :param data valor binario de la fracción del punro flotante
    :return: value cálculo del valor decimal de la fracción
    """
    value = 1.00
    data = list(data)
    for cont in range(len(data)):
        if(int(data[cont]) == 1):

            value =  value + (1.0 / ( 2** (cont + 1)))

    return value


def toDecimal(binary=""):
    """
        conversión del valor binario de punto flotante a su valor decimal
        :param binary valor binario a convertir a binario

        """
    decimal = 0
    try:

        parser = getSection(section='initial_conf')
        floating_size = int(parser.get("floating_size"))

        if len(binary) != floating_size:
            print("El valor binario: {0} tiene un tamaño de {1} bits. Los bits configurados son: {2} bits".format(binary,len(binary), floating_size))

        else:
            # tamaño del Exponente
            exp_size = int(parser.get("exp_size"))

            # Descomponiendo punto flotante
            signo = binary[0]
            exponente = binary[1:(exp_size + 1)]
            fraccion_binary = str(binary[(exp_size + 1): (floating_size + 1)])
            fraccion = getFraction(data=fraccion_binary)

            # obteniendo formula
            parser = getSection(section='floating_point')
            formula = str(parser.get("formula").format(str(signo),str(int(exponente,2)),str(fraccion)))

            """
            print("Signo: {0}\nExponente: {1}\nFracción Binaria: {2}\nFracción: {3}\nFormula: {4}".format(signo,
                                                                                                            exponente,
                                                                                                            fraccion_binary,
                                                                                                            fraccion,
                                                                                                            formula))
            """
            decimal = numexpr.evaluate(eval(formula))
            return decimal

    except :
        print(Exception)


binario =  "1100101110"
print("Binario: {0}\nDecimal: {1}".format(binario,toDecimal(binary=binario)))
