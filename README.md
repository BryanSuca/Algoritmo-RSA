# Algoritmo-RSA

Algebra Abstracta
2022-1
Permanente 2a
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

