#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument, and prevents SQL injections and prints in asc order
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    con = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])
    curs = con.cursor()
    curs.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                (argv[4],))
    query_rows = curs.fetchall()
    for row in query_rows:
        print(row)
    curs.close()
    con.close()
