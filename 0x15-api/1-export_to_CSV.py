#!/usr/bin/python3
"""REST API practice"""
import csv
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
    rows = []
    name = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    name = name.json().get('name')
    for todo in todos.json():
        if todo.get('userId') == id:
            status = todo.get('completed')
            title = todo.get('title')
            rows.append([id, name, status, title])
    with open(f'{id}.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerows(rows)


if __name__ == '__main__':
    get_employee_todos()
