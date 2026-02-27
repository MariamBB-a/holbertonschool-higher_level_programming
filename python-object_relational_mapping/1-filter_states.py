#!/usr/bin/python3
"""Lists all states starting with lowercase 'n' from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    # Case-sensitive search for lowercase 'n'
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'n%' ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
