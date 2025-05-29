import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('users.db')

# Create a cursor
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Insert a sample user
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ('admin', '1234'))

# Commit and close
conn.commit()
conn.close()
print("Database created with sample user: admin / 1234")
