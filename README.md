# Conversor de Punto Flotante a Decimal
Se define un nuevo formato de punto flotante de 10 bits con 1 bit de signo, 5 bits de exponente, usando un código exceso-15 (es decir, al exponente le restamos 15) y 4 bits de fracción.  a. Convierta el siguiente número binario en representación de punto flotante de 10 bits al equivalente en decimal. Indique cuáles son los bits de signo, exponente y fracción; deje evidencia del procedimiento utilizado para el resultado obtenido. 
 
* 1100101110 

* Signo: 1   
* Exponente: 10010 = 18
* Fracción: 1110 = 1 + 1/2 + 1/4 + 1/16 = 1.875   
* N = (-1)1 * 2(18 - 15) * 1.875 = 15

### Prerequisitos

Para ejecutar el programa es necesario contar con:

* Python 3.7.0
* [numexpr](https://pypi.org/project/numexpr/)


## Autores
* **Pablo Sao** - [psao](https://github.com/psao)
