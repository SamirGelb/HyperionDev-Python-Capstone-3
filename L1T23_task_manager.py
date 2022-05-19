import datetime

# I am defining a function called reg_user
# This will be called later on in the code
def reg_user():
    with open("user.txt", "a+") as f:
    # Next I ask the admin to enter a username.
        new_username = input("Please enter a username: ").lower()
        print("")
        # Using a while loop
        # I check if the username entered already exists in user.txt
        # If the username exists, the admin is asked to try again
        while new_username in user_dict:
            print("Sorry, that user already exists. Please try again")
            return reg_user()
        # If the username is unique, 
        # the admin may proceed to register a password for the username.
        new_password = input("Please enter a password: ")
        password_confirmation = input("Please enter your password again: ")
        
    # If the password and the confirmed password match
    # The program writes the username and password to the user.txt file on a new line.
        if new_password == password_confirmation:
            f.write("\n")
            f.write(f"{new_username}, {new_password}")
            print("New User Registered.")
            print("")
    
    while new_password != password_confirmation:
        # If the passwords do not match, the admin is asked to re-enter them until they do match
        # Once they match, the program writes the new information to the file
        print("Your passwords do not match. Please try again")
        new_password = input("Please enter a password: ")
        password_confirmation = input("Please enter your password again: ")
        if new_password == password_confirmation:
            f.write("\n")
            f.write(f"{new_username}, {new_password}")
            print("New User Registered.")
            print("")

# I am defining a function called add_task
# This will be called later on in the code
def add_task():
    # First we open the tasks.txt file and use the append function 
    # To avoid overwriting the existing tasks.
    with open("tasks.txt", "a+") as f:   
        # Then we ask the user to input the details of the task.      
        username = input("Please enter the username of the person to whom you wish to assign the task: ")
        task_title = input("Please enter the title of the task: ")
        task_descr = input("Please enter a description of the task: ")
        task_date = input("When is the task due? (Please enter the date in the format 'YYYY-MM-DD'): ")
        # I ask the user to input the date in a certain format
        # So that the datetime module will recognise the date.
        current_date = datetime.date.today()
        # I worked out how to use the datetime function here:
        # https://www.programiz.com/python-programming/datetime
        task_complete = "No"
        # Once the user has entered the details of the task
        # We write the task on a single new line in the file.
        f.write("\n")
        f.writelines(f"{username}, {task_title}, {task_descr}, {current_date}, {task_date}, {task_complete}")
        print("Task added.")
        print("")

# I am defining a function called view_all
# This will be called later on in the code
def view_all():
# First we open the tasks.txt file and read it.
    with open("tasks.txt", "r+") as f:
        # Then we create a list out of each line in the file.
        # We strip the white lines and split the commas.
        # We use list comprehension for this.
        lines =[line.strip().split(", ") for line in f]
        for list in lines:              
            # After the lists have been created
            # We print the information in an easy to read format.
            print(f"""
Task:\t{list[1]}
Assigned to:\t{list[0]}
Date Assigned:\t{list[2]}
Due Date:\t{list[4]}
Task Complete?\t{list[5]}
Task Description:\t{list[2]}""")
    
# I am defining a function called view_mine
# This will be called later on in the code
def view_mine():
    # Defining an empty dictionary.
    task_dict = {}
    # Defining an empty task counter.
    task_count = 0
    with open("tasks.txt", "r+") as f:
        # We create a list from the file.
        for list in f:
            # We strip the newline character and split the commas.
            lines = list.strip("\n").split(", ")
            # Increasing the task counter by 1 for each line in the file.
            task_count += 1
            #Adding the counter to the lines in the file.
            task_dict[task_count] = lines
            # Checking the username to see which user is logged in.
            if username == lines[0]:
                # Displaying all that user's tasks in an easy to read format.
                print(f"""
Task:\t{lines[1]}
Assigned to:\t{lines[0]}
Date Assigned:\t{lines[2]}
Due Date:\t{lines[4]}
Task Complete?\t{lines[5]}
Task Description:\t{lines[2]}
Task number:\t{task_count}""")
                print("")
    
    # Asking the user if they would like to edit a task or exit the menu.
    task_number = int(input("""Select One of the following options:
Enter Task Number
Or Enter '-1' to exit
: """)) 
    print("")
    
    # If the user wants to edit a task they are shown a new menu.
    if task_number in task_dict:
        task_edit = input("""Select One of the following options:
u - Change user assigned to task
d - Change task due date
c - Mark task complete
: """).lower()
        print("")

        # The user can only edit an incomplete task.
        if task_dict[task_number][-1] == "No":
            if task_edit == "u":
                #This allows the user to reassign a task
                task_dict[task_number][0] = input("Please enter new user: ")
                print("Task assigned to new user.")
                print("")    
            elif task_edit == "d":
                # This allows the user to change the due date of a task
                task_dict[task_number][-2] = input("Please enter new due date: ")
                print("Task due date changed.")
                print("")   
            elif task_edit == "c":
                # This allows a user to mark a task as completed
                task_dict[task_number][-1] = "Yes"
                print("Task marked completed.")
                print("")
        else:
            print("Sorry, you cannot edit a completed task.")
            print("") 
    # If the user enters "-1", they are taken to the menu.
    elif task_number == -1:
        return 

    # Recreating a string from the dictionary, with the edited information.
    task = "\n".join([", ".join(t) for t in task_dict.values()])
    
    # Writing the new information into the text file.
    with open("tasks.txt", "w") as f:
        f.write(task)

# I am defining a function called task_overview
# This creates a report on the tasks in the tasks.txt file
def task_overview():
    # In order to count each item
    # I set empty counters
    # I also create an empty task dictionary        
    task_dict = {}
    completed = 0
    incomplete = 0
    overdue = 0
    task_count = 0
    with open("tasks.txt", "r+") as f2:
        # Then I open the tasks.txt file
        # We create a list from the file.
        for list in f2:
            # We strip the newline character and split the commas.
            lines = list.strip("\n").split(", ")
            # Increasing the task counter by 1 for each line in the file.
            task_count += 1
            # Adding the counter to the lines in the file.
            task_dict[task_count] = lines
    # Then I create the task_overview file
    with open("task_overview.txt", "w") as f:
        for count in task_dict:
            # I create a variable of the dictionary
            task = task_dict[count]
            # Then I index the point where the task is complete or not
            # And increase the respective counters accordingly
            if task[-1] == "Yes":
                completed += 1
            elif task[-1] == "No":
                incomplete += 1
            # Next I create a variable for the date
            due_date = datetime.datetime.strptime(task[4], '%Y-%m-%d')
            # And check which incomplete tasks are overdue
            if due_date < datetime.datetime.today() and task[-1] == "No":
                # Then I increase the counter
                overdue += 1
        # Next I calculate the percentage of incomplete and overdue tasks
        # And round to two decimal places
        percentage_incomplete = round(((incomplete/task_count)*100), 2)
        percentage_overdue = round(((overdue/task_count)*100), 2)
        # Then I write the information into the new file
        f.writelines(f"""There are {task_count} tasks in the file.
Of those tasks, {completed} have been completed, and {incomplete} are incomplete.
As of today, {overdue} tasks are overdue.
Incomplete tasks make up {percentage_incomplete}% of the total tasks.
Overdue tasks make up {percentage_overdue}% of the total tasks. 
""")

# Defining a function called user()
# This creates a list of the users in the user.txt file
def user():
    # I declare an empty list
    users = []
    # I open the user.txt file
    with open("user.txt", "r+") as f:
        for line in f:
            # Strip and split the lines
            all_users = line.strip("\n").split(", ")
            # Add usernames into the dictionary
            users.append(all_users[0])
    # return the function
    return users

# Defining a function called each_user()
# This creates a report on the data from the tasks.txt file
# But it is contextualised for the users in the user.txt file
def each_user(usrname, task_dict):
    # I set the variables usrname and
    # task_dictionary as arguments
    # I set empty counters for each statistic
    tasks_user = 0
    completed_user = 0
    incomplete_user = 0
    overdue_user = 0
    total_tasks = 0
    task_percentage = 0
    user_complete_percent = 0
    user_incomplete_percent = 0
    user_overdue_percent = 0
    # Then I open the tasks.txt file
    with open("tasks.txt", "r") as f:
        # I run a for loop to calculate each statistic
        # And increase the appropriate counter
        for count in task_dict:
            task = task_dict[count]
            total_tasks += 1
            if usrname == task[0]:
                tasks_user += 1
            if usrname == task[0] and task[5] == "Yes":
                completed_user += 1
            if usrname == task[0] and task[5] == "No":
                incomplete_user += 1
            # I create a variable for the due date
            due_date = datetime.datetime.strptime(task[4], '%Y-%m-%d')
            # And then use it to check if the task is overdue
            if usrname == task[0] and due_date < datetime.datetime.today() and task[-1] == "No":
                overdue_user += 1
    # Then I calculate the percentages of tasks complete etc
    if tasks_user != 0:
        user_complete_percent = round(((completed_user/tasks_user)*100), 2)
        user_incomplete_percent = round(((incomplete_user/tasks_user)*100), 2)
        user_overdue_percent = round(((overdue_user/tasks_user)*100), 2)
        task_percentage = round(((tasks_user/total_tasks)*100), 2)
    # Lastly I return the information in a string
    return f"""\nUser: {usrname}.
Total Tasks: {total_tasks}.
User Tasks: {tasks_user}.
{usrname}'s tasks are {task_percentage} of all tasks.
{user_incomplete_percent}% of {usrname}'s tasks need to be completed.
{user_complete_percent}% of {usrname}'s tasks have been completed.
{user_overdue_percent}% of {usrname}'s tasks are overdue.
"""

# I am defining a function called user_overview
# This will be called later on in the code
def user_overview():
    # I create a dictionary
    task_dict = {}
    # I call the user() function
    users = user()
    # I calculate the number of users
    total_users = len(users)
    # I create an empty counter for the task 
    task_count = 0
    with open("tasks.txt", "r+") as f2:
        # Then I open the tasks.txt file
        # We create a list from the file.
        for list in f2:
            # We strip the newline character and split the commas.
            lines = list.strip("\n").split(", ")
            # Increasing the task counter by 1 for each line in the file.
            task_count += 1
            # Adding the counter to the lines in the file.
            task_dict[task_count] = lines
        # Defining an empty string
        user_data = ""
        # Running a for loop to iterate the data for each user
        for u in users:
            # Adding the data to the string 
            # By calling the each_user function
            user_data += each_user(u, task_dict)
    # Creating and writing the data into a text file
    with open("user_overview.txt", "w") as f:
        f.write(f"""There are {total_users} users.
There are {task_count} tasks.""")
        f.write("\n")
        f.write(user_data)

# Defining a function to generate reports
# This will call the task_overview() and user_overview() functions
def gen_reports():
    task_overview()
    user_overview()
    return print("Reports generated. Please open task_overview.txt and user_overview.txt for more info.")
# Defining a boolean value for the login credentials.
login = True

# Defining empty dictionaries from the user.txt and tasks.txt files.
# The dictionaries will be used to locate the usernames and passwords.
user_dict = {}
pass_dict = {}

# After opening the user.txt file we can add the usernames and passwords 
# To their respective dictionaries.
with open("user.txt", "r+") as f:
    for line in f:
        # First we strip the whitespace and newline character and then split the comma.       
        login_items = line.strip("\n").split(", ")        
        # Then we define keys and values for the dictionaries. 
        user_dict[login_items[0]] = login_items[1]
        pass_dict[login_items[1]] = login_items[0]

while login:
    # We ask the user to enter a username and password
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    # If they match the username and password saved in the user.txt file.
    # The user can login.
    if username in user_dict and password == user_dict[username]:
        login = False

while True:
    # If the user logged in is the admin
    # They are shown a menu with options
    # To add a new user and view statistics
    if username == "admin":
        menu = input("""Select one of the following Options below:
r - Register a new user
a - Adding a task
va - View all tasks
vm - View my tasks
gr - Generate Reports
s - Show statistics
e - Exit
: """).lower()

    # If the user is not the admin
    # They are shown a different menu    
    else:
        menu = input("""Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my tasks
e - Exit
: """).lower()
    print("")

    # If the user selects "Register a new user"
    # The program will check that the user is the admin.
    if menu == "r" and username == "admin":
    # Then it will call the reg_user() function
        reg_user()        

    # This next section of code deals with the user adding a new task.
    elif menu == "a":
        # The program will call the add_task() function
        add_task()
    
    # This next section of code deals with the user wanting to view all existing tasks.
    elif menu == "va":
        # The program will call the view_all() function
        view_all()

    # This next section of code deals with the user 
    # Only wanting to view the tasks assigned to them           
    elif menu == "vm":
        # The program will call the view_mine() function
        view_mine()

    elif menu == "gr":
        # The program will call the gen_reports() function
        gen_reports()

    
    # This section of code deals with the admin wanting to view the statistics
    # The program ensures that the admin is logged in
    elif menu == "s" and username == "admin":
        # First calling the code to generate the reports
        gen_reports()

        print("User reports:")
        # Open user_overview.txt file                 
        with open("user_overview.txt", "r") as f1:
            # Using a for loop we read each line in the file
            for line in f1:
                print(line)
                
        print("Task Report:")
        # Open task_overview.txt file 
        with open("task_overview.txt", "r") as f2:
            # Using a for loop we read each line in the file
            for line1 in f2:    
                print(line1)


    # If the user chooses to exit the program,
    elif menu == "e":
        print("Adios Muchacho.")
        # The program says goodbye to the user
        # And exits using the exit function.  
        exit()
    
    # If the user does not enter a valid choice of option
    # They are asked to try again.
    else:
        print("You have made an invalid choice, please try again.")