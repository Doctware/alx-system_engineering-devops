#!/usr/bin/python3
"""This module contains a function that requests
   REST API for a given employee ID then
   returns information about his/her todo list
   and exports it to a JSON file."""
import json
import requests
import sys


def get_employee_todolist(employee_id):
    """The function fetches the employee's todo list
        and exports it to a JSON file."""
    base_url = 'https://jsonplaceholder.typicode.com'
    todos_url = f'{base_url}/todos?userId={employee_id}'
    users_url = f'{base_url}/users/{employee_id}'

    # Fetch TODO list data
    todos_res = requests.get(todos_url)
    todos = todos_res.json()

    # Fetch employee data
    user_res = requests.get(users_url)
    user = user_res.json()

    # Get employee name
    employee_name = user['name']

    # Print the progress report
    total_tsk = len(todos)
    completed_tsk = [todo for todo in todos if todo['completed']]
    num_completed_tsk = len(completed_tsk)

    print(f"Employee {employee_name} is done with tasks ({num_completed_tsk}/{total_tsk}):")
    for tsk in completed_tsk:
        print(f"\t {tsk['title']}")

    # Prepare data for JSON export
    tasks = []
    for todo in todos:
        task_data = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": user['username']
        }
        tasks.append(task_data)

    json_data = {
        str(employee_id): tasks
    }

    # Export to JSON
    json_filename = f"{employee_id}.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todolist(employee_id)
