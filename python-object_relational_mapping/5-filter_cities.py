#!/usr/bin/python3
"""A script to list states from database hbtn_0e_0_usa."""
import sys
import MySQLdb

if __name__ == "__main__":
    """Get arguments  from command-line"""
    argumentos = sys.argv

    username = argumentos[1]
    password = argumentos[2]
    database = argumentos[3]
    state_name = argumentos[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities "
                   "JOIN states ON cities.state_id = states.id "
                   "WHERE states.name = %s", (state_name,))
    num_rows = cursor.rowcount
    count = 1
    for cities in cursor.fetchall():
        if count < num_rows:
            print("{}, ".format(cities[0]), end="")
        else:
            print("{}".format(cities[0]))
        count += 1

    cursor.close()
    db.close()
