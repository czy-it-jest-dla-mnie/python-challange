 #1. Wypisz tekst na konsoli 
from ntpath import join


print('\n- - - - - Zadanie 1')
tekst = "Hello World!"
 

#2. Dodaj dwie liczby i wyświetl na konsoli
print('\n- - - - - Zadanie 2')
a = 5
b = 10
print(a+b)

#3. Przypisz tekst "test" do trzech zmiennych (x,y,z) za pomocą jednej komendy ( w jednej linijce kodu )
print('\n- - - - - Zadanie 3')
x = y = z = ("test")
print(x)
print(y)
print(z)

#4. Skonwertuj liczbę 6.5 do liczy całkowitej i przypisz do zmiennej d i wypisz
print('\n- - - - - Zadanie 4')
c = 6.5
d = int(c)
print(int(d))

#5. Wypisz ilość znaków w tekście "Hello World"
print('\n- - - - - Zadanie 5')
print(len("Hello World"))

#6. Wypisz pierwszy znak z tekstu "Hello World" - używając zmiennej e
print('\n- - - - - Zadanie 6')
e = "Hello World"
print(e[0])

#7. Usuń spacje z napisu "Hello  World " i wypisz
f = "Hello  World "
g = ''.join(f)
print(g)

#8. Dodaj element "Chevrolet" jako ostatni do listy samochodów 
print('\n- - - - - Zadanie 8')
cars = ["Dodge", "RAM"]
cars.append("Chevrolet")
print(cars)

#9. Usuń element "RAM" z listy samochodów
print('\n- - - - - Zadanie 9')
cars.remove("RAM")
print(cars)

#10. Wypisz 2, 3 i 4 element z listy używając zakresu indeksów
print('\n- - - - - Zadanie 10')
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[1:4])

#11. Wypisz wielkość tablicy 'fruits'
print('\n- - - - - Zadanie 11')
print(len(fruits))

#12. Wypisz wszystkie owoce za pomocą pętli 'for'
print('\n- - - - - Zadanie 12')
for i in fruits:
    print(i)

#13. Stwórz funkcję która wypisuje podany w parametrze tekst a następnie ją wywołaj
print('\n- - - - - Zadanie 13')
zmienna = input("Wprowadź z klawiatury jakiś tekst: ")
print(zmienna)




