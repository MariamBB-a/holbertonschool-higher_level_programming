#!/usr/bin/python3
"""Lists all states starting with 'N' (case-insensitive for the filter)"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL login info from arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )

    cursor = db.cursor()
    # Use a case-insensitive LIKE for lowercase 'n'
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, ('n%',))  # lowercase 'n'

    # Print results
    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
