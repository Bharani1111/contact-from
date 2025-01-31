import sqlite3

conn = sqlite3.connect('contact.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contact (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
