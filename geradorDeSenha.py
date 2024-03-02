import random
n=int(input("Quantos caracteres a senha deve ter? "))
alfa=["a", "b", "c", "d", "e" ,"f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
num=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
tudo=alfa+num
print("A senha deve conter: ")
print("1- Apenas letras")
print("2- Apenas números")
print("3- Letras e números")
r=int(input(""))
print("Senha:", end=" ")
s=[ ]
if r==1:
	for k in range(0,n):
		c=random.choice(alfa)
		s.append(c)
if r==2:
	for k in range(0,n):
		c=random.choice(num)
		s.append(c)
if r==3:
    if n>1:
        for k in range(2, n):
            c=random.choice(tudo)
            s.append(c)
        s.append(random.choice(num))
        s.append(random.choice(alfa))
        random.shuffle(s)
    if n==1:
        c = random.choice(tudo)
        s.append(c)
for z in range(0, len(s)):
	print(s[z], end="")