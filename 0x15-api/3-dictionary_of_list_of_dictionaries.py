#!/usr/bin/python3
"""REST API practice"""
import json
import requests


def get_all_employee_todos():
    """Get todo list for all employees"""
    usersUrl = 'https://jsonplaceholder.typicode.com/users/'
    todosUrl = 'https://jsonplaceholder.typicode.com/todos/'
    users = requests.get(usersUrl)
    todos = requests.get(todosUrl)
    userTasks = []
    for user in users.json():
        id = user.get('id')
        username = user.get('username')
        for todo in todos.json():
            if todo.get('userId') == id:
                status = todo.get('completed')
                title = todo.get('title')
                taskDict = {
                                'username': username,
                                'task': title,
                                'completed': status
                            }
                userTasks.append(taskDict)
        userTasksDict = {str(id): userTasks}

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(userTasksDict, jsonfile)


if __name__ == '__main__':
    get_all_employee_todos()
