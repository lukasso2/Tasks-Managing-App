from zadania import Zadanie, ZadaniePriorytetowe, ZadanieRegularne, ManagerZadan

def menu():
    manager = ManagerZadan()
    manager.wczytaj_z_pliku()  
    
    while True:
        print("\n--- MENU ---")
        print("1. Dodaj zadanie")
        print("2. Usuń zadanie")
        print("3. Oznacz jako wykonane")
        print("4. Edytuj zadanie")
        print("5. Wyświetl zadania")
        print("6. Zapisz zadania do pliku")
        print("7. Wyjdź")
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            tytul = input("Tytuł: ")
            opis = input("Opis: ")
            termin = input("Termin (YYYY-MM-DD): ")
            typ = input("Typ (priorytetowe/regularne/zwykłe): ")
            dodatkowe_info = {}
            
            if typ == "priorytetowe":
                priorytet = input("Priorytet (1-5): ")
                zadanie = ZadaniePriorytetowe(tytul, opis, termin, priorytet, **dodatkowe_info)
            elif typ == "regularne":
                powtarzalnosc = input("Powtarzalność (np. codziennie, co tydzień): ")
                zadanie = ZadanieRegularne(tytul, opis, termin, powtarzalnosc, **dodatkowe_info)
            else:
                zadanie = Zadanie(tytul, opis, termin, **dodatkowe_info)
            
            manager.dodaj_zadanie(zadanie)

        elif wybor == "2":
            tytul = input("Podaj tytuł zadania do usunięcia: ")
            zadanie = next((z for z in manager.lista_zadan if z.tytul == tytul), None)
            if zadanie:
                manager.usun_zadanie(zadanie)
            else:
                print("Nie znaleziono zadania.")

        elif wybor == "3":
            tytul = input("Podaj tytuł zadania do oznaczenia jako wykonane: ")
            manager.oznacz_jako_wykonane(tytul)

        elif wybor == "4":
            tytul = input("Podaj tytuł zadania do edycji: ")
            nowy_tytul = input("Nowy tytuł (pozostaw puste, aby nie zmieniać): ") or None
            nowy_opis = input("Nowy opis (pozostaw puste, aby nie zmieniać): ") or None
            nowy_termin = input("Nowy termin (YYYY-MM-DD, pozostaw puste, aby nie zmieniać): ") or None
            manager.edytuj_zadanie(tytul, nowy_tytul, nowy_opis, nowy_termin)

        elif wybor == "5":
            manager.wyswietl_zadania()

        elif wybor == "6":
            manager.zapisz_do_pliku()
            print("Zadania zapisane do pliku.")

        elif wybor == "7":
            print("Zamykanie aplikacji.")
            manager.zapisz_do_pliku()
            break
        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")

if __name__ == "__main__":
    menu()