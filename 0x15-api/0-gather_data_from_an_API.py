#!/usr/bin/python3
"""REST API practice"""
import requests
import sys


def get_employee_todos():
    """Get todo list for employee based on id"""
    id = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/todos/'
    todos = requests.get(url)
    totalTasks = 0
    completed = 0
    taskTitles = ""
    for todo in todos.json():
        if todo.get('userId') == id:
            totalTasks += 1
            title = todo.get('title')
            title = f'\t {title}\n'
            taskTitles += title
            if todo.get('completed'):
                completed += 1
    name = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    name = name.json().get('name')
    output = f'Employee {name} is done with tasks({completed}/{totalTasks}):'
    print(output)
    print(taskTitles, end="")


if __name__ == '__main__':
    get_employee_todos()
