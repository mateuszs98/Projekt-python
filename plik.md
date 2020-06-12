###Sprawozdanie projekt J�zyki Symboliczne 
###"Okr�ty"

Mateusz Sitek
Nr. Albumu: 130581

###Za�o�enia projektowe

Za�o�eniem projektu by�o stworzenie gry strategicznej w Okr�ty.
Gra zosta�a wykonana w j�zyku programowania Python.
Spos�b dzia�ania i zachowania gry jest stworzony wed�ug zalece� prowadz�cego 
i udostepnionych przez niego materia��w.

###Przebieg

Program zosta� napisany przy pomocy biblioteki Pygame. Pygame okaza� si� 
funkcjonalny w pisaniu gry, wiele problem�w zosta�o poruszone w poradnikach,
dokumentacji i na forach internetowych.
Ca�y program podzielony jest na cztery pliki. Plik START.py
odpowiedzialny jest za poprawne uruchomienie gry, plik MyException.py zawiera jedynie klas� wyj�tk�w. 
W pliku Interfejs.py umie�ci�em kod odpowiedzialny za widoczne aspekty gry,
w tym klas� Window zawieraj�c� metod� wirtualn�, klas� AlienShip, odpowiadaj�c� za drugiego gracza � komputer,
dziedzicz�c� po klasie Ship i korzystaj�ce z metody wirtualnej getPositionInField.
U�ywam tu r�wnie� wyj�tk�w, przy funkcji odpowiadaj�cej za rysowanie statk�w,
wyra�enia lambda do ustalania rozmiaru rysowanego statku jak i list comprehensions do tworzenia p�l gry. 
W pliku Gra.py mie�ci si� ca�a logika gry.
Wykorzystuj� tu r�wnie� bibliotek� Random w celu losowego ustalania pozycji statk�w komputera
i losowych strza��w na nasze okr�ty.
Spotkamy si� z g��wn� klas� Battle, dziedzicz�c� po klasie Window.
W tej cz�ci programu korzystam z wyra�e� lambda w celu operacji na polach wok� statku,
a za pomoc� list comprehensions obs�uguj� tablic� celnych i spud�owanych strza��w.
G��wnym problemem by�o obmy�lenie prawid�owego zachowania po celnym strzale komputera (superInstynkt)
jak i odpowiednie przechowywanie wszystkich danych, np.takich jak oddane strza�y.

###Linki
*Lambda-wyra�enia
Lambda do sprawdzania pol woko�o statku
https://github.com/mateuszs98/Projekt-python/blob/328db4690c866f55608e09be7b3c7bdfe3c89798/Gra.py#L364
Lambda do usuwania p�l
https://github.com/mateuszs98/Projekt-python/blob/328db4690c866f55608e09be7b3c7bdfe3c89798/Gra.py#L376
Lambda do sprawdzenia rozmiaru statku
https://github.com/mateuszs98/Projekt-python/blob/328db4690c866f55608e09be7b3c7bdfe3c89798/Interfejs.py#L120
* List comprehensions
Usuwanie z generalnej tabeli tego co by�o w tymczasowych tablicach (list comprehension x2)
https://github.com/mateuszs98/Projekt-python/blob/328db4690c866f55608e09be7b3c7bdfe3c89798/Gra.py#L311-L315
https://github.com/mateuszs98/Projekt-python/blob/328db4690c866f55608e09be7b3c7bdfe3c89798/Interfejs.py#L118
https://github.com/mateuszs98/Projekt-python/blob/328db4690c866f55608e09be7b3c7bdfe3c89798/Gra.py#L372
* Klasy
Klasa AlienShip dziedziczaca po klasie Ship
https://github.com/mateuszs98/Projekt-python/blob/328db4690c866f55608e09be7b3c7bdfe3c89798/Interfejs.py#L82
Klasa Battle dziedzicz�ca po klasie Window
https://github.com/mateuszs98/Projekt-python/blob/328db4690c866f55608e09be7b3c7bdfe3c89798/Gra.py#L3
