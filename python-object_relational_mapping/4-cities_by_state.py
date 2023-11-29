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

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name,states.name FROM cities JOIN states ON cities.state_id = states.id")
    for cities in cursor.fetchall():
        print(cities)

    cursor.close()
    db.close()
