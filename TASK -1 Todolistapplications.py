#to do list application in python using command line arguments(CLI)
#list to store apllications
tasks=[]
# To show all details
def show_details():
    if not tasks:
        print("\n No tasks in your list.")
    else:
        print("\nyour To-Do List.")
        for i,task in enumerate(tasks, start=1):
            print(f"{i}.{task}")
#function to add new tasks
def add_task():
    task=input("Enter the task to add: ")
    tasks.append(task)
    print("task is added successfully")
#function to update a task
def update_task():
    show_details()
    if tasks:
        try:
            num=int(input("Enter a number to update your task: "))
            if 1<= num <=len(tasks):
                new_task=input("Enter the new task to update: ")
                tasks[num -1]=new_task
                print("Task updated successfully!")
            else:
                print("Invald task number given.")
        except ValueError:
            print("Please enter a valid number.")
#function to delete a task
def delete_task():
    show_details()
    if tasks:
        try:
            num = int(input("Enter a task number: "))
            if 1<=num<=len(tasks):
                tasks.pop(num -1)
                print("Task deleted successfully!")
            else:
                print("Invalis task number given")
        except ValueError:
            print("Please enter a valid number")
#Main menu
def main():
    while True:
        print("\n  TO - DO - LIST MENU ")
        print("1.Show details")
        print("2.Add task")
        print("3.Update task") 
        print("4.Delete task")
        print("5.Exit")

        choose=input("Enter a number(1-5): ")
        
        if choose == '1':
            show_details()
        elif choose == '2':
            add_task()
        elif choose == '3':
            update_task()
        elif choose == '4':
            delete_task()
        elif choose == '5':
            print("Thanks for using TO DO LIST. Goodbye")
            break
        else:
            print("invalid number choosen. Please select from only(1-5)")

main()
