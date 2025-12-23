"""
This Python module is a task manager. Its purpose is to hold user login details,
create and assign tasks to users, and to display tasks for each user, in addition
to an overview of tasks and users within the task manager.

Access the task manager using your login details. Then, choose from the menu which
option you wish to run.

● Use the following username and password to access the admin rights 

    username: admin
    password: password

● Ensure you open the whole folder for this task in VS Code otherwise
the program will look in your root directory for the text files.

"""

# ===== Importing Libraries =====
# os - operating system functions
# datetime - date and time functions
import os
from datetime import datetime, date

# Module-wide date format
DATETIME_STRING_FORMAT = "%Y-%m-%d"


# ===== User Functions Section =====
def reg_user():
    """
    Registers a new user to the user text file.

    Parameters:
    None.

    Returns:
    str: Statement of success or failure.
    """
    # Get new user information
    new_username = input("New Username: ")
    new_password = input("New Password: ")
    confirm_password = input("Confirm Password: ")

    # Check username is unique in user dictionary
    while new_username in username_password:
        print("This username already exists.")
        new_username = input("New Username: ")

    else:

        # Check if entered passwords are identical
        # Add username/password pair to dictionary
        if new_password == confirm_password:
            result = "New user added"
            username_password[new_username] = new_password

            # Add new dictionary pair to user text file
            with open("user.txt", "w", encoding="utf-8") as out_file:
                user_data = []

                for username, password in username_password.items():
                    user_data.append(f"{username};{password}")
                out_file.write("\n".join(user_data))

        else:
            result = "Passwords do not match"

    print(result)

    return result


def add_task():
    """
    Adds a new task to the tasks text file.

    Parameters:
    None.

    Returns:
    str: Statement of success.
    """
    task_username = input("Name of person assigned to task: ")

    # Check that the user assigned to the task is valid
    while task_username not in username_password:
        print("User does not exist. Please enter a valid username")
        task_username = input("Name of person assigned to task: ")

    # Receive task details
    else:
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")

        # Check date entered is in correct format
        while True:

            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(
                    task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")

    current_date = date.today()

    # Dictionary of new task added to list of all tasks
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": current_date,
        "completed": False
    }
    task_list.append(new_task)

    # Add all dictionaries within tasks list to tasks text file
    with open("tasks.txt", "w", encoding="utf-8") as task_file:
        task_list_to_write = []

        for task in task_list:
            str_attrs = [
                task['username'],
                task['title'],
                task['description'],
                task['due_date'].strftime(DATETIME_STRING_FORMAT),
                task['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if task['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))

        task_file.write("\n".join(task_list_to_write))

    result = "Task successfully added."
    print(result)

    return result


def view_all():
    """
    Views all tasks in the tasks text file.

    Parameter:
    None.

    Returns:
    str: A 'for' loop of tasks from the tasks list.
    """
    display = ""

    # Loop through each task and print
    for task in task_list:
        display += (
            f"\nTask: \t\t {task['title']}\n"
            f"Assigned to: \t {task['username']}\n"
            f"Date Assigned: \t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            f"Due Date: \t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            f"Task Description: \n {task['description']}\n"
        )

    print(display)

    return display


def view_mine():
    """
    Views all the user's tasks in the tasks text file.

    Parameter:
    None.

    Returns:
    str: Statement of success or return to main menu.
    """
    # Set variables
    n = 0
    display = ""
    task_load = []

    # Loop through each task belonging to the user
    # Add a number to each task
    # Add each task to a new list
    for task in task_list:

        if task['username'] == current_user:
            n += 1
            display += (
                f"\nNumber: \t {n}\n"
                f"Task: \t\t {task['title']}\n"
                f"Assigned to: \t {task['username']}\n"
                f"Date Assigned: \t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                f"Due Date: \t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                f"Task Description: \n {task['description']}\n\n"
                f"Completed: \t {task['completed']}\n\n"
            )
            task_load.append(task)

    # Show user their tasks
    print(display)

    task_choice_1 = int(input(
        "Which task would you like to edit or mark as complete? (Type '-1' to return): "))

    """
    
    The following is partly mine in addition to code I wrote after consulting with a mentor
    during a 1:1 session on the 25/11.

    This code is in relation to '4.' of the practical task instructions.
    
    """
    # Returns to menu if '-1' is chosen
    # Cannot choose a task number above how many there are
    # Can only edit an incomplete task
    while task_choice_1 != -1:

        if task_choice_1 <= len(task_load):

            if not task_load[task_choice_1 - 1]['completed']:
                task_choice_2 = input("Type from the following:\n"
                                      "user - Edit the username of the task owner.\n"
                                      "date - Edit the due date of the task.\n"
                                      "complete - Mark task as complete.\n\n"
                                      "Press enter to return.\n"
                                      ": ").lower()

                # Change assigned user
                if task_choice_2 == "user":
                    new_user = input("Enter the task's new owner: ")
                    task_load[task_choice_1 - 1]['username'] = new_user

                # Change due date
                elif task_choice_2 == "date":

                    while True:

                        try:
                            new_due_date = input(
                                "New due date of task (YYYY-MM-DD): ")
                            due_date_time = datetime.strptime(
                                new_due_date, DATETIME_STRING_FORMAT)
                            break

                        except ValueError:
                            print(
                                "Invalid datetime format. Please use the format specified")

                    task_load[task_choice_1 - 1]['due_date'] = due_date_time

                # Mark task as complete
                elif task_choice_2 == "complete":
                    task_load[task_choice_1 - 1]['completed'] = "Yes"

                result = "Task successfully edited."

            else:
                print("This task has already been marked as complete.")

        else:
            print("This choice is invalid. Please choose a valid task number.")

        # Replace all tasks sharing the same title with the edited tasks
        for task in range(0, len(task_list) - 1):

            if task_load[task_choice_1 - 1]['title'] == task_list[task]['title']:
                task_list[task] = task_load[task_choice_1 - 1]

            else:
                continue

        # Write all tasks to tasks text file
        with open("tasks.txt", "w", encoding="utf-8") as task_file:
            task_list_to_write = []

            for task in task_list:
                str_attrs = [
                    task['username'],
                    task['title'],
                    task['description'],
                    task['due_date'].strftime(DATETIME_STRING_FORMAT),
                    task['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if task['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))

            task_file.write("\n".join(task_list_to_write))

        task_choice_1 = int(input(
            "Which task would you like to edit or mark as complete? (Type '-1' to return): "))

    else:
        result = "Returned to menu."

    print(result)

    return result


def gen_reports():
    """
    Generates text files containing overviews.

    Parameter:
    None.

    Returns:
    dict: Dictionaries of task and user overviews.
    """
    # Creates a task overview file if one doesn't exist
    if not os.path.exists("task_overview.txt"):
        with open("task_overview.txt", "w", encoding="utf-8") as default_file:
            pass

    # Read in the task overview file
    with open("task_overview.txt", 'r', encoding="utf-8") as task_overview_file:
        task_overview_data = task_overview_file.read().split("\n")

    task_overview = {}

    # Initialise counts for statistics
    tasks_completed = 0
    tasks_incomplete = 0
    tasks_overdue = 0

    # Count completed, incomplete and overdue tasks
    for task in task_list:

        if task['completed']:
            tasks_completed += 1

        else:
            tasks_incomplete += 1

            if task['due_date'] < datetime.today():
                tasks_overdue += 1

    # Add statistics to dictionary
    task_overview['Total Tasks'] = str(len(task_list))
    task_overview['Completed Tasks'] = str(tasks_completed)
    task_overview['Incomplete Tasks'] = str(tasks_incomplete)
    task_overview['Overdue Tasks'] = str(tasks_overdue)
    task_overview['% Incomplete Tasks'] = str(
        round((tasks_incomplete / len(task_list)) * 100, 2))
    task_overview['% Overdue Tasks'] = str(
        round((tasks_overdue / len(task_list)) * 100, 2))

    # Write the dictionary to task overview text file
    with open("task_overview.txt", "w", encoding="utf-8") as task_file:
        task_overview_data = []

        for data_point, data_value in task_overview.items():
            task_overview_data.append(f"{data_point};{data_value}")

        task_file.write("\n".join(task_overview_data))

    # Creates a user overview file if one doesn't exist
    if not os.path.exists("user_overview.txt"):
        with open("user_overview.txt", "w", encoding="utf-8") as default_file:
            pass

    # Read in the user overview file
    with open("user_overview.txt", 'r', encoding="utf-8") as user_overview_file:
        user_overview_data = user_overview_file.read().split("\n")

    user_overview = {}

    # Initialise counts for statistics
    total_users = 0
    per_task_completed = 0
    per_task_over_incomplete = 0

    # Create a list of usernames
    usernames = username_password.keys()

    # Count users, tasks, tasks per user, and percentages of tasks
    # Percentages include incomplete and overdue
    # Add statistics to dictionary
    for user in usernames:

        x = 0
        total_users += 1
        user_overview['Total Users'] = str(total_users)

        for task in task_list:

            user_overview['Total Tasks'] = str(len(task_list))

            if task['username'] == user:

                x += 1
                user_task_total = x
                user_overview[str(user) + "'s Tasks"] = str(user_task_total)
                user_overview[str(
                    user) + "'s Tasks %"] = str(round((user_task_total / len(task_list)) * 100, 2))

                if task['completed']:

                    per_task_completed += 1
                    user_overview[str(user) + "'s Completed %"] = str(
                        round((per_task_completed / user_task_total) * 100, 2))
                    user_overview[str(user) + "'s Incomplete %"] = str(100 -
                                                                       float(user_overview[str(user) + "'s Completed %"]))

                    if task['due_date'] < datetime.today():

                        per_task_over_incomplete += 1
                        user_overview[str(user) + "'s Overdue & Incomplete %"] = str(
                            round((per_task_over_incomplete / user_task_total) * 100, 2))

                    else:

                        user_overview[str(user) +
                                      "'s Overdue & Incomplete %"] = "0.0"

                else:

                    user_overview[str(user) + "'s Completed %"] = "0.0"
                    user_overview[str(user) + "'s Incomplete %"] = "100.0"
                    user_overview[str(user) +
                                  "'s Overdue & Incomplete %"] = "100.0"

    # Write to the user overview text file a dictionary of statistics
    with open("user_overview.txt", "w", encoding="utf-8") as user_file:
        user_overview_data = []

        for data_point, data_value in user_overview.items():
            user_overview_data.append(f"{data_point};{data_value}")

        user_file.write("\n".join(user_overview_data))

    print("Overviews generated successfully!")

    return task_overview, user_overview


# ===== Tasks Section =====
# This code reads tasks from the tasks.txt file and
# adds them to a list.

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):

    with open("tasks.txt", "w", encoding="utf-8") as default_file:
        pass

# Read in the tasks text file
with open("tasks.txt", 'r', encoding="utf-8") as task_file:
    task_data = task_file.read().split("\n")
    task_data = [task for task in task_data if task != ""]

# Create a list of tasks from the tasks text file
task_list = []
for task in task_data:
    current_task = {}

    # Split by semicolon and manually add each component
    task_components = task.split(";")
    current_task['username'] = task_components[0]
    current_task['title'] = task_components[1]
    current_task['description'] = task_components[2]
    current_task['due_date'] = datetime.strptime(
        task_components[3], DATETIME_STRING_FORMAT)
    current_task['assigned_date'] = datetime.strptime(
        task_components[4], DATETIME_STRING_FORMAT)
    current_task['completed'] = task_components[5] == "Yes"

    task_list.append(current_task)


# ====Login Section====
# This code reads usernames and password from the user.txt file to
# allow a user to login.

# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w", encoding="utf-8") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r', encoding="utf-8") as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

while True:
    print("LOGIN")
    current_user = input("Username: ")
    current_pass = input("Password: ")
    if current_user not in username_password:
        print("User does not exist")
        continue
    if username_password[current_user] != current_pass:
        print("Wrong password")
        continue
    print("Login Successful!")
    break

# ===== Main Menu Section =====
while True:
    # Presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    print()
    menu = input("Select one of the following options below:\n"
                 "r - Registering a user\n"
                 "a - Adding a task\n"
                 "va - View all tasks\n"
                 "vm - View my tasks\n"
                 "gr - Generate reports\n"
                 "ds - Display statistics\n"
                 "e - Exit\n"
                 ": ").lower()

    # Add a new user to the user.txt file
    if menu == 'r':
        reg_user()

    # Allow a user to add a new task to task.txt file
    elif menu == 'a':
        add_task()

    # Reads the tasks from tasks.txt file and displays
    # to the user.
    elif menu == 'va':
        view_all()

    # Reads the tasks belonging to the user from tasks.txt and
    # allows the user to edit any of them.
    elif menu == 'vm':
        view_mine()

    # Generates two text files containing statistics on both
    # tasks and users.
    elif menu == 'gr':
        gen_reports()

    # If the user is an admin they can display statistics about number of users
    # and tasks.
    elif menu == 'ds' and current_user == 'admin':
        task_overview, user_overview = gen_reports()
        # Displays all statistics from task_overview.txt
        print("\n\n-----------------------------------")
        print(f"Number of tasks: \t\t {task_overview['Total Tasks']}")
        print(
            f"Number of completed tasks: \t\t {task_overview['Completed Tasks']}")
        print(
            f"Number of incomplete tasks: \t\t {task_overview['Incomplete Tasks']}")
        print(
            f"Percentage of incomplete tasks: \t\t {task_overview['% Incomplete Tasks']}")
        print(
            f"Number of overdue tasks: \t\t {task_overview['Overdue Tasks']}")
        print(
            f"Percentage of overdue tasks: \t\t {task_overview['% Overdue Tasks']}")
        print("-----------------------------------\n\n")
        print(f"Number of users: \t\t {user_overview['Total Users']}")

        # Loop through each user to display each user's statistics
        # from user_overview.txt
        for user in username_password.keys():

            if user + "'s Tasks" in user_overview.keys():

                print(
                    user + "'s Tasks: \t {}".format(user_overview[user + "'s Tasks"]))
                print(
                    user + "'s Tasks (%): \t {}".format(user_overview[user + "'s Tasks %"]))
                print(
                    user + "'s Completed (%): \t {}".format(user_overview[user + "'s Completed %"]))
                print(
                    user + "'s Incomplete (%): \t {}".format(user_overview[user + "'s Incomplete %"]))
                print(user + "'s Overdue Tasks (%): \t {}\n\n".format(
                    user_overview[user + "'s Overdue & Incomplete %"]))

            else:

                print(user + "'s Tasks: \t {}".format("0"))
                print(user + "'s Tasks (%): \t {}".format("N/A"))
                print(user + "'s Completed (%): \t {}".format("N/A"))
                print(user + "'s Incomplete (%): \t {}".format("N/A"))
                print(user + "'s Overdue Tasks (%): \t {}\n\n".format("N/A"))

        print("-----------------------------------\n\n")

    # Exit the task manager.
    elif menu == 'e':
        print('Goodbye!!!')
        break

    else:
        print("You have made a wrong choice, Please try again.\n")
