def list():
    task = []
    print("1:add list")
    print("2:remove list")
    print("3:show list")
    int = input("enter a task: ")   
    while True:
        if int == "1":
            item = input("enter a task to add: ")
            task.append(item)
            print("list appended sucessfully")  
            int = input("enter a task: ")   
        elif int == "2":
            item = input("enter a task to remove: ")
            if item in task:
             task.remove(item)
             print("list removed sucessfully") 
            else:
                print("task not found")
            int = input("enter a task: ")    
        
        elif int == "3":
            print(task)
            int = input("enter a task: ") 
              
        else:
            print("invalid input")
            exit()
            
t1 = list()
list()