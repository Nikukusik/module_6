from sqlite3 import Error

from connect import connect_database, database
from faker import Faker
import random
faker = Faker()


def insert_into(conn, insert, arg):
    try:
        c = conn.cursor()
        c.execute(insert, arg)
        conn.commit()
    except Error as e:
        print(e)

if __name__ == "__main__":

    insert_students = '''
    INSERT INTO students(name,group_id) VALUES(?,?);
'''
    insert_groups = '''
    INSERT INTO groups(name) VALUES(?);
'''
    insert_teachers = '''
    INSERT INTO teachers(name) VALUES(?);
'''
    insert_subjects = '''
    INSERT INTO subjects(name, teacher_id) VALUES(?,?);
'''
    insert_scores = '''
    INSERT INTO scores(student_id, teacher_id, subject_id, mark) VALUES(?,?,?,?);
'''
    with connect_database(database) as conn:
        if conn is not None:

            for _ in range(40):
                arg_students = (faker.name(), random.randint(1,3))
                insert_into(conn, insert_students, arg_students)

            for i in range(3):
                arg_groups = (f'group_{i}', ) # maybe forget coma
                insert_into(conn, insert_groups, arg_groups)

            for i in range(4):
                arg_teachers = (faker.name(), ) # maybe forget coma
                insert_into(conn, insert_teachers, arg_teachers)

            for i in range(6):
                arg_subjects = (f'subject_{i}', random.randint(1,4))
                insert_into(conn, insert_subjects, arg_subjects)
                
            for i in range(200):
                arg_scores = (random.randint(1,40), random.randint(1,4), random.randint(1,6), random.randint(1,12))
                insert_into(conn, insert_scores, arg_scores)
                
        else:
            print("Error connection")