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

# 2. Zmień imię Zygmunt na Ilona

# 3. Dodaj nowe imię 'Pawel' do listy (na koniec listy)

# 4. Dodaj nowe imię do list 'Agata' jako drugie

# 5. Usuń z listy imię Jadwiga

# 6. Wypisz ilość imion w liście (uzywając do tego odpowiedniej metody)

# 7. Pomnóz dwie zmienne: liczba_1 oraz liczba_2 i wypisz

# 8. Sprawdź uzywając warunków if/else która zmienna: liczba_1 oraz liczba_2 jest większa i wypisz odpowiedni tekst na ekranie

# 9. Sprawdź czy na liście imion znajduje się imię 'Jan' i wypisz odpowiedni komunikat

# 10. Sprawdź czy na liście imion znajduje się imię 'Jan', jezeli tak to sprawdź czy liczba_2 jest większa od liczba_1, jezeli tak to wypisz na ekran drugie i trzecie imię z listy imion

# 11. Zmień typ liczba_1 na string a następnie wypisz na ekran

# 12. Zmień typ liczba_2 na float i dodaj do niej liczbę 24.5 i wypisz na ekran

# 13. Wypisz tekst na ekran: 'Wartość liczby_2 to: [tutaj ma się pojawić wartość ze zmiennej]'

# 14. Sprawdź czy liczba_2 jest większa od liczba_1 LUB lista imion zawiera imię 'Zygmunt' i wypisz na ekranie odpowiedni komunikat.

# 15. * Stwórz nową listę która zawiera 5 elementów losowo wybranych cyfr a następnie dodaj wszystkie elementy do siebie i wypisz na ekranie 
# (tak aby mozna było dynamicznie rozszerzeć wielkość tablicy i zeby suma się liczyła za kazdym razem poprawnie)

# 16. * Przeiteruj po wszystkich elementach stworzonej listy w pkt 15 i wypisz je na ekran podnosząc kazdą wartość do potęgi 2
