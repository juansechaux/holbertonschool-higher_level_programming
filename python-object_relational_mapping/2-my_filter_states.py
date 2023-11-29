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

    cursor.execute("SELECT * FROM states")
    for states in cursor.fetchall():
        if states[1] == state_name:
            print('({}, {})'.format(states[0], states[1]))

    cursor.close()
    db.close()
