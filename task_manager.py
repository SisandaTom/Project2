import datetime

users = []
passwords = []
user_name  = ""
total_users = []
total_tasks = []
details = False

# open both user and task files
with open("user.txt", 'r+') as f:
    for line in f:
        total_users.append(line.split())
        
#validating the user username and password by allowing the
#user to enter their username and password
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for i in range(len(total_users)):
            if username and password in total_users[i]:
                details = True

        if details == True:
            break
        else:
            print("Enter a valid username/ password.")


while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':
        #if user chooses r then they may be asked to enter new username,
        #new password, confirm password 
        if username == "admin":
            new_username = input("Enter the new user's username: ")
            new_password = input("Enter the new user's password: ")
            new_password_confirm = input("Confirm the new user's password: ")

            #if the password matches, the te new password is stored to the file
            if new_password == new_password_confirm:
                user_file = open("user.txt", "a")
                user_file.write("\n" + new_username + ", " + new_password)
                user_file.close()
                print("The new user has been registered.")
            else:print("The new password and confirmed password do not match, please try again.")

    #if menu a is chosen user iformation about the task is required 
    elif menu == 'a':
        #user inputs title, description, due date, username of the person,
        #due date of the task and is stored in the variables below
        username_assigned = input("Enter the username of the person the task is assigned to: ")
        task_title = input("Enter the title of the task: ")
        task_description = input("Enter the description of the task: ")
        task_due_date = input("Enter the due date of the task (dd/mm/yyyy): ")

        #open file task.txt to write the data above
        task_file = open("tasks.txt", "a")
        task_file.write("\n" + username_assigned + ", " + task_title + ", " + task_description + ", " + str(datetime.date.today()) + ", " + task_due_date + ", No")
        task_file.close()
        print("The task has been added.")

    elif menu == 'va':
         file = open("tasks.txt", "r")
         for line in file:

           # if the line is not empty
           if line != "\n":

               # split the line into a list
               line = line.split(",")

               # remove the \n character
               line[-1] = line[-1].strip()

               # print the details of each task
               print("Task:\t\t\t\t" + line[1])

               print("Assigned to:\t\t\t" + line[0])

               print("Date assigned:\t\t\t" + line[3])

               print("Due Date:\t\t\t" + line[4])

               print("Task complete?\t\t\t" + line[5])

               print("Task Description:\n" + line[2])

               print("\n------------------------------------------------------------------------------\n")

    elif menu == 'vm':
        file = open("tasks.txt", "r")
    # go through each line in the tasks.txt file
        for line in file:

           #if the line is not empty
           if line != "\n":

               # split the line into a list
               line = line.split(",")

               # remove the \n character
               line[-1] = line[-1].strip()

               # if the username on the current line is the same as the username that is logged in
               if line[0] == username:

                   # print the details of each task
                 print("\n------------------------------------------------------------------------------\n")

                 print("Task:\t\t\t\t" + line[1])

                 print("Assigned to:\t\t\t " + " " + line[0])

                 print("Date assigned:\t\t\t" + line[3])

                 print("Due Date:\t\t\t" + line[4])

                 print("Task complete?\t\t\t " +" "+  line[5])

                 print("Task Description:\n" + line[2] + "\n")

                 print("\n------------------------------------------------------------------------------\n")

        file.close()

    elif menu == "s":
        #if username is admin, allow the program to be executed if not a message is displayed
        if username != "admin":
            print("Only admins can access statistics.")
        elif username == "admin":
            user_count = "user.txt"
            counting = 0
            with open('user.txt', 'r') as f:
                for line in f:
                    counting += 1
            print("Total users are: ", counting)

# create function to count the number of tasks in the file
            task_count = "tasks.txt"
            task_counting = 0
            with open('tasks.txt', 'r') as g:
                for line in g:
                    task_counting += 1
            print("Total tasks are: ", task_counting)

    #print exit when the user enter e
    elif menu == 'e':
        print("Goodbye!!!")
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
