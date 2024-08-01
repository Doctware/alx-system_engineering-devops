#!/usr/bin/python3
"""This module contains a function that requests
   REST API for a given employee ID then
   returns information about his/her todo list and exports it to a CSV file."""
import csv
import requests
import sys


def get_employee_todolist(employee_id):
    """The function fetches the employee's todo list
        and exports it to a CSV file."""
    base_url = 'https://jsonplaceholder.typicode.com'
    todos_url = f'{base_url}/todos?userId={employee_id}'
    users_url = f'{base_url}/users/{employee_id}'

    # Fetch TODO list data
    todos_res = requests.get(todos_url)
    todos = todos_res.json()

    # Fetch employee data
    user_res = requests.get(users_url)
    user = user_res.json()

    # Calculate the number of tasks and completed tasks
    total_tsk = len(todos)
    completed_tsk = [todo for todo in todos if todo['completed']]
    num_completed_tsk = len(completed_tsk)

    # Get employee name
    employee_name = user['name']

    # Print the progress report
    print(f"Employee {employee_name} is done with tasks ({num_completed_tsk}/{total_tsk}):")
    for tsk in completed_tsk:
        print(f"\t {tsk['title']}")

    # Export to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames =\
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for todo in todos:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": user['username'],
                "TASK_COMPLETED_STATUS": todo['completed'],
                "TASK_TITLE": todo['title']
            })


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todolist(employee_id)
