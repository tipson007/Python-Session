while True:
    # Prompt the user for an action and remove any leading/trailing whitespace
    user_action = input("Add task, Show tasks, Edit, Complete or Exit: ")
    user_action = user_action.strip()

    # Compare the user's input to different cases using the new match statement (Python 3.10+)
    match user_action:
        case 'add':
            # Open the file in read mode, read the tasks into a list, and close the file
            file = open("Tasks.txt", "r")
            tasks = file.readlines()
            file.close()

            # Prompt the user for a new task and add it to the list
            task = input("Enter a task: ") + "\n"
            tasks.append(task)

            # Open the file in write mode, write the updated tasks to the file, and close the file
            file = open("Tasks.txt", "w")
            file.writelines(tasks)
            file.close()

        case 'show':
            # Open the file in read mode, read the tasks into a list, and close the file
            file = open("Tasks.txt", "r")
            tasks = file.readlines()
            file.close()

            # Loop through the tasks and print each one with a label that includes its index number
            for index, item in enumerate(tasks):
                label = f"{index + 1}.{item}"
                print(label)

        case 'edit':
            # Open the file in read mode, read the tasks into a list, and close the file
            file = open("Tasks.txt", "r")
            tasks = file.readlines()
            file.close()

            # Prompt the user for the index of the task to edit and a new task, and replace the old task with the new one
            number = int(input("Enter the number of the task to edit: "))
            number = number - 1
            new_task = input("Enter new task: ") + "\n"
            tasks[number] = new_task

            # Open the file in write mode, write the updated tasks to the file, and close the file
            file = open("Tasks.txt", "w")
            file.writelines(tasks)
            file.close()

            # Print a message to confirm that the task was edited
            print("Task edited!")

        case 'complete':
            # Open the file in read mode, read the tasks into a list, and close the file
            file = open("Tasks.txt", "r")
            tasks = file.readlines()
            file.close()

            # Prompt the user for the completed task, and remove it from the list if it exists
            completed_task = input("Enter the completed task: ")
            if completed_task in tasks:
                tasks.remove(completed_task)

                # Open the file in write mode, write the updated tasks to the file, and close the file
                file = open("Tasks.txt", "w")
                file.writelines(tasks)
                file.close()

                # Print a message to confirm that the task was removed
                print("Task removed!")
            else:
                # Print an error message if the task was not found
                print("Task not found!")

        case 'exit':
            # Exit the loop and the program
            break

# Print a message to confirm that tasks have been successfully added
print("You have successfully managed your tasks!")
