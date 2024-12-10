To-Do List Application (Python)
This is a simple To-Do List application built using Python, which allows users to manage tasks by adding, viewing, deleting, and sorting tasks based on priority and due date. This project serves as a beginner-level Python project and will continue to be developed to introduce more advanced features and functionality over time.

Features
Add Task: Allows the user to add tasks with a name, priority, and due date.
View Tasks: Displays all the tasks in a list format.
Delete Task: Users can delete tasks by selecting the task number.
Sort Tasks by Priority: Tasks can be sorted by priority (High, Medium, Low).
Sort Tasks by Due Date: Tasks can be sorted by their due date, from nearest to furthest.
Project Overview
This project was created as my first Python project to learn and apply basic programming concepts like data types, classes, functions, loops, conditionals, and error handling. The application stores tasks in a list and allows users to interact with them via a simple text-based menu.

How It Works
Task Class: Each task is represented as an object of the Task class. A task has three properties:

name: The name or description of the task.
priority: The priority of the task (1: High, 2: Medium, 3: Low).
due_date: The due date of the task in YYYY-MM-DD format.
Main Program Loop: The program runs in a loop that displays a menu to the user. The user can select an option to interact with the tasks. The main operations are:

Add task: Prompts the user for task details and adds it to the list.
View tasks: Displays all the tasks in the list.
Delete task: Removes a task based on its number.
Sort tasks: Tasks can be sorted either by priority or due date.
Error Handling: The program includes basic error handling to ensure the user inputs valid data for priority and due date fields.

Technologies Used
Python 3.x

Future Improvements
This is just the first version of the project. In the future, I plan to add more features, such as:

Persistence: Save tasks to a file or database so that they persist across program restarts.
Task Editing: Allow users to update the details of a task after it has been added.
Task Completion: Implement a feature to mark tasks as complete.
Graphical User Interface (GUI): Build a GUI using frameworks like Tkinter or PyQt to make the application more user-friendly.
Task Categories: Allow tasks to be organized into categories or projects.
Prioritization by Deadline: Automatically prioritize tasks that are due sooner.
