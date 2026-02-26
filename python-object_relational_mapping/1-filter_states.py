#!/usr/bin/python3
"""Lists all states with a name starting with n"""

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

    cursor = db.cursor()

    # Parameterized query to prevent SQL injection
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC", ("n%",))

    # Stream results row by row
    for state in cursor:
        print(state)

    cursor.close()
    db.close()
