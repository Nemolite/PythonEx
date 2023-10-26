import sqlite3;
from prettytable import PrettyTable
connnectToDB = sqlite3.connect("mybasa.db")
cursor = connnectToDB.cursor()

# cursor.execute("""CREATE TABLE users
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 First_Name TEXT,
#                 Last_Name TEXT,
#                 Work_exp REAL)
#             """)
#
# cursor.execute("INSERT INTO users (First_Name, Last_Name, Work_exp) VALUES ('James', 'Quas',2.5)")
# cursor.execute("INSERT INTO users (First_Name, Last_Name, Work_exp) VALUES ('Mihail', 'Vecs',5)")
# cursor.execute("INSERT INTO users (First_Name, Last_Name, Work_exp) VALUES ('Patrik', 'Exsort',3.5)")
# cursor.execute("INSERT INTO users (First_Name, Last_Name, Work_exp) VALUES ('Lary', 'Star',3)")
#
# connnectToDB.commit()

cursor.execute("SELECT * FROM users")
newTable = PrettyTable(["ID", "First_Name", "Last_Name", "Work_exp"])
for user in cursor.fetchall():
    newTable.add_row([user[0], user[1], user[2], str(user[3]) + ' years'])

print(newTable)
