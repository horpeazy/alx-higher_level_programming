#!/usr/bin/python3
"""
Lists all states from the database
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from states WHERE name = '{}'".format(sys.argv[4]))
    for row in cur.fetchall():
        if row[1] == sys.argv[4]:
            print(row)
