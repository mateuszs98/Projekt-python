## Okrêty (https://pl.wikipedia.org/wiki/Okr%C4%99ty)
### Opis zadania
* Okno z dwoma planszami 10x10 pól (np. siatki przycisków) oraz
przyciskiem rozpoczêcia gry i przyciskiem reset.
* Na pocz¹tku gracz rozmieszcza okrêty (1x czteromasztowiec, 2x trójmasztowiec, 3x
dwumasztowiec, 4x jednomasztowiec).
* Po rozmieszczeniu okrêtów przez gracza i wciœniêciu przycisku nowej gry
przeciwnik komputerowy losowo rozmieszcza swoje okrêty.
* Okrêty nie mog¹ siê dotykaæ ani bokami ani rogami.
* Po rozmieszczeniu okrêtów przez obu graczy jeden z nich wykonuje pierwszy ruch
(losowo gracz lub komputer).
* Wybór celu przez gracza nastêpuje przez klikniêcie pola, w razie trafienia przycisk
staje siê czerwony, w przeciwnym razie niebieski (nie mo¿na strzeliæ dwa razy w to
samo pole).
* Komputer strzela w losowe, nie wybrane wczeœniej pole. Po trafieniu próba
znalezienia orientacji statku i zestrzelenie go do koñca.
* Gra koñczy siê gdy któryœ gracz straci ostatni okrêt, wyœwietlane jest okno
z informacj¹ o zwyciêzcy (np. “Wygrana!”, “Przegrana!”).
* Opcjonalnie: bardziej zaawansowana sztuczna inteligencja omijaj¹ca pola na
których na pewno nie mo¿e znaleŸæ siê okrêt gracza.
### Testy
1. Próba niepoprawnego ustawienia okrêtu (stykanie siê bokami lub
rogami). Oczekiwana informacja o b³êdzie
2. Poprawne rozmieszczenie wszystkich okrêtów przez gracza i wciœniêcie
przycisku rozpoczêcia gry.
3. Strzelenie w puste pole.
4. Trafienie w okrêt przeciwnika.
5. Próba zestrzelenia swojego okrêtu - oczekiwane niepowodzenie.
6. Próba ponownego strzelenia w puste pole - oczekiwane niepowodzenie.
7. Próba ponownego strzelenia w okrêt przeciwnika - oczekiwane niepowodzenie.
8. Rozmieszczenie czêœci okrêtów, wciœniêcie przycisku reset - oczekiwany
reset plansz.
9. Poprawne rozmieszczenie wszystkich okrêtów, oddanie kilku strza³ów, rozpoczêcie
nowej gry, ponowne poprawne rozmieszczenie okrêtów, oddanie strza³ów w te same
pola.
10. Wygranie gry (np. Przez pokazanie okrêtów przeciwnika). Rozpoczêcie nowej
gry bez ponownego uruchamiania programu.
11. Przegranie gry (np. Przez aktywacjê super-instynktu gracza komputera).
Rozpoczêcie nowej gry bez ponownego uruchamiania programu.

Link do repozytorium: [GitHub](https://github.com/mateuszs98/Projekt-python)