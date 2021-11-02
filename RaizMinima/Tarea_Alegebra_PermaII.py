from math import sqrt

def Primo( p):
	if (p <= 1):
		return False
	if (p <= 3):
		return True
	if (p % 2 == 0 or p % 3 == 0):
		return False
	i = 5
	while(i * i <= p):
		if (p % i == 0 or p % (i + 2) == 0) :
			return False
		i = i + 6
	return True

def Calcular( x, y, p):
	res = 1
	x = x % p
	while (y > 0):
		if (y & 1):
			res = (res * x) % p
		y = y >> 1
		x = (x * x) % p
	return res

def Numeros(s, p) :
	while (p % 2 == 0) :
		s.add(2)
		p = p // 2
	for i in range(3, int(sqrt(p)), 2):
		while (p % i == 0) :
			s.add(i)
			p = p // i
	if (p > 2) :
		s.add(p)

def RaizPrimitiva( p) :
	s = set()
	if (Primo(p) == False):
		return -1
	q = p - 1
	Numeros(s, q)
	for r in range(2, q + 1):
		flag = False
		for it in s:
			if (Calcular(r, q // it, p) == 1):
				flag = True
				break
		if (flag == False):
			return r
	return -1

p = int(input("El número a sacar su raíz primaria es: "))
print("La raíz primaria para", p, " es ", RaizPrimitiva(p))