## Okr�ty (https://pl.wikipedia.org/wiki/Okr%C4%99ty)
### Opis zadania
* Okno z dwoma planszami 10x10 p�l (np. siatki przycisk�w) oraz
przyciskiem rozpocz�cia gry i przyciskiem reset.
* Na pocz�tku gracz rozmieszcza okr�ty (1x czteromasztowiec, 2x tr�jmasztowiec, 3x
dwumasztowiec, 4x jednomasztowiec).
* Po rozmieszczeniu okr�t�w przez gracza i wci�ni�ciu przycisku nowej gry
przeciwnik komputerowy losowo rozmieszcza swoje okr�ty.
* Okr�ty nie mog� si� dotyka� ani bokami ani rogami.
* Po rozmieszczeniu okr�t�w przez obu graczy jeden z nich wykonuje pierwszy ruch
(losowo gracz lub komputer).
* Wyb�r celu przez gracza nast�puje przez klikni�cie pola, w razie trafienia przycisk
staje si� czerwony, w przeciwnym razie niebieski (nie mo�na strzeli� dwa razy w to
samo pole).
* Komputer strzela w losowe, nie wybrane wcze�niej pole. Po trafieniu pr�ba
znalezienia orientacji statku i zestrzelenie go do ko�ca.
* Gra ko�czy si� gdy kt�ry� gracz straci ostatni okr�t, wy�wietlane jest okno
z informacj� o zwyci�zcy (np. �Wygrana!�, �Przegrana!�).
* Opcjonalnie: bardziej zaawansowana sztuczna inteligencja omijaj�ca pola na
kt�rych na pewno nie mo�e znale�� si� okr�t gracza.
### Testy
1. Pr�ba niepoprawnego ustawienia okr�tu (stykanie si� bokami lub
rogami). Oczekiwana informacja o b��dzie
2. Poprawne rozmieszczenie wszystkich okr�t�w przez gracza i wci�ni�cie
przycisku rozpocz�cia gry.
3. Strzelenie w puste pole.
4. Trafienie w okr�t przeciwnika.
5. Pr�ba zestrzelenia swojego okr�tu - oczekiwane niepowodzenie.
6. Pr�ba ponownego strzelenia w puste pole - oczekiwane niepowodzenie.
7. Pr�ba ponownego strzelenia w okr�t przeciwnika - oczekiwane niepowodzenie.
8. Rozmieszczenie cz�ci okr�t�w, wci�ni�cie przycisku reset - oczekiwany
reset plansz.
9. Poprawne rozmieszczenie wszystkich okr�t�w, oddanie kilku strza��w, rozpocz�cie
nowej gry, ponowne poprawne rozmieszczenie okr�t�w, oddanie strza��w w te same
pola.
10. Wygranie gry (np. Przez pokazanie okr�t�w przeciwnika). Rozpocz�cie nowej
gry bez ponownego uruchamiania programu.
11. Przegranie gry (np. Przez aktywacj� super-instynktu gracza komputera).
Rozpocz�cie nowej gry bez ponownego uruchamiania programu.

Link do repozytorium: [GitHub](https://github.com/mateuszs98/Projekt-python)