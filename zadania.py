import time
from datetime import datetime
"""
 Dekorator mierzący czas wykonania funkcji
"""
def mierzenie_czasu(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        end = time.time()
        print(f"Czas wykonania {funkcja.__name__}: {end - start:.4f} sekundy")
        return wynik
    return wrapper

class Zadanie:
    """
    Klasa Zadanie reprezentująca podstawowe zadanie
    """
    def __init__(self, tytul, opis, termin_wykonania, **kwargs):
        self.tytul = tytul
        self.opis = opis
        self.termin_wykonania = termin_wykonania
        self.wykonane = False
        self.dodatkowe_info = kwargs
    
    def __str__(self):
        status = "✔" if self.wykonane else "✘"
        return f"[{status}] {self.venv/tytul} - {self.opis} (Termin: {self.termin_wykonania})"

class ZadaniePriorytetowe(Zadanie):
    """
    Klasa ZadaniePriorytetowe reprezentująca zadanie priorytetowe
    """
    def __init__(self, tytul, opis, termin_wykonania, priorytet, **kwargs):
        super().__init__(tytul, opis, termin_wykonania, **kwargs)
        self.priorytet = int(priorytet)

    def __str__(self):
        return super().__str__() + f" (Priorytet: {self.priorytet})"

class ZadanieRegularne(Zadanie):
    """
    Klasa ZadanieRegularne prezentująca zadanie regularne
    """
    def __init__(self, tytul, opis, termin_wykonania, powtarzalnosc, **kwargs):
        super().__init__(tytul, opis, termin_wykonania, **kwargs)
        self.powtarzalnosc = powtarzalnosc

    def __str__(self):
        return super().__str__() + f" (Powtarzalność: {self.powtarzalnosc})"

class ManagerZadan:
    """
    Zarządzanie listą zadań
    """
    def __init__(self):
        self.lista_zadan = []

    @mierzenie_czasu
    def dodaj_zadanie(self, zadanie):
        self.lista_zadan.append(zadanie)
        print(f"Dodano zadanie: {zadanie}")

    @mierzenie_czasu
    def usun_zadanie(self, zadanie):
        self.lista_zadan.remove(zadanie)
        print(f"Usunięto zadanie: {zadanie}")

    @mierzenie_czasu
    def oznacz_jako_wykonane(self, tytul):
        for zadanie in self.lista_zadan:
            if zadanie.tytul == tytul:
                zadanie.wykonane = True
                print(f"Zadanie oznaczone jako wykonane: {zadanie}")
                return
        print("Nie znaleziono zadania.")

    @mierzenie_czasu
    def edytuj_zadanie(self, tytul, nowy_tytul=None, nowy_opis=None, nowy_termin=None):
        for zadanie in self.lista_zadan:
            if zadanie.tytul == tytul:
                if nowy_tytul:
                    zadanie.tytul = nowy_tytul
                if nowy_opis:
                    zadanie.opis = nowy_opis
                if nowy_termin:
                    zadanie.termin_wykonania = nowy_termin
                print(f"Zaktualizowano zadanie: {zadanie}")
                return
        print("Nie znaleziono zadania.")
    
    def __contains__(self, zadanie):
        return zadanie in self.lista_zadan

    @mierzenie_czasu
    def wyswietl_zadania(self):
        if not self.lista_zadan:
            print("Brak zadań.")
        else:
            for zadanie in sorted(self.lista_zadan, key=lambda x: datetime.strptime(x.termin_wykonania, "%Y-%m-%d")):
                print(zadanie)

    @mierzenie_czasu
    def zapisz_do_pliku(self, nazwa_pliku="zadania.txt"):
        with open(nazwa_pliku, "w", encoding="utf-8") as plik:
            for zadanie in self.lista_zadan:
                plik.write(f"{zadanie.tytul}|{zadanie.opis}|{zadanie.termin_wykonania}|{zadanie.wykonane}\n")
        print("Zadania zapisane do pliku.")

    @mierzenie_czasu
    def wczytaj_z_pliku(self, nazwa_pliku="zadania.txt"):
        try:
            with open(nazwa_pliku, "r", encoding="utf-8") as plik:
                for linia in plik:
                    tytul, opis, termin, wykonane = linia.strip().split("|")
                    zadanie = Zadanie(tytul, opis, termin)
                    zadanie.wykonane = wykonane == "True"
                    self.lista_zadan.append(zadanie)
            print("Zadania wczytane z pliku.")
        except FileNotFoundError:
            print("Brak pliku z zapisanymi zadaniami.")