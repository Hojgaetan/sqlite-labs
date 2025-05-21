import sqlite3


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks
                          (
                              id
                              INTEGER
                              PRIMARY
                              KEY,
                              name
                              TEXT
                              NOT
                              NULL,
                              priority
                              INTEGER
                              NOT
                              NULL
                          );''')

    def add_task(self):
        name = input('Enter task name: ')
        priority = int(input('Enter priority: '))

        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()

    def view_tasks(self):
        self.c.execute('SELECT * FROM tasks')
        tasks = self.c.fetchall()
        for task in tasks:
            print(task)

app = Todo()
while True:
    choice = input('What do you want to do?\n'
                   '1. View tasks\n'
                   '2. Add task\n'
                   '3. Exit\n'
                   'Enter your choice: ')
    if choice == '1':
        app.view_tasks()
    if choice == '2':
        print('Adding task...')
        app.add_task()
    if choice == '3':
        print('Exiting...')
        break
