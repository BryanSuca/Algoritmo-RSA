# Algoritmo-RSA

Algebra Abstracta
2022-1
Permanente 02b
Alumno: Bryan Edward Suca Jaramillo
____________________________________________________________________________________________

# Archivos creados en python:

Ejercicio1: AlgoritmoRSA1-BryanSuca.py

Ejercicio2: AlgoritmoRSA2-BryanSuca.py

_____________________________________________________________________________________________

# Ejercicio 1:

RSA KEY GENERATOR(k)

Encontraremos los pasos comentados al final del codigo despues de : if __name__ == '__main__':

1.	Generar dos primos p y q, tal que p 6= q. Cada uno de k/2 bits.

    Creamos las funciones en el ejercicio:
    
    ○ exponenciacionModular
   
    ○ MiillerRabin
    
    ○ calcularPrimo
    
    ○ randoms
    
    Estas funciones nos ayudara a tener 2 numeros primos de k bits y diferentes
    
2.	Calcular n = p × q

    Realizado en el paso 2 del codigo 
    
3.	Calcular φ(n) = φ = (p-1)*(q-1)

    Realizado en el paso 3 del codigo

4.	Generar aleatoriamente e ∈ [2,n − 1], tal que gcd(e,φ(n)) = 1

    Realizado en el paso 4 del codigo, en esta ocasion nos ayudamos de la funcion creada maximo comun divisor 
    
5.	Hallar d tal que ed ≡ 1 (mod φ(n))

    Creamos la funcion llamada def encontrarD, que nos permitira encontrar D, en la siguiente funcion se encontrar la forma de hallar d pasando e como divisor pero primero se encontrara una k que ayude a que sea diferente de 0 para d
    
6.	return {n,e,d}

    Realizado en el paso 6, encontramos el modulo n, la llave publica e y la llave privada d
    
 7. Cifrar usando P(m) = me mod n = c
  
    Realizado en el paso 7, Creamos las funciones para cifrar un mensaje, letra por letra que lo convierte a digitos
 
 8. Descifrar usando S(c) = cd mod n = m.
 
    Realizado en el paso 8, Creamos las funciones para descifrar digitos, y lo convierte a una palabra pero el codigo va descifrando letra por letra


Muestra de la ejecucion:

    Numero primo aleatorio p: 61
    Numero primo aleatorio q: 19
    Calculando n: 1159
    Calculando φ(n): 1080
    Calculando e: 1007
    Calculando d: 503
    LLave publica  1159,  1007
    LLave privada 1159, 503
    --------------------------------------------
    Colocar el mensaje en palabras
    Mensaje para cifrar : HOLA
    Mensaje Cifrado : 315 774 843 0  
    --------------------------------------------
    Colocar el mensaje cifrado(los numeros)
    Mensaje para descifrar : 315 774 843 0
    Mensaje Descifrado : HOLA 

# Ejercicio 2:

Crear un sistema RSA-64 (de k = 64 bits)

El programa funciona con 24 bits/2, tambien funciona para 32 bits pero el tiempo de ejecucion demora demasiado tiempo

El programa muestra e,d,n y genera 3 colummnas con 10 mensajes aleatorios

El programa funciona adecuadamente cifrando y descifrando


Muestra de la ejecucion:

    Numero primo aleatorio p: 2969
    Numero primo aleatorio q: 839
    Calculando n: 2490991
    Calculando φ(n): 2487184
    Calculando e: 936349
    Calculando d: 2119125
    LLave publica [2490991, 936349]
    LLave privada [2490991, 2119125]
    ------------------------------------------------------
    Mensaje |       Cifrar  |       Descifrar   
    28822   |       1140062 |       28822
    74601   |       2353311 |       74601
    35904   |       815932  |       35904
    72201   |       2376071 |       72201
    23795   |       16088   |       23795
    46773   |       1325458 |       46773
    73800   |       1112599 |       73800
    10098   |       805778  |       10098
    44428   |       1563072 |       44428
    70618   |       305169  |       70618
    ------------------------------------------------------
