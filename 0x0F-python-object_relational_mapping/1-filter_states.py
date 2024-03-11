#!/usr/bin/python3
'''
Write a script that lists all states starting with `N`
from the database hbtn_0e_0_usa:
'''
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    res = cur.fetchall()
    for r in res:
        print(r)
    cur.close()
    db.close()
