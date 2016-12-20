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


def main():

    file_name = {0: "imiona_meskie", 1: "imiona_zenskie", 2: "nazwiska" }

    tab_ulice = utilis.parse_xml_street()
    ulica, miasto = utilis.get_city(tab_ulice)

    tab_imion_m = utilis.generate_list_from_file(line.rstrip('\n') for line in open(file_name[0]))
    tab_imion_z = utilis.generate_list_from_file(line.rstrip('\n') for line in open(file_name[1]))
    tab_nazwisk = utilis.generate_list_from_file(line.rstrip('\n') for line in open(file_name[2]))

    osoba = Osoba(0, [tab_imion_m[random.randrange(0, len(tab_imion_m), 1)] if random.randrange(0, 2, 1) else tab_imion_m[random.randrange(0, len(tab_imion_z), 1)]],
                  tab_nazwisk[random.randrange(0, len(tab_nazwisk), 1)], ulica, random.randrange(0, 1000, 1), random.randrange(0, 100, 1), miasto, 1)

    print "Wygenerowana osoba", osoba.id_osoba, osoba.imie, osoba.nazwisko, osoba.ulica, osoba.nr_domu, osoba.nr_mieszkania, osoba.miejscowosc, osoba.id_kraju

main()
