import datetime as dt

def Show(Tasks):
    if not Tasks:
        print('No tasks are added.')
    else:
        print('Tasks:')
        for task in Tasks:
            print(f"- {task['Task']} (added at {task['Added at']})")

def Add(Tasks, User):
    if any(task["Task"] == User for task in Tasks):
        print('Task already added.')
    else:
        timestamp = dt.datetime.now().strftime("%H:%M:%S")
        Tasks.append({"Task": User, "Added at": timestamp})
        print(User, 'added to list.')

def Remove(Tasks, User):
    for task in Tasks:
        if task["Task"] == User:
            Tasks.remove(task)
            print(User, 'Removed successfully.')
            return
    print('Task not found.')

def Search(Tasks, User):
    for task in Tasks:
        if task["Task"] == User:
            print(f"Task: {User} | Added at: {task['Added at']}")
            return
    print('Task not found.')

def main():
    Tasks = []
    while True:
        print('\n', 'Welcome to my To-Do List'.center(62, "-"))
        print('\nOptions:')
        print('1: Add task.')
        print('2: Remove task.')
        print('3: Search task.')
        print('4: Show tasks.')
        print('5: Exit.')
        choice = input('What do you want to do (1–5): ').strip()

        try:
            if choice == "1":
                User = input('Enter task: ')
                Add(Tasks, User)
            elif choice == '2':
                User = input('Enter task: ')
                Remove(Tasks, User)
            elif choice == '3':
                User = input('Enter task: ')
                Search(Tasks, User)
            elif choice == '4':
                Show(Tasks)
            elif choice == '5':
                with open('To-Do_list_text.txt', 'w') as tdl:
                    for task in Tasks:
                        tdl.write(f"{task['Task']} (Added at {task['Added at']})\n")
                print('Saving tasks...')
                import time as t
                t.sleep(0.25)
                print('Goodbye!!')
                break
            else:
                print('Invalid choice. Try 1–5.')
        except Exception as E:
            print('An error occurred:', E)

if __name__ == "__main__":
    main()
