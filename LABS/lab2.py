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

    def change_priority(self):
        self.show_tasks()
        try:
            task_id = int(input('Enter task ID: '))
            self.c.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
            task = self.c.fetchone()
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return

            new_priority = int(input('Enter new priority: '))
            if new_priority < 1:
                print("Error: Priority must be at least 1.")
                return

            self.c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (new_priority, task_id))
            self.conn.commit()
            print(f"Priority of task '{task[1]}' updated successfully.")
        except ValueError:
            print("Error: ID and priority must be numbers.")

    def delete_task(self):
        self.show_tasks()
        try:
            task_id = int(input('Enter task ID: '))
            self.c.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
            task = self.c.fetchone()
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return

            self.c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
            self.conn.commit()
            print(f"Task '{task[1]}' deleted successfully.")
        except ValueError:
            print("Error: ID must be a number.")

app = Todo()
while True:
    choice = input('What do you want to do?\n'
                   '1. Show Tasks\n'
                   '2. Add Task\n'
                   '3. Change Priority\n'
                   '4. Delete Task\n'
                   '5. Exit\n'
                   'Enter your choice: ')
    if choice == '1':
        app.show_tasks()
    elif choice == '2':
        print('Adding task...')
        app.add_task()
    elif choice == '3':
        print('Changing priority...')
        app.change_priority()
    elif choice == '4':
        print('Deleting task...')
        app.delete_task()
    elif choice == '5':
        print('Exiting...')
        break
    else:
        print('Invalid choice. Please try again.')
