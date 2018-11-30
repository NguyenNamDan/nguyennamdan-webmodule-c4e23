import mlab
from todo import Todo

mlab.connect() 

string = '''
1. New todo
2. View All Todos
3. Mark a Todo Completed
4. Delete a todo
5. Exit
Enter your Command? 
'''
user = int(input(string))
if user == 1:
    n = input("Name: ")
    d = input("Description: ")
    t = Todo(name= n, description= d)
    t.save()
elif user == 2:
    todo_list = Todo.objects()
    if len(todo_list) != 0:
        for i in todo_list:
            print(i.name, i.description, sep= '\n')
    else:
        print("Empty")
elif user == 3:
    index = int(input("Which one? "))
    print("Updated")
    records = Todo.objects()
    for r in records:
        if r == index:
            r.update(set__available= True) 
elif user == 4:
    index = int(input("Which one? "))
    print("Deleted")
    m = Todo.objects()[index-1] #find index 
    m.delete() 
else:
    pass 

    