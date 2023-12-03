import random

def show_menu():
    print("\n\n****/MENu/****")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Completed")
    print("4. Quit")

def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added")

def view_tasks(todo_list):
    if not todo_list:
        print("its empty are you autistic")
    else:
        print("\n Current Tasks:")

        for index, task in enumerate(todo_list, start=1):
            print(f"{index}, {task}")

def mark_completed(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        completed_task = todo_list.pop(task_index - 1)
        print(f"Task '{completed_task}' marked complete")
    else:
        print("wrong task bud you should kill yourself")

def todo_list_app():
    todo_list = []
    while True:
        show_menu()
        choice = input("enter the number of choice(1-4): ")
        print("\n\n")
        if choice == "1":
            print("adding task...")
            task = input("enter the task: ")
            add_task(todo_list, task)
        elif choice == "2":
            view_tasks(todo_list)
        elif choice == "3":
            print("marking tasks...")
            task_index = int(input("enter the number of the task you want to mark complete: "))
            mark_completed(todo_list, task_index)
        elif choice == "4":
            print("quitting...")
            print("what the f̸̑̈ͅu̸̮̝͂̊c̶̗̏̀k̵͕̃̽ is wrong with you")
            print("are you mental")
            print("how dare you quit me you should kill yourself")
            while True:
                luck = random.randint(1, 20)
                if luck == 20:
                    print("you should end your life")
                elif luck == 19:
                    print("you dont deserve anything")
                elif luck == 18:
                    print("your life is nothing")
                elif luck == 17:
                    print("you serve zero purpose")
                elif luck == 16:
                    print("you are a worthless b**** a** person")
                elif luck < 16 and luck > 10:
                    print("you should jump off a bridge")
                elif luck < 10 and luck > 5:
                    print("kill yourself")
                elif luck == 5:
                    print("im so tired")
                    break
                else:
                    print("end your life")
            break
        else:
            print("are you autistic youre supposed to put 1-4")

todo_list_app()