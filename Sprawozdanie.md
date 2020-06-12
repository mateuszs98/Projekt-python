###Sprawozdanie projekt Jêzyki Symboliczne 
###"Okrêty"

Mateusz Sitek
Nr. Albumu: 130581

###Za³o¿enia projektowe

Za³o¿eniem projektu by³o stworzenie gry strategicznej w Okrêty.
Gra zosta³a wykonana w jêzyku programowania Python.
Sposób dzia³ania i zachowania gry jest stworzony wed³ug zaleceñ prowadz¹cego 
i udostepnionych przez niego materia³ów.

###Przebieg

Program zosta³ napisany przy pomocy biblioteki Pygame. Pygame okaza³ siê 
funkcjonalny w pisaniu gry, wiele problemów zosta³o poruszone w poradnikach,
dokumentacji i na forach internetowych.
Ca³y program podzielony jest na cztery pliki. Plik START.py
odpowiedzialny jest za poprawne uruchomienie gry, plik MyException.py zawiera jedynie klasê wyj¹tków. 
W pliku Interfejs.py umieœci³em kod odpowiedzialny za widoczne aspekty gry,
w tym klasê Window zawieraj¹c¹ metodê wirtualn¹, klasê AlienShip, odpowiadaj¹c¹ za drugiego gracza – komputer,
dziedzicz¹c¹ po klasie Ship i korzystaj¹ce z metody wirtualnej getPositionInField.
U¿ywam tu równie¿ wyj¹tków, przy funkcji odpowiadaj¹cej za rysowanie statków,
wyra¿enia lambda do ustalania rozmiaru rysowanego statku jak i list comprehensions do tworzenia pól gry. 
W pliku Gra.py mieœci siê ca³a logika gry.
Wykorzystujê tu równie¿ bibliotekê Random w celu losowego ustalania pozycji statków komputera
i losowych strza³ów na nasze okrêty.
Spotkamy siê z g³ówn¹ klas¹ Battle, dziedzicz¹c¹ po klasie Window.
W tej czêœci programu korzystam z wyra¿eñ lambda w celu operacji na polach wokó³ statku,
a za pomoc¹ list comprehensions obs³ugujê tablicê celnych i spud³owanych strza³ów.
G³ównym problemem by³o obmyœlenie prawid³owego zachowania po celnym strzale komputera (superInstynkt)
jak i odpowiednie przechowywanie wszystkich danych, np.takich jak oddane strza³y.

###Linki
*Lambda-wyra¿enia
Lambda do sprawdzania pol woko³o statku
https://github.com/mateuszs98/Projekt-python/blob/328db4690c866f55608e09be7b3c7bdfe3c89798/Gra.py#L364
Lambda do usuwania pól
https://github.com/mateuszs98/Projekt-python/blob/328db4690c866f55608e09be7b3c7bdfe3c89798/Gra.py#L376
Lambda do sprawdzenia rozmiaru statku
https://github.com/mateuszs98/Projekt-python/blob/328db4690c866f55608e09be7b3c7bdfe3c89798/Interfejs.py#L120
* List comprehensions
Usuwanie z generalnej tabeli tego co by³o w tymczasowych tablicach (list comprehension x2)
https://github.com/mateuszs98/Projekt-python/blob/328db4690c866f55608e09be7b3c7bdfe3c89798/Gra.py#L311-L315
https://github.com/mateuszs98/Projekt-python/blob/328db4690c866f55608e09be7b3c7bdfe3c89798/Interfejs.py#L118
https://github.com/mateuszs98/Projekt-python/blob/328db4690c866f55608e09be7b3c7bdfe3c89798/Gra.py#L372
* Klasy
Klasa AlienShip dziedziczaca po klasie Ship
https://github.com/mateuszs98/Projekt-python/blob/328db4690c866f55608e09be7b3c7bdfe3c89798/Interfejs.py#L82
Klasa Battle dziedzicz¹ca po klasie Window
https://github.com/mateuszs98/Projekt-python/blob/328db4690c866f55608e09be7b3c7bdfe3c89798/Gra.py#L3
