#Warsztaty cz.1 - tak robimy komentarze

# Hello World
from operator import le


print('Hello World!')

# Zmienne

zmienna_typu_int = 1
zmienna_typu_string = "Filip"
zmienna_typu_float = 20.5
zmienna_typu_float_2 = 5e10
zmienna_typu_complex = 1j

print(zmienna_typu_int)
print(zmienna_typu_int + 1)
print(zmienna_typu_int, 2, zmienna_typu_int)

print(zmienna_typu_string)
print(zmienna_typu_string, 'test')
print(zmienna_typu_string, "test2")
print(zmienna_typu_string + ' ' + zmienna_typu_string + f' {zmienna_typu_string}')

print(zmienna_typu_float)
print(zmienna_typu_float_2)
print(zmienna_typu_complex)

zmienna3 = 1      
zmienna3 = "Filip"

print(zmienna3)

#string = str(zmienna_typu_int)
#int = int(zmienna_typu_int)  
#float = float(zmienna_typu_int)

#print(string) # komenda string + 1 spowodowałaby bład niezgodności typów
#print(int + 1)
#print(float)

filip, damian = "Filip", "Damian"

print(filip)
print(damian)

zmienna_typu_bool = True
print(zmienna_typu_bool)
print(2 > 1)

# listy w Python zachowują kolejność
zmienna_typu_lista_1 = ["Filip", "Damian", "Jan", "Jadwiga", "Zygmunt"] 
zmienna_typu_lista_2 = [1, 4, 100, 50] 
zmienna_typu_lista_3 = ["abc", 34, True, 40, "male"]

print(zmienna_typu_lista_1)
print(zmienna_typu_lista_2)
print(zmienna_typu_lista_3)

print(len(zmienna_typu_lista_1))
print(zmienna_typu_lista_1[0])
print(zmienna_typu_lista_1[-1])
print(zmienna_typu_lista_1[0:2]) # od strony lewej przedział domknięty, od prawej otwarty

print(zmienna_typu_lista_1[:2])
print(zmienna_typu_lista_1[2:])

zmienna_typu_lista_1[0] = "Nowe imię"
print(zmienna_typu_lista_1)

zmienna_typu_lista_1.append("Nowe imię 2")
print(zmienna_typu_lista_1)

zmienna_typu_lista_1.insert(1, "Helena")
print(zmienna_typu_lista_1)

zmienna_typu_lista_1.remove("Nowe imię 2")
print(zmienna_typu_lista_1)

del zmienna_typu_lista_1[0]
print(zmienna_typu_lista_1)

# Warunku if/else


if True:
  print("Weszliśmy do If-a")

if False:
  print("Weszliśmy do If-a")

a = 1
b = 2

if a < 2:
  print("Weszliśmy do If-a")

zmienna_typu_bool = True

if zmienna_typu_bool:
  print("Weszliśmy do If-a")
  if zmienna_typu_bool:
    print("Weszliśmy do If-a 2")


a = 1
b = 1
if b > a:
  print("b jest większe niz a")
elif a == b:
  print("a i b są równe")

a = 1
b = 1
if b > a:
  print("b jest większe niz a")
elif a == b:
  print("a i b są równe")
else:
  print("a jest większe niz b")


a = 2
b = 1
c = 3
if a > b and c > a:
  print("Oba warunki są prawdziwe")


# Zadania

# Dane do zadań

lista_imion = ["Filip", "Damian", "Jan", "Jadwiga", "Zygmunt"]
liczba_1 = 2
liczba_2 = 10

# 1. Wypisz drugie imię z listy 'lista_imion'
print('\n- - - - - Zadanie 1')
print(lista_imion[1])

# 2. Zmień imię Zygmunt na Ilona
print('\n- - - - - Zadanie 2')
lista_imion[-1] = 'Ilona'
print(lista_imion)

# 3. Dodaj nowe imię 'Pawel' do listy (na koniec listy)
print('\n- - - - - Zadanie 3')
lista_imion.append('Pawel')
print(lista_imion)

# 4. Dodaj nowe imię do list 'Agata' jako drugie
print('\n- - - - - Zadanie 4')
lista_imion.insert(1,'Agata')
print(lista_imion)

# 5. Usuń z listy imię Jadwiga
print('\n- - - - - Zadanie 5')
lista_imion.remove('Jadwiga')
print(lista_imion)

# 6. Wypisz ilość imion w liście (uzywając do tego odpowiedniej metody)
print('\n- - - - - Zadanie 6')
print('Ilosc imion w tablicy: ',len(lista_imion))

# 7. Pomnóz dwie zmienne: liczba_1 oraz liczba_2 i wypisz
print('\n- - - - - Zadanie 7')
print('Liczba_1: ',liczba_1)
print('Liczba_2: ',liczba_2)
print('Iloczyn: ',liczba_1*liczba_2)

# 8. Sprawdź uzywając warunków if/else która zmienna: liczba_1 oraz liczba_2 jest większa i wypisz odpowiedni tekst na ekranie
print('\n- - - - - Zadanie 8')
if liczba_1 > liczba_2:
  print('Liczba_1 jest wieksza od liczba_2')
else:
  print('Liczba_2 jest wieksza od liczba_1')

# 9. Sprawdź czy na liście imion znajduje się imię 'Jan' i wypisz odpowiedni komunikat
print('\n- - - - - Zadanie 9')
if lista_imion[0] == 'Jan':
  print("Jan na 1. pozycji listy")
elif lista_imion[1] == 'Jan':
  print("Jan na 2. pozycji listy")
elif lista_imion[2] == 'Jan':
  print("Jan na 3. pozycji listy")
elif lista_imion[3] == 'Jan':
  print("Jan na 4. pozycji listy")
elif lista_imion[4] == 'Jan':
  print("Jan na 5. pozycji listy")
elif lista_imion[5] == 'Jan':
  print("Jan na 6. pozycji listy")

#Drugie rozwiązanie tego samego zadania. Chyba bardziej eleganckie.

ilosc_osob = len(lista_imion)
print(ilosc_osob)
i = 0
while i<= ilosc_osob-1:
  print('licznik pętli: ',i)
  if lista_imion[i] == 'Jan':
    print('Jan znaleziony na ',i+1,' miejscu')
  i=i+1

# 10. Sprawdź czy na liście imion znajduje się imię 'Jan', jezeli tak to sprawdź czy liczba_2 jest większa od liczba_1, jezeli tak to wypisz na ekran drugie i trzecie imię z listy imion
print('\n- - - - - Zadanie 10')
ilosc_osob = len(lista_imion)
i = 0
while i<= ilosc_osob-1:
  if lista_imion[i] == 'Jan':
    print('Jan znaleziony na ',i+1,' miejscu')
    if liczba_2 > liczba_1:
      print('Drugie imię z listy: ',lista_imion[1])
      print('Trzecie imię z listy: ',lista_imion[2])
  i=i+1

# 11. Zmień typ liczba_1 na string a następnie wypisz na ekran
print('\n- - - - - Zadanie 11')
liczba_1_str = str(liczba_1)
print(liczba_1_str)

# 12. Zmień typ liczba_2 na float i dodaj do niej liczbę 24.5 i wypisz na ekran
print('\n- - - - - Zadanie 12')
#liczba_2_float = float(liczba_2) <- w tej linijce cały czas wyskakiwał błąd ['float' object is not callable]
print(liczba_2+24.5)


# 13. Wypisz tekst na ekran: 'Wartość liczby_2 to: [tutaj ma się pojawić wartość ze zmiennej]'
print('\n- - - - - Zadanie 13')
print('Wartość liczby_2 to: ',liczba_2)

# 14. Sprawdź czy liczba_2 jest większa od liczba_1 LUB lista imion zawiera imię 'Zygmunt' i wypisz na ekranie odpowiedni komunikat.
print('\n- - - - - Zadanie 14')
lista_imion.append('Zygmunt')
ilosc_osob = len(lista_imion)
print(ilosc_osob,'',lista_imion)

if lista_imion.index('Zygmunt')>0:
  print("Jest Zygmunt")

if liczba_2 > liczba_1:
  print('Liczba_2 jest większa od liczba_1')

# 15. * Stwórz nową listę która zawiera 5 elementów losowo wybranych cyfr a następnie dodaj wszystkie elementy do siebie i wypisz na ekranie 
# (tak aby mozna było dynamicznie rozszerzeć wielkość tablicy i zeby suma się liczyła za kazdym razem poprawnie)
print('\n- - - - - Zadanie 15')
import random
ilosc_liczb = 0
lista_losowa = []
suma = 0
ilosc_liczb = int(input("Podaj ilość liczb do losowania "))
i = 0
while i < ilosc_liczb:
  los = random.randint(0,10)
  lista_losowa.append(los)
  suma = suma + los
  i = i+1
print(lista_losowa)
print(suma)



# 16. * Przeiteruj po wszystkich elementach stworzonej listy w pkt 15 i wypisz je na ekran podnosząc kazdą wartość do potęgi 2
print('\n- - - - - Zadanie 16')
print(lista_losowa)
#print(ilosc_liczb)
i = 0
while i < ilosc_liczb:
  print(lista_losowa[i]**2)
  i = i+1
