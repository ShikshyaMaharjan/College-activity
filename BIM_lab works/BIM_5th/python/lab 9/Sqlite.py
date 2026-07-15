import sqlite3
conn = sqlite3.connect("student.db")

cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')

cursor.execute("DELETE FROM students")

students_data = [
    (1, "Ram", 19),
    (2, "Sita", 23),
    (3, "Liam", 26),
    (4, "Sudi", 23),
    (5, "Bidhya", 30),
    (6, "Luniva", 24),
    (7, "Kale", 28),
    (8, "Nora", 22),
    (9, "Fatey", 23),
    (10, "Aarya", 20)
]

cursor.executemany("INSERT INTO students VALUES (?, ?, ?)", students_data)
# Save changes
conn.commit()

# display data
cursor.execute("SELECT * FROM students")
# cursor.execute("DELETE FROM students")
rows = cursor.fetchall()

print("Student Records:")
for row in rows:
    print(row)

conn.close()