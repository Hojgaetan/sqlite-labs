import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL)
    ''')
# Insert a row of data
c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', ('My first task', 1))
# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it
conn.close()