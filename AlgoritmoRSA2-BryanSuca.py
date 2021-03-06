
import random
 
# exponenciación modular.
# Devuelve (x^y) % p
def exponenciacionModular(x, y, p):
    r = 1;
    x = x % p;

    while (y > 0):
         
        
        if (y & 1):
            r = (r * x) % p;
        y = y>>1; 
        x = (x * x) % p;
     
    return r;
 
# MiillerRabin
def miillerRabin(d, n):
    #número aleatorio en [2..n-2], el caso cumple n>4
    a = 2 + random.randint(1, n - 4);
 
    #Calculando a^d % n
    x = exponenciacionModular(a, d, n);
 
    if (x == 1 or x == n - 1):
        return True;
 
    #Sigue elevando x al cuadrado mientras uno de los siguiente casos no cumpla
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
 
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;

    return False;

def calcularPrimo(n,k):
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;
 
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;
 
    # Repite k veces
    for i in range(k):
        if (miillerRabin(d, n) == False):
            return False;
 
    return True;

#Maximo comun divisor
def maximocd(a,b):
    r = b%a
    while r != 0:
        b=a
        a=r
        r= b%a
    return a

#Genera un número aleatorios n bits
def randoms(d):
    
    a = random.getrandbits(d)
    if a % 2 == 0:
        a -= 1
    return a

#Extendido de euclides
def encontrarD(e,φ):
	k=1
	m=(1+(k)*(φ))%(e)
	while m!=0:
		k=k+1
		m=(1+(k)*(φ))%(e)
	d=int((1+(k)*(φ))/(e))
	return d

if __name__ == '__main__':

# RSA KEY GENERATOR
    s = 4; # Número s de Miller-Rabin
    k = 24; # RSA KEY GENERATOR(k) 

# 1.- Primos aleatorios en bits
    cbits = int(k/2)
    bits = cbits
    p = randoms(bits)
    q = randoms(bits)

    while not calcularPrimo(p, s):
        p = randoms(bits)
    while not calcularPrimo(q, s):
        q = randoms(bits)  
    if p != q:
        print("Numero primo aleatorio p: " + str(p))
        print("Numero primo aleatorio q: " + str(q))

# 2.- Calcular n = p * q 
    
    n = p * q
    print("Calculando n: " + str(n))

# 3.- Calcular φ(n)
    φ = (p-1)*(q-1)
    print("Calculando φ(n): " + str(φ))

# 4.- Generar aleatoriamente e ∈ [2, n − 1], tal que gcd(e, φ(n)) = 1
    r = 2
    lista=[]
    while r < φ:
        m=maximocd(r,φ)
        if m == 1:
            lista.append(r)
            r = r + 1
        else:
            r = r + 1
    #print(lista) 
    e = random.choice(lista)
    print("Calculando e: " + str(e))

# 5.- Generar d
    d = encontrarD(e,φ)
    print("Calculando d: " + str(d))
    
# 6.- Llave publica y privada
    publica=[n,e]
    privada=[n,d]
    print("LLave publica " + str(publica) )
    print( "LLave privada " + str(privada))

# 7.- Cifrado y descifrado de mensajes
    print("------------------------------------------------------")
    print("Mensaje " + "|\t" + "Cifrar  "+ "|\t" + "Descifrar   ")
    for i in range (0,10):
        a = random.randrange(100000)
        cifrar = (a**e)%n
        descifrar = (cifrar**d)%n
        print( str(a) + "\t|\t" + str(cifrar) + "\t|\t" + str(descifrar) )
    print("------------------------------------------------------")

    