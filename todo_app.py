import random, time

def show_menu():
    print("\n\n****/MENu/****")
    time.sleep(0.1)
    print("1. Add Task")
    time.sleep(0.1)
    print("2. View Task")
    time.sleep(0.1)
    print("3. Mark Task as Completed")
    time.sleep(0.1)
    print("4. Quit")

def add_task(todo_list, task):
    todo_list.append(task)
    time.sleep(0.1)
    print(f"Task '{task}' added")

def view_tasks(todo_list):
    if not todo_list:
        time.sleep(0.5)
        print("its empty are you autistic")
    else:
        time.sleep(0.1)
        print("\n Current Tasks:")

        for index, task in enumerate(todo_list, start=1):
            print(f"{index}, {task}")

def mark_completed(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        time.sleep(0.1)
        completed_task = todo_list.pop(task_index - 1)
        print(f"Task '{completed_task}' marked complete")
    else:
        time.sleep(0.1)
        print("wrong task bud you should kill yourself")

def todo_list_app():
    todo_list = []
    while True:
        time.sleep(0.1)
        show_menu()
        choice = input("enter the number of choice(1-4): ")
        print("\n\n")
        if choice == "1":
            time.sleep(0.1)
            print("adding task...")
            time.sleep(0.15)
            task = input("enter the task: ")
            add_task(todo_list, task)
        elif choice == "2":
            view_tasks(todo_list)
        elif choice == "3":
            time.sleep(0.1)
            print("marking tasks...")
            time.sleep(0.1)
            task_index = int(input("enter the number of the task you want to mark complete: "))
            mark_completed(todo_list, task_index)
        elif choice == "4":
            print("quitting...")
            time.sleep(0.1)
            print("what the f̸̑̈ͅu̸̮̝͂̊c̶̗̏̀k̵͕̃̽ is wrong with you")
            time.sleep(0.5)
            print("are you mental")
            time.sleep(0.5)
            print("how dare you quit me you should kill yourself")
            time.sleep(0.5)
            while True:
                time.sleep(0.1)
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