from views import db
from models import Task
from datetime import date

# create the database and the db table
db.create_all()

# insert data
db.session.add(Task("finish this tutorial", date(2020, 9, 22), 10, 1))
db.session.add(Task("Finish Real Python", date(2020, 9, 30), 10, 1))
db.session.commit()



# using Sqlite3

# import sqlite3
# from _config import DATABASE_PATH


# with sqlite3.connect(DATABASE_PATH) as connection:
#
#         c = connection.cursor()
#
#         # Create the table
#         c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL, due_date TEXT NOT NULL,
#         priority INTEGER NOT NULL, status INTEGER NOT NULL)""")
#
#         # insert data into the table
#         c.execute(
#             'INSERT INTO tasks(name, due_date, priority, status)'
#                   'VALUES("Finish this tutorial", "03/25/2015", 10, 1)'
#         )
#
#         c.execute(
#             'INSERT INTO tasks (name, due_date, priority, status)'
#             'VALUES ("finis RP course 2", "09/20/2020", 10, 1)'
#         )
