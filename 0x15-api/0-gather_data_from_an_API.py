#!/usr/bin/python3
""" this module contains a function thats request
    REST API for a given employee ID then
    return about his/her todo list """
import requests
import sys


def get_employee_todolist(employee_id):
    """ the function thats fetch emplyee todolist """
    base_url = 'https://jsonplaceholder.typicode.com'
    todos_url = f'{base_url}/todos?userId={employee_id}'
    users_url = f'{base_url}/users/{employee_id}'

    # fetch TODO list data
    todos_res = requests.get(todos_url)
    todos = todos_res.json()

    # fetch employee data
    user_res = requests.get(users_url)
    user = user_res.json()

    # calculate the number of task and completed one
    total_tsk = len(todos)
    completed_tsk = [todo for todo in todos if todo['completed']]
    num_completed_tsk = len(completed_tsk)

    # get employee name
    employee_name = user['name']

    # print the progres report
    print(f"Employee {employee_name} is done with tasks ({num_completed_tsk}/{total_tsk}): ")
    for tsk in completed_tsk:
        print(f"\t  {tsk['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        system.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todolist(employee_id)
