from sqlite3 import Error

from connect import connect_database, database


def create_task(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == "__main__":

    sql_create_students_table = '''
    CREATE TABLE IF NOT EXISTS students(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    name varchar(50),
    group_id integer,
    FOREIGN KEY (group_id) REFERENCES groups (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
    );
'''
    sql_create_groups_table = '''
    CREATE TABLE IF NOT EXISTS groups(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    name varchar(20)
    );
'''
    sql_create_teachers_table = '''
    CREATE TABLE IF NOT EXISTS teachers(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    name varchar(50)
    );
'''
    sql_create_subjects_table = '''
    CREATE TABLE IF NOT EXISTS subjects(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    name varchar(20),
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
       ON DELETE SET NULL
       ON UPDATE CASCADE
    );
'''
    sql_create_scores_table = '''
    CREATE TABLE IF NOT EXISTS scores(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    student_id integer,
    teacher_id integer,
    subject_id integer,
    mark TINYINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students (id)
       ON DELETE SET NULL
       ON UPDATE CASCADE,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
       ON DELETE SET NULL
       ON UPDATE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
       ON DELETE SET NULL
       ON UPDATE CASCADE
    );
'''

    with connect_database(database) as conn:
        if conn is not None:
            create_task(conn, sql_create_students_table)
            create_task(conn, sql_create_groups_table)
            create_task(conn, sql_create_teachers_table)
            create_task(conn, sql_create_subjects_table)
            create_task(conn, sql_create_scores_table)

        else:
            print("Error connection")