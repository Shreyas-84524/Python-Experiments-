#Shreyas Rajendra Shigwan, Roll no. 90, CSE(AIML)
#Exp 2.1 : Task List Manager
tasks = []
while True:
 print("\n--- TASK MANAGER ---")
 print("1. Add Task")
 print("2. Remove Task")
 print("3. Update Task")
 print("4. View Tasks")
 print("5. Sort Tasks")
 print("6. Exit")
 choice = input("Enter your choice (1-6): ")
# Add task
 if choice == "1":
   task = input("Enter a new task: ")
   tasks.append(task)
   print("Task added successfully!")
#Remove task
 elif choice == "2":
  if not tasks:
   print("No tasks to remove.")
  else:
   task = input("Enter the task to remove: ")
   if task in tasks:
     tasks.remove(task)
     print("Task removed successfully!")
   else:
     print("Task not found.")
#Update task
 elif choice == "3":
    if not tasks:
       print("No tasks to update.")
    else:
      old_task = input("Enter the task to update: ")
      if old_task in tasks:
           new_task =  input("Enter the new task: ")
           index = tasks.index(old_task)
           tasks[index] = new_task
           print("Task updated successfully!")
      else:
        print("Task not found.")
# View tasks (using tuple)
 elif choice == "4":
   if not tasks:
     print("No tasks available.")
   else:
    print("\nYour Tasks:")
    task_tuple = tuple(tasks)
    for i, task in enumerate (task_tuple, start=1):
      print(f"{i}. {task}")
#Sort tasks
 elif choice == "5":
   if not tasks:
    print("No tasks to sort.")
   else:
    tasks.sort()
    print("Tasks sorted alphabetically!")
# Exit
 elif choice == "6":
  print("Exiting Task Manager. Goodbye!")
  break
 else:
   print("Invalid choice. Please try again.")