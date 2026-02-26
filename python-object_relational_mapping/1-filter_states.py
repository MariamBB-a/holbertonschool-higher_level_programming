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

    # Correct placeholder usage with %s
    query = "SELECT * FROM states WHERE BINARY name LIKE %s ORDER BY id ASC"
    cursor.execute(query, ("n%",))

    for state in cursor:
        print(state)

    cursor.close()
    db.close()
