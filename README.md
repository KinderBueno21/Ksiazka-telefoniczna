# Ksiazka-telefoniczna
Mini projekt semestralny, Informatyka EiA 2 Semestr.
W projekcie zostały spełnione wszystkie wymagane warunki do wykonania.
W programie została wykorzystana nakładka PyQt umożliwiająca tworzenie interfejsu graficznego

"Instrukcja programu" 

1.PLIK
  Do działania programu używany jest plik "ksiazka.json". Jesli plik nie istnieje zostanie on automatycznie utworzony przy dodawaniu pierwszej osoby do książki. Funkcje programu nie będą działały jeśli baza jest pusta/nie istnieje. Wyskoczy komunikat o pustej bazie np. po kliknięciu w statystyki.
Dodatkowo: W repozytorium załączyłem plik ksiazka.json zawierający 40 wygenerowanych losowo rekordów. Plik mozna wykorzystać do przetestowania funkcji programu. 

2.DZIAŁANIE PROGRAMU
a) Dodawanie rekordu
  W celu dodania rekordu trzeba wypełnić wszystkie pola! W przeciwnym wypadku wyskoczy komunikat z prośbą o uzupełnienie wszystkich pól. Po dodaniu rekord jest automatycznie zapisywany do pliku ksiazka.json . 

b) Wyszukiwanie
  W celu wyszukania rekordów trzeba wybrać z rozwijanej listy parametr po którym chce się przeszukać książkę telefoniczną. Wtedy trzeba wpisać wyszukiwaną frazę pod rozwijaną listą a następnie kliknąć "Szukaj". Jeśli baza nie jest pusta wyskoczy komunikat ze znalezionymi osobami. Dodatkowo w tabeli na dole programu zostaną wyświetlone znalezione osoby oraz ich wszystkie dane w odpowiednich kolumnach. 
  *Początkowo w tabeli pokazują się wszystkie rekordy! Po wyszukaniu pokażą się tylko wyszukane. W celu ponownego pokazania wszystkich rekordów trzeba wyczyścić pole pod listą i wtedy wyszukać.* 
  

c) Statystyki
Po kliknięciu "Statystyki" pokażą się statystyki: 1. Liczba wszystkich rekordów. 2. Najpopularniejsze miasto. 3. Najpopularniejsze imię. 4. Najpopularniejszy prefiks telefonu (np w celu lokalizacji). Dane są rozpisane w tabeli.

