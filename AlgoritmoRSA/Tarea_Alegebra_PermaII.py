def euclid(m, n): 
    if n == 0: 
        return m 
    else: 
        r = m % n 
        return euclid(n, r) 
def exteuclid(a, b):       
    r1 = a 
    r2 = b 
    s1 = int(1) 
    s2 = int(0) 
    t1 = int(0) 
    t2 = int(1) 
    while r2 > 0: 
        q = r1//r2 
        r = r1-q * r2 
        r1 = r2 
        r2 = r 
        s = s1-q * s2 
        s1 = s2 
        s2 = s 
        t = t1-q * t2 
        t1 = t2 
        t2 = t 
    if t1 < 0: 
        t1 = t1 % a 
    return (r1, t1) 
p = 3
q = 11
n = p * q 
Pn = (p-1)*(q-1) 
  
key = [] 
  
for i in range(2, Pn): 
    gcd = euclid(Pn, i) 
    if gcd == 1: 
        key.append(i)
        print(i)
e = int(21) 
r, d = exteuclid(Pn, e) 
if r == 1: 
    d = int(d) 
    print("key : ", d) 
else: 
    print("No existe el inverso multiplicativo para \ la clave de cifrado dada. Elija una clave de cifrado diferente ") 
M = 21
S = (M**d) % n 
M1 = (S**e) % n 
if M == M1: 
    print("El mensaje es el mismo que se pidio, acepta el usuario el mensaje.") 
else: 
    print("El mensaje no es el mismo al que se pidio. ") 