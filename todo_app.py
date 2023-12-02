def show_menu():
    print("****/MENu/****")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Completed")
    print("Quit")

def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task ["{task}"] added")

def view_tasks(todo_list):
    if not todo_list:
        print("its empty are you autistic")
    else:
        print("\n Current Tasks")

        for index, task in enumerate(todo_list, start=1):
            print(f"{index}, {task}")

def mark_completed(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        completed_task = todo_list.pop(task_index - 1)
        print(f"Task ["{completed_task}"] marked complete")
    else:
        print("wrong task bud you should kill yourself")