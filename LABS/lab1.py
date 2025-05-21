import sqlite3


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('../database.db')
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
        if not name:
            print("Error: Task name cannot be empty.")
            return

        if self.find_task(name):
            print(f"Error: Task '{name}' already exists.")
            return

        try:
            priority = int(input('Enter priority: '))
            if priority < 1:
                print("Error: Priority must be at least 1.")
                return
        except ValueError:
            print("Error: Priority must be a number.")
            return

        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()
        print(f"Task '{name}' added successfully.")

    def find_task(self, name):
        self.c.execute('SELECT * FROM tasks WHERE name = ?', (name,))
        task = self.c.fetchone()
        return task

    def view_tasks(self):
        self.c.execute('SELECT * FROM tasks')
        tasks = self.c.fetchall()
        for task in tasks:
            print(task)

    def show_tasks(self):
        self.c.execute('SELECT * FROM tasks')
        tasks = self.c.fetchall()
        if not tasks:
            print("No tasks found.")
            return
        print("ID | Task Name | Priority")
        print("-" * 30)
        for task in tasks:
            print(f"{task[0]} | {task[1]} | {task[2]}")

app = Todo()
while True:
    choice = input('What do you want to do?\n'
                   '1. View tasks (raw format)\n'
                   '2. Show tasks (formatted)\n'
                   '3. Add task\n'
                   '4. Exit\n'
                   'Enter your choice: ')
    if choice == '1':
        app.view_tasks()
    elif choice == '2':
        app.show_tasks()
    elif choice == '3':
        print('Adding task...')
        app.add_task()
    elif choice == '4':
        print('Exiting...')
        break
    else:
        print('Invalid choice. Please try again.')
