#-*- coding: utf-8 -*-
import random

def generate_date(start_year, start_mount, start_day):
    from datetime import datetime
    current_year = datetime.now().year
    current_mount = datetime.now().month
    current_day = datetime.now().day

    year = random.randrange(start_year, current_year, 1)

    month = [random.randrange(1, 13, 1) if start_year < year < current_year else
             random.randrange(start_mount, 13, 1) if year == start_year else
             random.randrange(1, current_mount+1, 1)]

    day = [random.randrange(1, 32, 1) if month[0] % 2 == 1 and month[0] != 2 and start_year < year < current_year else
           random.randrange(1, 31, 1) if not month[0] != 2 and start_year < year < current_year else
           random.randrange(1, 31, 1) if start_year < year < current_year else
           random.randrange(start_day, 32, 1) if month[0] % 2 == 1 and month[0] != 2 and year == start_year else
           random.randrange(start_day, 31, 1) if month[0] != 2 and year == start_year else
           random.randrange(start_day, 30, 1) if month[0] == 2 and year == start_year else
           random.randrange(1, current_day+1, 1)]

    return year, month[0], day[0]


def generate_double_date_list(who_many, start_year, start_mount, start_day, delay):

    tab_data = []
    for i in range(who_many):
        date = generate_date(start_year, start_mount, start_day)
        # czas umowy na max 6 lat (na sztywno)
        data_in, date_out = date, (date[0] + random.randrange(1, delay, 1), date[1], date[2])
        # Zatrudiony od, zatrudiony do
        tab_data.append([data_in, date_out])

    return tab_data


def parse_data_one_format(data):

    list_parse = str(data).replace(',','-')
    list_parse = list_parse.replace(' ','')
    list_parse = list_parse.replace('(','')
    return list_parse.replace(')','')


def format_one_double_date_list(who_many, start_year, start_mount, start_day, delay):

    _losowe_daty = generate_double_date_list(who_many, start_year, start_mount, start_day, delay)
    losowa_data = []

    for data in _losowe_daty:
        losowa_data.append([parse_data_one_format(data[0]), parse_data_one_format(data[1])])

    return losowa_data


def format_one_date_list(who_many, start_year, start_mount, start_day):

    tab_data = []
    for i in range(who_many):
        tab_data.append(generate_date(start_year, start_mount, start_day))

    tab_parse_data = []
    for data in tab_data:
        tab_parse_data.append(parse_data_one_format(data))

    return tab_parse_data


def generate_list_from_file(file):

    ele = ""
    list = []

    for lines in file:
        for c in lines.decode('utf8'):

            if c == ' ' or c == '.' or c == '\t' or c in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                if not ele.__eq__(""):
                    list.append(ele)
                    ele = ""
                    continue
            else:
                ele += c

    return list


def parse_xml_street():

    import xml.etree.ElementTree as xml
    print 'Otwieram xml street'
    xmltree = xml.parse('ULIC.xml')
    print 'Wczytano xml'
    print 'Prasuje xml'
    ulice = []
    values = []
    for m in xmltree.iter('catalog'):
        for r in m.iter('row'):
            for v in r.iter('col'):
                if v.attrib['name'] == 'SYM':
                    values.append(v.text)
                if v.attrib['name'] == 'NAZWA_1':
                    values.append(v.text)
            ulice.append(values)
            values = []
    print 'Parsowanie zakonczone'
    return ulice


def get_city(ulice):

    import pandas
    import random
    print 'Otwieram csv city'
    city_csv=pandas.read_csv('simc.csv', encoding='utf-8', sep='\t',header=None)
    print 'Otwarto'
    print 'Losuje liczbe'
    losuj_int = random.randrange(0, len(ulice), 1)
    print 'Losuje ulice'
    street_name = ulice[losuj_int][1]
    street_id = int(ulice[losuj_int][0])
    print 'Wylosowano', street_name, street_id
    print 'Wyszukuje misto'
    for i in range(1, len(city_csv.values)):
        if int(city_csv.values[i][7]) == street_id:
            city_name = city_csv.values[i][6]

    return street_name, city_name


def generate_country_list():
    import pandas

    country =[]
    print 'Otwieram csv country'
    country_csv = pandas.read_csv('lista_krajow.csv', sep='\t', header=None)

    for i in range(len(country_csv)):
        country.append(str(country_csv.values[i][0]).split(',')[1])

    return country

###################TESTS####################################

#przyklad generowania tablic z imionami
# file = [line.rstrip('\n') for line in open('imiona_meskie')]
#
# tab_name = generate_list_from_file(file)
# print [nam for nam in tab_name]
# print 'Sa polskie znaki ' + tab_name[0]
#
# #zenskie
# file = [line.rstrip('\n') for line in open('imiona_zenskie')]
# tab_name = generate_list_from_file(file)
#
# tab_name = generate_list_from_file(file)
# print [nam for nam in tab_name]
# print 'Sa polskie znaki ' + tab_name[0]
#
# #nazwiska
# file = [line.rstrip('\n') for line in open('nazwiska')]
# tab_name = generate_list_from_file(file)
#
# tab_name = generate_list_from_file(file)
# print [nam for nam in tab_name]
# print 'Sa polskie znaki ' + tab_name[2]


# mozna uzyc do wygenerowania 10000 pracownikow zatrudionych od 10.02.2002 z czasem umowy na maximum 6 lat
# parse_date(10000, 2002, 2, 10)