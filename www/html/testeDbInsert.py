#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

db = MySQLdb.connect("localhost","adm","password","temperatura")

curs = db.cursor()

try:
    curs.execute("""INSERT INTO dados
            values(CURRENT_DATE() - INTERVAL 1 DAY,NOW(),'Potência',26,'AD5')""")
    curs.execute("""INSERT INTO dados
            values(CURRENT_DATE() - INTERVAL 1 DAY,NOW(),'Temp    ',35,'AD0')""")
    db.commit()
    print"Data Committed"
    
except:
    print"Error: the database is being rolled back"
    db.rollback()
