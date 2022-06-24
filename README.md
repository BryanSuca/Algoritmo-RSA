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
1.	Generar dos primos p y q, tal que p 6= q. Cada uno de k/2 bits.

    Creamos las funciones en el ejercicio:
    
    ○ exponenciacionModular
   
    ○ MiillerRabin
    
    ○ calcularPrimo
    
    ○ randoms
    
    Estas funciones nos ayudara a tener 2 numeros primos de k bits y diferentes
    
2.	Calcular n = p × q
3.	Calcular φ(n)
4.	Generar aleatoriamente e ∈ [2,n − 1], tal que gcd(e,φ(n)) = 1
5.	Hallar d tal que ed ≡ 1 (mod φ(n))
6.	return {n,e,d}


El algoritmo funciona en python.

Esta tolamente comentando que especifica los pasos del algoritmo miller rabin dicho algoritmo al momento de ejecutar genera los primos de 3, 4 y 5 cifras. Para que funcione correctamente el programa se necesito de la exponencion modular (x*y) % z, seguido del algoritmo Miller Rabin.

Muestra de la ejecucion:

101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587 593 599 601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701 709 719 727 733 739 743 751 757 761 769 773 787 797 809 811 821 823 827 829 839 853 857 859 863 877 881 883 887 907 911 919 929 937 941 947 953 967 971 977 983 991 997 1009 1013 1019 1021 1031 1033 1039 1049 1051 1061 1063 1069 1087 1091 1093 1097 1103 

.
.
.

98779 98801 98807 98809 98837 98849 98867 98869 98873 98887 98893 98897 98899 98909 98911 98927 98929 98939 98947 98953 98963 98981 98993 98999 99013 99017 99023 99041 99053 99079 99083 99089 99103 99109 99119 99131 99133 99137 99139 99149 99173 99181 99191 99223 99233 99241 99251 99257 99259 99277 99289 99317 99347 99349 99367 99371 99377 99391 99397 99401 99409 99431 99439 99469 99487 99497 99523 99527 99529 99551 99559 99563 99571 99577 99581 99607 99611 99623 99643 99661 99667 99679 99689 99707 99709 99713 99719 99721 99733 99761 99767 99787 99793 99809 99817 99823 99829 99833 99839 99859 99871 99877 99881 99901 99907 99923 99929 99961 99971 99989 99991

○ EL VALOR UTILIZADO PARA "S" ES 10.
