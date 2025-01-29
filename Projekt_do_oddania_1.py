import numpy as np
import math
import matplotlib.pyplot as plt
"""
#zad 2
def Pomiary(lista_do_sredniej):
  suma = sum(lista_do_sredniej)
  srednia = suma / len(lista_do_sredniej)
  print(f"srednia: {srednia}")

  suma_do_wariancji = 0
  for i in lista_do_sredniej:
    j = (i - srednia)**2
    suma_do_wariancji += j

  wariancja = suma_do_wariancji/len(lista_do_sredniej)
  print(f"Wariancja: {wariancja}")

  odchylenie_standardowe = math.sqrt(wariancja)
  print(f"odchyleniestandardowe:  {odchylenie_standardowe}")

Pomiary([1,2,3])
"""
"""
#zad 3

def fx(x):
  f = math.sqrt((x**2)+1)-1
  return f
def gx(x):
  g = (x**2)/(math.sqrt((x**2)+1)+1)
  return g

def liczenie_wiarygodne():
  for i in range(10):
    x = 8**(-(i+1))
    print(f'{x:<35.15f} {fx(x):<35.15f} {gx(x):<35.15f}')

liczenie_wiarygodne()
"""
"""
#zad 4

def yx(x):
    y = x - np.sin(x)
    return y

xv= [1e-1, 1e-5, 1e-10, 1e-15, 1e-20]
results = [(x, yx(x)) for x in xv]

for x, y in results:
    print(f"x = {x:.1e}, y= {y:.16e}")
"""
"""
#zad 5

def jeden_do_sto():
    suma = 0
    for i in range(1, 101):
        x = 1/i
        suma += x
    print(f'suma 1 => 100 = {suma}')

def sto_do_jeden():
    suma = 0
    for i in range(101,0,-1):
        x = 1 / i
        suma += x
    print(f'suma 100 => 1 = {suma}')
jeden_do_sto()
sto_do_jeden()
"""
"""
#zad 6
def wykres():
    def fx(x):
        f = x + np.sin(x)
        return f

    x = np.linspace(-2*math.pi,2*math.pi,10000)
    plt.plot(x,fx(x))
    plt.title('Funkcja f(x) na przedziale [-2π,2π]')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend(['f(x)=x+sin(x)'])
    plt.show()

wykres()
"""
"""
#zad 7

def wykres():
    def fx(x):
        f = x + 6
        return f
    def gx(x):
        g = math.e ** (4 * x)
        return g

    x = np.linspace(-10,1,10000)
    plt.plot(x,fx(x))
    plt.plot(x,gx(x))
    plt.title('Funkcje f(x) i g(x) na przedziale [-10,1]')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend(['f(x)=x+6', 'g(x)=e**4x'])
    plt.show()

wykres()
"""
"""
#zad 8
def fx(x):
    y = x
    return y
def wykres():
    lista_wartosc = []
    for i in range(10):
        lista_wartosc.append(fx(i))
    print(lista_wartosc)
    x = lista_wartosc
    y = lista_wartosc

    plt.scatter(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis([0,10 , 0,10])
    plt.title('Wykres punktowy dla liczb naturalnych')
    plt.show()

wykres()
print("zobaczmy czy cos sie zmieni w branchach"
"""




