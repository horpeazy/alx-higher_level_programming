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
    cur.execute("SELECT cities.name, states.name\
    FROM cities JOIN states ON states.id = cities.state_id \
    WHERE states.name = (%s);", (sys.argv[4],))
    cities = cur.fetchall()
    for i in range(len(cities)):
        if cities[i][1] == sys.argv[4]:
            if i == len(cities) - 1:
                print(cities[i][0], end="")
            else:
                print(cities[i][0], end=", ")
    print()
