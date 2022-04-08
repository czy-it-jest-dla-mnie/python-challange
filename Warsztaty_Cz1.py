#Warsztaty cz.1 - tak robimy komentarze

# Hello World
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

string = str(zmienna_typu_int)
int = int(zmienna_typu_int)  
float = float(zmienna_typu_int)

print(string) # komenda string + 1 spowodowałaby bład niezgodności typów
print(int + 1)
print(float)

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

print(lista_imion[1])

# 2. Zmień imię Zygmunt na Ilona

lista_imion[-1]='Ilona'

# 3. Dodaj nowe imię 'Pawel' do listy (na koniec listy)

lista_imion.append('Pawel')

# 4. Dodaj nowe imię do list 'Agata' jako drugie

lista_imion.insert(1,'Agata')

# 5. Usuń z listy imię Jadwiga

lista_imion.remove('Jadwiga')

# 6. Wypisz ilość imion w liście (uzywając do tego odpowiedniej metody)

print(len(lista_imion))

# 7. Pomnóz dwie zmienne: liczba_1 oraz liczba_2 i wypisz

print(liczba_1*liczba_2)

# 8. Sprawdź uzywając warunków if/else która zmienna: liczba_1 oraz liczba_2 jest większa i wypisz odpowiedni tekst na ekranie

if liczba_1>liczba_2:
  print('Liczba 1 jest większa od liczby 2')
else:
  print('Liczba 2 jest większa od liczby 1')

# 9. Sprawdź czy na liście imion znajduje się imię 'Jan' i wypisz odpowiedni komunikat

if('Jan' in lista_imion):
    print('Jan znajduje się na liście imion')
else:
    print('Jan nie znajduje się na liście imion')

# 10. Sprawdź czy na liście imion znajduje się imię 'Jan', jezeli tak to sprawdź czy liczba_2 jest większa od liczba_1, jezeli tak to wypisz na ekran drugie i trzecie imię z listy imion

if('Jan' in lista_imion):
  if liczba_2>liczba_1:
    print(lista_imion[1] + ' ' + lista_imion[2])
#swoją drogą - czy da się wypisać oba te imiona pod indeksem 1 i 2 bez dwukrotnego przywoływania tablicy lista_imion? Przy "print(lista_imion[1][2]" wypluwa pierwszą literkę drugiego imienia

# 11. Zmień typ liczba_1 na string a następnie wypisz na ekran

string_1=str(liczba_1)
print(string_1)

# 12. Zmień typ liczba_2 na float i dodaj do niej liczbę 24.5 i wypisz na ekran

float_2 = float(liczba_2)
print(float_2+24.5)

# 13. Wypisz tekst na ekran: 'Wartość liczby_2 to: [tutaj ma się pojawić wartość ze zmiennej]'

print('Wartość liczby_2 to:',liczba_2)

# 14. Sprawdź czy liczba_2 jest większa od liczba_1 LUB lista imion zawiera imię 'Zygmunt' i wypisz na ekranie odpowiedni komunikat.

if liczba_2>liczba_1 or 'Zygmunt' in lista_imion:
  print('liczba_2 jest większa od liczba_1 lub lista_imion zawiera imie Zygmunt')

# 15. * Stwórz nową listę która zawiera 5 elementów losowo wybranych cyfr a następnie dodaj wszystkie elementy do siebie i wypisz na ekranie 
# (tak aby mozna było dynamicznie rozszerzeć wielkość tablicy i zeby suma się liczyła za kazdym razem poprawnie)

import random
print('Ile cyfr powinna zawierać lista?')
ile_cyfr=input()
int_cyfr=int(ile_cyfr)
lista_cyfr=[]

if (len(lista_cyfr)) < int_cyfr:
  for _ in range(int_cyfr): 
      (lista_cyfr.append(random.randint(1,9)))
print('Lista cyfr to:')
print(lista_cyfr)
print('Ich suma wynosi:')
print(sum(lista_cyfr))

# 16. * Przeiteruj po wszystkich elementach stworzonej listy w pkt 15 i wypisz je na ekran podnosząc kazdą wartość do potęgi 2

do_kwadratu = [cyfra ** 2 for cyfra in lista_cyfr]
print('Po podniesieniu każdej liczby do potęgi drugiej uzyskamy:')
print(do_kwadratu)
