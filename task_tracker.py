import json
import datetime
file_name = "data.json"
try:
    with open(file_name, "r") as f:
        task_dict = json.load(f)
    for i in task_dict:
        max_id = 1
        if task_dict[i]['id'] > max_id:
            max_id = task_dict[i]['id']
    current_id = max_id + 1
except:
    with open(file_name, "w") as f:
        f.write('{}')
    current_id = 1



def new_task(task_name, id_num):
    task_dict[task_name] = {}
    task_dict[task_name]['id'] = id_num
    task_dict[task_name]['status'] = 'Todo'
    task_dict[task_name]['description'] = 'None'
    task_dict[task_name]['createdAt'] = str(datetime.datetime.now())
    print(f"Perfect! The task '{task_name}' was created with the id of {task_dict[task_name]['id']} at {task_dict[task_name]['createdAt']}")

def edit_task(task_name):
    new_name = input("Please enter the updated name: ")
    task_dict[new_name] = task_dict.pop(task_name)
    print(task_dict)

def verify_id(task_id):
    if task_id in [obj[x] for i, obj in task_dict.items() for x in obj]: #Checking if id is real
        for name, obj in task_dict.items():
            for x in obj:
                if obj[x] == task_id:
                    task_name = name
                    return task_name, task_id
    else:
        raise RuntimeError
    
def delete_task(task_id, task_name):
    print(f"You have chosen to delete the task '{task_name}', with the id of {task_id}")
    if input("Are you sure you want to delete? (y) Enter anything else to cancel") == 'y':
        del task_dict[task_name]
        print("Task deleted!")
    else:
        print()

def menu_print():
    print(f"{'These are the following commands to put before the task ID:':^80}")
    print(f"{'-'*80}")
    print(f"{'add [name]':^80}")
    print(f"{'add with the name of the task creates a new task':^80}")
    print(f"{'-'*80}")
    print(f"{'edit [id]':^80}")
    print(f"{'edit the name of the task':^80}")
    print(f"{'-'*80}")
    print(f"{'delete [id]':^80}")
    print(f"{'delete task from the list':^80}")
    print(f"{'-'*80}")
    print(f"{'menu':^80}")
    print(f"{'prints out this menu of options':^80}")
    print(f"{'-'*80}")
    print(f"{'status [id]':^80}")
    print(f"{'allows you to edit the status of a task (default is Todo)':^80}")
    print(f"{'-'*80}")
    print(f"{'list [status]':^80}")
    print(f"{'allows you to see the list of tasks':^80}")
    print(f"{'the [status] sort is optional (can be left blank for all)':^80}")
    print(f"{'-'*80}")
    print(f"{'description [id]':^80}")
    print(f"{'allows you to give a description of the task, left None by default':^80}")
    print(f"{'-'*80}")
    print(f"{'exit':^80}")
    print(f"{'Saves your edits to a .json file and quits':^80}")
    print(f"{'-'*80}")



def update_status(task_name):
    
    print(f"{task_dict[task_name]['status']} is the current status")
    print("These are the following options to update the status:")
    print(f"{'1. Todo':^30}")
    print(f"{'2. In Progress':^30}")
    print(f"{'2. Done':^30}")
    while True:
        try:
            status_select = int(input("Please enter the corresponding number"))
            if status_select == 1:
                task_dict[task_name]['status'] = "Todo"
                break
            elif status_select == 2:
                task_dict[task_name]['status'] = "In Progress"
                break
            elif status_select == 3:
                task_dict[task_name]['status'] = "Done"
                break
            else:
                print("Please enter a valid number")
        except:
            print("Sorry invalid input")

def list_print(status=""):
    if len(task_dict.keys()) > 0:
        for i in task_dict:
            if (task_dict[i]['status'].lower() == status) or (status == ""):
                print(f"{f'Task Name - {i}':^30}")
                for x in task_dict[i].keys():
                    print(f"{f'{x} - {task_dict[i][x]}':^80}")
                print()
    else:
        print("Sorry, you haven't entered any tasks yet")

def update_description(task_name):
    task_dict[task_name]['description'] = input(f"Please enter the updated description for your task named '{task_name}' here: ")


if __name__ == "__main__":
    print(f"{'Hello!':^80}")
    print(f"{'This is my Task Tracker app!':^80}")
    print()
    menu_print()
    while True:
        user_select = input("Enter your choice: ")
        print()
        if user_select[:3] == "add":
            new_task(user_select[4:], current_id)
            current_id += 1
        elif user_select[:4] == "edit":
            try:
                task_to_edit, task_id_to_edit = verify_id(int(user_select[5]))
                print(f"You have chosen to edit the task '{task_to_edit}', with the id of {task_id_to_edit}")
                edit_task(task_to_edit)
            except:
                print(f"Sorry, the task id {(user_select[5])} was not found.")
        elif user_select[:6] == 'delete':
            try:
                task_to_delete, task_id_to_delete = verify_id(int(user_select[7]))
                delete_task(task_id_to_delete, task_to_delete)
            except:
                print(f"Sorry, the task id {(user_select[7])} was not found.")
        elif user_select[:4] == "menu":
            menu_print()
        elif user_select[:6] == "status":
            try:
                task_name_for_status, task_id_for_status = verify_id(int(user_select[7]))
                update_status(task_name_for_status)
            except:
                print(f"Sorry, the task id {(user_select[7])} was not found.")
        elif user_select[:4] == "list":
            if user_select[4:].strip() == "":
                list_print()
            else:
                list_print(user_select[4:].strip().lower())
        elif user_select[:11] == "description":
            try:
                task_description_name, task_id_description = verify_id(int(user_select[12]))
                update_description(task_description_name)
            except:
                print(f"Sorry, the task id {(user_select[12])} was not found.")
        elif user_select[:4] == "exit":
            print()
            print("Thanks for using the app")
            print(f"Your data has been saved to: {file_name}")
            with open(file_name, "w") as f:
                json.dump(task_dict, f, indent=4)
            break
        else:
            print("Sorry that is not one of the choices.")
            
    

            

        
    