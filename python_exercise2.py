#Task Manager Program
list=[]

print("""Enter your choice:
        1-To Add a new btask
        2-To add a specific task 
        3-Remove the task
        4-Clear the task
        5-Remove a specific task
        6-copy the task
        7-sort the task
        8-Reverse the task order
        8- Exit the task manager
        """)
while(True):

    ch=int(input("Enter the choice:\n"))
    print("Your choice is ",ch)
    if(ch>0 and ch<=8):
        if ch==1:
            p=int(input("Enter the task to be added:"))
            list.append(p)
            print("The task manager after adding the task is: ",list)
        elif ch==2:
            q=int(input("Enter the index of the task to be added:"))
            l=int(input("Enter the task"))
            list.insert(q,l)
            print("The task manager after adding the specific task is: ",list)
        elif ch==3:
            i=int(input("Enter the task to be removed:"))
            list.remove(i)
            print("The task manager after removing the task is:",list)
        elif ch==4:
            list.clear()
            print("Task manager list is cleared.",list)
        elif ch==5:
            m=int(input("Enter the index of task to be removed:"))
            list.pop(m)
            print("The list after popping the element is:",list)
        elif ch==6:
            newlist=list.copy()
            print("The copied list is:",newlist)
        elif ch==7 :
            list.sort()
            print("Sorted list is",list)
        else :
            list.reverse()
            print("Reversed list is",list)
            
    else:
        break
