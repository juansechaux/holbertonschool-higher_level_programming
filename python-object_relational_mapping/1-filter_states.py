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

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for states in cursor.fetchall():
        if states[1][0] == "N":
            print(states)

    cursor.close()
    db.close()
