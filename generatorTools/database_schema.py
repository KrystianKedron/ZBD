import utilis
import random


class Osoba():

    id_osoba = 0
    imie = ""
    nazwisko = ""
    ulica = ""
    nr_domu = 0
    nr_mieszkania = 0
    miejscowosc = ""
    id_kraju = ""

    def __init__(self, last_id, imie, nazwisko, ulica, nr_domu, nr_mieszkania, miejscowosc, id_kraju):

        self.id_osoba = last_id + 1
        #unicode fix
        self.imie = imie[0]
        self.nazwisko = nazwisko
        self.ulica = ulica
        self.nr_domu = nr_domu
        self.nr_mieszkania = nr_mieszkania
        self.miejscowosc = miejscowosc
        self.id_kraju = id_kraju


class Kraj():

    id_kraju = 0
    kraj = ''

    def __init__(self, id_kraju, kraj):

        self.id_kraju = id_kraju
        self.kraj = kraj


class Polaczenie():

    id_polaczenia = 0
    kraj_nadania = ''
    kraj_odbioru = ''

    def __init__(self, id_polaczenia, kraj_nadania, kraj_odbioru):

        self.id_polaczenia = id_polaczenia
        self.kraj_nadania = kraj_nadania
        self.kraj_odbioru = kraj_odbioru


class Tranzyt():

    id_polaczenia = 0
    id_przesylki = 0
    data_odbioru = ''
    data_nadania = ''

    def __init__(self, id_polaczenia, id_przesylki, data_odbioru, data_nadania):

        self.id_polaczenia = id_polaczenia
        self.id_przesylki = id_przesylki
        self.data_odbioru = data_odbioru
        self.data_nadania = data_nadania


class Pracownik():

    id_pracowniaka = 0
    imie = ''
    nazwisko = ''
    pesel = 0
    data_zatrudnienia = ''
    zatrudniony_do = ''

    def __init__(self, id_pracowniaka, imie, nazwisko, pesel, data_zatrudnienia, zatrudniony_do):

        self.id_pracowniaka = id_pracowniaka
        self.imie = imie[0]
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.data_zatrudnienia = data_zatrudnienia
        self.zatrudniony_do = zatrudniony_do


class Przesylka():

    id_przesylki = 0
    id_pracownika = 0
    odbiorca = 0
    nadawca = 0
    data_otrzymania = ''
    data_wydania = ''
    waga = 0.0
    rodzaj = ''
    clo = 0
    vat = 0

    def __init__(self, id_przesylki, id_pracownika, odbiorca, nadawca, data_otrzymania, data_wydania, waga, rodzaj, clo, vat):
        self.id_przesylki = id_przesylki
        self.id_pracownika = id_pracownika
        self.odbiorca = odbiorca
        self.nadawca = nadawca
        self.data_otrzymania = data_otrzymania
        self.data_wydania = data_wydania
        self.waga = waga
        self.rodzaj = rodzaj
        self.clo = clo
        self.vat = vat

def main():

    file_name = {0: "imiona_meskie", 1: "imiona_zenskie", 2: "nazwiska" }

    # tab_ulice = utilis.parse_xml_street()
    # ulica, miasto = utilis.get_city(tab_ulice)

    tab_imion_m = utilis.generate_list_from_file(line.rstrip('\n') for line in open(file_name[0]))
    tab_imion_z = utilis.generate_list_from_file(line.rstrip('\n') for line in open(file_name[1]))
    tab_nazwisk = utilis.generate_list_from_file(line.rstrip('\n') for line in open(file_name[2]))

    tab_kraje = utilis.generate_country_list()

    tab_double_data = utilis.format_one_double_date_list(10, 2000, 1, 1, 6)
    tab_data = utilis.format_one_date_list(10, 2000, 1, 1)



    # osoba = Osoba(0, [tab_imion_m[random.randrange(0, len(tab_imion_m), 1)] if random.randrange(0, 2, 1) else tab_imion_m[random.randrange(0, len(tab_imion_z), 1)]],
    #               tab_nazwisk[random.randrange(0, len(tab_nazwisk), 1)], ulica, random.randrange(0, 1000, 1), random.randrange(0, 100, 1), miasto, 1)

    # print "Wygenerowana osoba", osoba.id_osoba, osoba.imie, osoba.nazwisko, osoba.ulica, osoba.nr_domu, osoba.nr_mieszkania, osoba.miejscowosc, osoba.id_kraju

main()
