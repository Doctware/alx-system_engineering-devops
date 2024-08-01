#!/usr/bin/python3
"""This module fetches TODO list data for all employees
   from a REST API and exports it to a JSON file."""
import json
import requests


def get_all_employees_todolist():
    """Fetches TODO list data for all employees
        and exports it to a JSON file."""
    base_url = 'https://jsonplaceholder.typicode.com'
    todos_url = f'{base_url}/todos'
    users_url = f'{base_url}/users'

    # Fetch TODO list data for all employees
    todos_res = requests.get(todos_url)
    todos = todos_res.json()

    # Fetch user data for all employees
    users_res = requests.get(users_url)
    users = users_res.json()

    # Prepare data for JSON export
    todos_by_user = {}
    users_dict = {user['id']: user['username'] for user in users}

    for todo in todos:
        user_id = todo['userId']
        if user_id not in todos_by_user:
            todos_by_user[user_id] = []

        task_data = {
            "username": users_dict[user_id],
            "task": todo['title'],
            "completed": todo['completed']
        }
        todos_by_user[user_id].append(task_data)

    # Export to JSON
    json_filename = 'todo_all_employees.json'
    with open(json_filename, mode='w') as json_file:
        json.dump(todos_by_user, json_file, indent=4)


if __name__ == "__main__":
    get_all_employees_todolist()
