#!/usr/bin/python3
"""Lists all states starting with 'N' (case-insensitive for the filter)"""

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

    # Filter states starting with 'N' (uppercase) only, keeping original case
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, ("N%",))

    for state in cursor:
        print(state)

    cursor.close()
    db.close()
