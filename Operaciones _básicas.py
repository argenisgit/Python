# Operaciones básicas:

123 + 222
# resultado = 345

 1.5 * 4
 #resultado = 6.0
 
 2 ** 100
 #resultado = 1267650600228229401496703205376
 
 len(893)
  #resultado = TypeError: object of type 'int' has no len()
 
len("893")
 #resultado = 3

 len([2, 3, 4, 5])
  #resultado =
 
 len(str(2 ** 1000000))
  #resultado = 4
 
 import math
  # importar libreria
  
 Math.pi
 # resultado = NameError: name 'Math' is not defined
 
 math.sqrt(85)
 # resultado = 9.219544457292887
 
 import random
 # importar libreria
 
 random.random()
 #resultado = 0.7272394715338446
 
 random.choice([1, 2, 3, 4])
 # resultado =3
 
 st = 'Spam'
 
 len(st)
 # resultado = 4

 st[0]
 # resultado = 'S'
 
 st[-1]
 #resultado = 'm'
 
 st[1:3]
 #resultado = 'pa'
 
 st[1:]
 #resultado = 'pam'
 
 st[:]
 #resultado = 'Spam'
 
 st + "Hola"
 #resultado = 'SpamHola'
 
 st * 5
 #resultado = 'SpamSpamSpamSpamSpam'
 
 
 st[0] = 'z'
 #resultado = TypeError: 'str' object does not support item assignment
 
 
# inmutabilidad los strings no cambian de valor como las # listas
 st = 'z' + st[1:]


print(st)
#resultado = zpam








#Transformar string a lista:

S = 'shrubbery'
#resultado = 


 L = list(S)
 #resultado = 

 L
 #resultado =m ['s', 'h', 'r', 'u', 'b', 'b', 'e', 'r', 'y']
 
L[1] = 'c'
#resultado = 

''.join(L)
#resultado = 'scrubbery'

 B = bytearray(b'spam')
 #resultado = 
 
 B.extend(b'eggs')
 #resultado = 
 
 B
 #resultado = bytearray(b'spameggs')
 
 B.decode()
 #resultado = 'spameggs'
 
 
 
 
 
 #Métodos especiales para strings:
 
 S = 'Spam'
 #resultado = 

 S.find('pa')
 #resultado = 1
 
 S
 #resultado = 'Spam'
 
 
 S.replace('pa', 'XYZ')
 #resultado = 'SXYZm'
 
 S
 #resultado = 'Spam'
 
 
 
 line = 'aaa,bbb,ccccc,dd'
 #resultado = 
 
 line.split(',')
 #resultado = ['aaa', 'bbb', 'ccccc', 'dd']
 
 S = 'spam'
 #resultado = 
 
 S.upper()
 #resltado = 'SPAM'
 
 S.isalpha() # Content tests: isalpha, isdigit, etc.
 
 line = 'aaa,bbb,ccccc,dd\n'
 #resultado = 
 
 line.rstrip()
 #resultado = 'aaa,bbb,ccccc,dd'
 
 
 line.rstrip().split(',')
 #resultado = ['aaa', 'bbb', 'ccccc', 'dd']
 
 
 
 
 
 
 #Plantillas para strings:
 
 '%s, eggs, and %s' % ('spam', 'SPAM!')
 #resultado = 'spam, eggs, and SPAM!'
 
 '{0}, eggs, and {1}'.format('spam', 'SPAM!')
 #resultado = 'spam, eggs, and SPAM!'
 
 '{}, eggs, and {}'.format('spam', 'SPAM!')
 #resultado = 'spam, eggs, and SPAM!'
 
 f'{S}, eggs, and {line}'
 #resultado =
 
 
 
 
 
 #Visualizar los métodos de un objecto:
 
 dir(S) # S es un string
 #resultado = NameError: name 'S' is not defined
 
 help(S.replace)
 #resultado = NameError: name 'S' is not defined
 
 S = 'A\nB\tC'
 #resultado = S = 'A\nB\tC'
 
 len(S)
 #resultado = 5
 
 ord('\n')
 #resultado = 10
 
 
 S = 'A\0B\0C'
 #reultado =
 
 len(S)
 #resultado = 5
 
 S
 #resultado = 'A\x00B\x00C'
 
 msg = """
aaaaaaaaaaaaa
Strings | 105bbb'''bbbbbbbbbb""bbbbbbb'bbbb
cccccccccccccc
"""
 
 msg
 #resultado = NameError: name 'msg' is not defined
 
 
 
 
 
 
 
 #Entradas de usuario:
 
 color = input("Introduce el color de tu camisa?: ")
 #resultado = Introduce el color de tu camisa?: 
 
 print(color)
 #resultado =
 
 n = int(input("Cuantas camisas tienes?: "))
 #resultado = Cuantas camisas tienes?: 
 
  print(n)
  #resultado = NameError: name 'n' is not defined
  
 price = float(input("Cuanto costo la mas bonita?: "))
 print(price)
 #resultado = IndentationError: unexpected indent
 
 