import json
from collections import Counter

from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QWidget, QPushButton, QLabel,
    QLineEdit, QComboBox, QMessageBox, QTableWidget, QTableWidgetItem,
    QDialog, QHeaderView
)
# Wstępne zdefiniowanie funkcji
def odswieztabele(dane): ...
def kliknieto():...
def pokaz_statystyki():...
def szukaniecombo():...
def pokaz_wyniki(wyniki):...
# Tabela 
program = QApplication([])
tabela = QTableWidget()
tabela.setColumnCount(7)
tabela.setHorizontalHeaderLabels(
    ["Imię", "Nazwisko", "Telefon", "Miasto",
     "Ulica", "Numer domu", "Kod pocztowy"]
)
tabela.setEditTriggers(QTableWidget.NoEditTriggers)
tabela.verticalHeader().setVisible(False)

# Plik
try:
    with open("ksiazka.json", "r", encoding="utf-8") as plik:
        kontakty = json.load(plik)
except FileNotFoundError:
    kontakty = []

# Okno i pola
okno   = QWidget()
okno.setWindowTitle("Ksiazka telefoniczna")
okno.resize(800, 500)
uklad = QVBoxLayout(okno)

etykieta = QLabel("Dodaj kontakt")
imie         = QLineEdit(); imie.setPlaceholderText("Imię")
nazwisko     = QLineEdit(); nazwisko.setPlaceholderText("Nazwisko")
telefon      = QLineEdit(); telefon.setPlaceholderText("+48123456789")
ulica        = QLineEdit(); ulica.setPlaceholderText("Ulica")
numer        = QLineEdit(); numer.setPlaceholderText("Numer domu")
miasto       = QLineEdit(); miasto.setPlaceholderText("Miasto")
kod_pocztowy = QLineEdit(); kod_pocztowy.setPlaceholderText("Kod pocztowy")
szukanepole  = QLineEdit(); szukanepole.setPlaceholderText("Wpisz frazę…")

przycisk_dodaj = QPushButton("Dodaj")
przyciskszuk  = QPushButton("Szukaj")
przyciskstatystyki = QPushButton("Statystyki")
combo = QComboBox()
combo.addItems([
    "Imię", "Nazwisko", "Telefon",
    "Ulica", "Miasto", "Numer domu", "Kod pocztowy"
])

# Funkcje i ich uzupełnienia
def odswieztabele(dane):
    tabela.setRowCount(len(dane))
    for i, k in enumerate(dane):
        tabela.setItem(i, 0, QTableWidgetItem(k.get("imie", "")))
        tabela.setItem(i, 1, QTableWidgetItem(k.get("nazwisko", "")))
        tabela.setItem(i, 2, QTableWidgetItem(k.get("telefon", "")))
        tabela.setItem(i, 3, QTableWidgetItem(k.get("miasto", "")))
        tabela.setItem(i, 4, QTableWidgetItem(k.get("ulica", "")))
        tabela.setItem(i, 5, QTableWidgetItem(k.get("numer_domu", "")))
        tabela.setItem(i, 6, QTableWidgetItem(k.get("kod_pocztowy", "")))

def kliknieto():
    wymagane = [imie, nazwisko, telefon, ulica, numer, miasto, kod_pocztowy]
    if any(not w.text().strip() for w in wymagane):
        QMessageBox.warning(okno, "Brak danych",
                            "Uzupełnij wszystkie pola, zanim dodasz kontakt.")
        return                      
    for k in kontakty:
        if k['imie'] == imie.text() and k['nazwisko'] == nazwisko.text() and k['miasto']==miasto.text() and k['ulica']==ulica.text():
            QMessageBox.warning(okno, "Błąd", "Kontakt już istnieje.")
            return
    kontakt = {
        "imie": imie.text(),
        "nazwisko": nazwisko.text(),
        "telefon": telefon.text(),
        "ulica": ulica.text(),
        "numer_domu": numer.text(),
        "miasto": miasto.text(),
        "kod_pocztowy": kod_pocztowy.text()
    }
    kontakty.append(kontakt)
    with open("ksiazka.json", "w", encoding="utf-8") as plik:
        json.dump(kontakty, plik, ensure_ascii=False, indent=2)

    etykieta.setText(f"Dodano: {kontakt['imie']} {kontakt['nazwisko']}")
    for w in (imie, nazwisko, telefon, ulica, numer, miasto, kod_pocztowy):
        w.clear()
    odswieztabele(kontakty)

def pokaz_wyniki(wyniki):
    if not wyniki:
        tabela.clearContents()
        tabela.setRowCount(0)
        QMessageBox.information(okno, "Brak wyników", "Nie znaleziono kontaktów.")
        return
    odswieztabele(wyniki)
    tekst = "\n".join(
        f"{i+1}. {k['imie']} {k['nazwisko']} – {k['telefon']}"
        for i, k in enumerate(wyniki)
    )
    QMessageBox.information(okno, "Wyniki wyszukiwania", tekst)

def szukaniecombo():
    rodzaj  = combo.currentText()
    szukane = szukanepole.text().lower()
    wyniki  = []

    for k in kontakty:
        if rodzaj == "Imię" and szukane in k['imie'].lower():
            wyniki.append(k)
        elif rodzaj == "Nazwisko" and szukane in k['nazwisko'].lower():
            wyniki.append(k)
        elif rodzaj == "Telefon" and szukane in k['telefon']:
            wyniki.append(k)
        elif rodzaj == "Ulica" and szukane in k.get('ulica', '').lower():
            wyniki.append(k)
        elif rodzaj == "Miasto" and szukane in k.get('miasto', '').lower():
            wyniki.append(k)
        elif rodzaj == "Numer domu" and szukane in k.get('numer_domu', ''):
            wyniki.append(k)
        elif rodzaj == "Kod pocztowy" and szukane in k.get('kod_pocztowy', ''):
            wyniki.append(k)

    szukanepole.clear()
    pokaz_wyniki(wyniki)

def pokaz_statystyki():
    if not kontakty:
        QMessageBox.information(okno, "Brak danych",
                                 "Baza kontaktów jest pusta.")
        return

    miasta = [k["miasto"].strip().title()
              for k in kontakty
              if k.get("miasto") and k["miasto"].strip()]

    imiona = [k["imie"].strip().title()
              for k in kontakty
              if k.get("imie") and k["imie"].strip()]

    miasto_cnt = Counter(miasta)
    imie_cnt   = Counter(imiona)

    caloscc = len(kontakty)
    miasto_top, miasto_top_n = miasto_cnt.most_common(1)[0] \
                               if miasto_cnt else ("<brak>", 0)
    imie_top, imie_top_n     = imie_cnt.most_common(1)[0]   \
                               if imie_cnt   else ("<brak>", 0)

    # Prefiks tel
    def pref(nr: str) -> str:
        nr = (nr or "").strip()
        return nr[:3] if nr.startswith("+") else "<brak>"

    pref_cnt = Counter(pref(k.get("telefon", "")) for k in kontakty)
    if pref_cnt:
        pref_top, pref_top_n = pref_cnt.most_common(1)[0]
    else:
        pref_top, pref_top_n = "<brak>", 0

    
    okkno = QDialog(okno)
    okkno.setWindowTitle("Statystyki")

    tbl = QTableWidget(okkno)
    tbl.setColumnCount(2)
    tbl.setHorizontalHeaderLabels(["Statystyka", "Wartość"])
    tbl.verticalHeader().setVisible(False)
    tbl.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
    tbl.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
    okkno.resize(900,500)
    wiersze = [
        ("Liczba wszystkich kontaktów", caloscc),
        ("Najpopularniejsze miasto",   f"{miasto_top} ({miasto_top_n})"),
        ("Najpopularniejsze imię",     f"{imie_top} ({imie_top_n})"),
        ("Najpopularniejszy prefiks tel.", f"{pref_top} ({pref_top_n})")
    ]

    tbl.setRowCount(len(wiersze))
    for i, (a, b) in enumerate(wiersze):
        tbl.setItem(i, 0, QTableWidgetItem(str(a)))
        tbl.setItem(i, 1, QTableWidgetItem(str(b)))

    QVBoxLayout(okkno).addWidget(tbl)
    okkno.resize(420, 250)
    okkno.exec_()




# Łączenie przycisków i funkcji 
przycisk_dodaj.clicked.connect(kliknieto)
przyciskszuk.clicked.connect(szukaniecombo)
przyciskstatystyki.clicked.connect(pokaz_statystyki)

# Gui
for w in (
    etykieta, imie, nazwisko, telefon, ulica, numer,
    miasto, kod_pocztowy, przycisk_dodaj,
    combo, szukanepole, przyciskszuk,
    tabela, przyciskstatystyki
):
    uklad.addWidget(w)

# Start 
odswieztabele(kontakty)
okno.show()
program.exec_()
