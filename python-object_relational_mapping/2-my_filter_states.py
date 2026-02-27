#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa
where name matches the argument (using format)."""


import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=passwd, db=db_name)

    # Create cursor
    cur = db.cursor()

    # Build query using format (assignment requirement)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    # Execute query
    cur.execute(query)

    # Fetch and print results
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
