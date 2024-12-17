#14.To Do App Programme

def task():
    tasks = [] 
    print("-----WELCOME TO THE TASK MANAGEMENT APP-----")

    total_task = int(input("Enter How Many Task You Want To Add:- "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter Task {i} :- ")
        tasks.append(task_name)

    print(f"Today's Tasks Are\n{tasks}")

    while True:
        operation = int(input("Enter\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop"))
        if operation == 1:
            add = input("Enter Task You Want To Add:- ")
            tasks.append(add)
            print(f"Task {add} Has Been Successfully Added...")
        
        elif operation == 2:
            Updated_list = input("Enter The Task Name You Want To Update:- ")
            if Updated_list in tasks:
                up = input("Enter New Task:- ")
                ind = tasks.index(Updated_list)
                tasks[ind] = up
                print(f"Updated Task {up}")

        elif operation == 3:
            del_val = input("Which Task You Want To Delete:- ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} Has Been Deleted...")
        elif operation == 4:
            print(f"Total tasks:- {tasks} ")
        
        elif operation == 5:
            print(f"Closing The Program...")
            break

        else:
            print("Invalid Input")

task()