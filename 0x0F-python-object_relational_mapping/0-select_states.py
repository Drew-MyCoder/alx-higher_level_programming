#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_usa sorted in ascending order"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    con = MySQLdb.connect(host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    curs = con.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = curs.fetchall()
    for row in query_rows:
        print(row)
    curs.close()
    con.close()
