# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 19:37:22 2018

@author: Administrator
"""

import sqlite3 as sql

conn = sql.connect('email.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('''
CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER)
              ''')

cur.execute('''

INSERT INTO Ages (name, age) VALUES ('Heidar', 37);
INSERT INTO Ages (name, age) VALUES ('Megg', 20);
INSERT INTO Ages (name, age) VALUES ('Hui', 35);
INSERT INTO Ages (name, age) VALUES ('Pearsen', 14);
INSERT INTO Ages (name, age) VALUES ('Ines', 32);
INSERT INTO Ages (name, age) VALUES ('Rexford', 28);
''')
cur.execute('SELECT * FROM Ages')

conn.commit()
for row in cur.execute('SELECT * FROM Ages'):
    print(str(row))
