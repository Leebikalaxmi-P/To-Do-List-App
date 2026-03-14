tasks =[]
def add_task():
    task=input("Enter Task :")
    tasks.append(task)
    print("Task added")
    m=input("Would you like to add more ?(Y/N) :")
    if m== 'Y':
        add_task()

        
def remove_task():
    task = input("Enter Task to remove : ")
    if task in tasks:
        tasks.remove(task)
        print("Task Removed")
    else:
        print("Task Not Found !")
def display_tasks():
    print("\nTo-Do-List :")
    for ind,task in enumerate(tasks,start=1):
        print(f"_______________________________\n{ind}. |{task}")
while True:
    print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit")
    ch = input("Enter Choice :")
    if ch=='1':
        add_task()
    elif ch =='2':
        remove_task()
    elif ch =='3':
        display_tasks()
    elif ch =='4':
        break
    else:
        print("Invalid Choice ! Try Again ")
