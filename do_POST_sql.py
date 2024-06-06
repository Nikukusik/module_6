from sqlite3 import Error

from connect import connect_database, database

import sys




def do_post_sql(conn, sql):
    rows = None
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        rows = c.fetchall()
    except Error as e:
        print(e)
    return rows


if __name__ == "__main__":
    arg = sys.argv[1]
    with connect_database(database) as conn:
        if conn is not None:
            with open(arg, 'r', encoding = 'utf-8') as file:
                sql = file.read()
                print(do_post_sql(conn, sql))
        else:
            print("Error connection")
            