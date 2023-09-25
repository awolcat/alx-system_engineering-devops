#!/usr/bin/python3
"""REST API practice"""
import json
import requests
import sys


def get_employee_todos():
    """Get todo list for employee based on id"""
    id = int(sys.argv[1])
    todosUrl = 'https://jsonplaceholder.typicode.com/todos/'
    todos = requests.get(todosUrl)
    totalTasks = 0
    completed = 0
    taskTitles = ""
    rows = []
    name = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    name = name.json().get('username')
    for todo in todos.json():
        if todo.get('userId') == id:
            status = todo.get('completed')
            title = todo.get('title')
            taskDict = {
                            'task': title,
                            'completed': status,
                            'username': name
                        }
            rows.append(taskDict)
    userTasks = {str(id): rows}
    with open(f'{id}.json', 'w') as jsonfile:
        json.dump(userTasks, jsonfile)


if __name__ == '__main__':
    get_employee_todos()
