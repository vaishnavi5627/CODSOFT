import os

def show_tasks(tasks):
    if not tasks:
        print("no tasks found")
    else:
        for i, task in enumerate(tasks,1):
            print(f"{i}. {task}")
def add_task(tasks, new_tasks):
    tasks.append(new_tasks)    
    print("task added")

def update_task(tasks, index, update_task):
    if 1 <= index <=len(tasks):
        tasks[index -1] =update_task
        print("task updated")
    else:
        print("invalid task index")  

def delete_task(tasks, index):
    if 1 <= index <=len(tasks):
        delete_task = tasks.pop(index-1)
        print(f"Task '{delete_task} deleted")    
    else:
        print("invalid task")


def save_tasks(file_path, tasks):
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")



def load_tasks(file_path):
    task = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            task= file.read().splitlines()
    return task        


def main():
    file_path = "todo_list.txt"
    tasks = load_tasks(file_path)
    while True:
        print('---------------------------')
        print("1. Show Tasks")
        print("2. Add Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save and Exit ")
        print('----------------------------')
        choice = input(" Enter your choice:")
        if choice=="1":
            show_tasks(tasks)
        elif choice=="2":
            new_tasks = input(" Enter the new task: ")
            add_task(tasks, new_tasks)
        elif choice=="3":
            index = int(input(" Enter task index to update: "))
            update_task = input(" Enter the  updated task:")
        elif choice=="4":
            index = int(input(" Enter task index to delete:")) 
            delete_task(tasks, index)
        elif choice=="5":
            save_tasks(file_path, tasks)
            print("Task saved...& Exiting")
            break
        else:
            print("Invalid choice")

                   

if __name__ == "__main__":
    main()