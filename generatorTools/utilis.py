#-*- coding: utf-8 -*-
from datetime import datetime
import random

current_year = datetime.now().year
current_mount = datetime.now().month
current_day = datetime.now().day


def generate_date(start_year, start_mount, start_day):

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


def parse_date(who_many, start_year, start_mount, start_day):

    for i in range(who_many):
        date = generate_date(start_year, start_mount, start_day)
        # czas umowy na max 6 lat (na sztywno)
        data_in, date_out = date, (date[0] + random.randrange(1, 6, 1), date[1], date[2])
        # Zatrudiony od, zatrudiony do
        print data_in, date_out


def generate_name(file):

    name = ""
    list_name = []

    for lines in file:
        for c in lines.decode('utf8'):

            if c == ' ' or c == '.' or c == '\t' or c in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                if not name.__eq__(""):
                    list_name.append(name)
                    name = ""
                    continue
            else:
                name += c

    return list_name


#przyklad generowania tablic z imionami
file = [line.rstrip('\n') for line in open('imiona_meskie')]

tab_name = generate_name(file)
print [nam for nam in tab_name]
print 'Sa polskie znaki ' + tab_name[0]

#zenskie
file = [line.rstrip('\n') for line in open('imiona_zenskie')]
tab_name = generate_name(file)

tab_name = generate_name(file)
print [nam for nam in tab_name]
print 'Sa polskie znaki ' + tab_name[0]

# mozna uzyc do wygenerowania 10000 pracownikow zatrudionych od 10.02.2002 z czasem umowy na maximum 6 lat
# parse_date(10000, 2002, 2, 10)