#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

db = MySQLdb.connect("localhost","adm","password","temperatura")

curs = db.cursor()


curs.execute("SELECT * FROM dados2 where (tdate>='2016-10-10')")

print "\n   DATE        Time     Informação            Valor            AD[]"
print "==============================================================================="

for reading in curs.fetchall():
    print str(reading[0])+"      "+str(reading[1])+"      "+\
                (reading[2])+"        "+str(reading[3])+"              "+str(reading[4])
    

