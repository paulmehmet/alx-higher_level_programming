#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_us
"""
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
    cur.execute(
        """
        SELECT cities.name FROM cities
        WHERE cities.state_id = (
            SELECT states.id FROM states
            WHERE states.name=%s
        )
        """,
        (sys.argv[4], )
    )
    res = cur.fetchall()
    tmp = [r[0] for r in res]
    print(*tmp, sep=', ')
    cur.close()
    db.close()
