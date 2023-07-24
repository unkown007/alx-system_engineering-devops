#!/usr/bin/python3
""" gather data from an API """
import json
from requests import get


if __name__ == "__main__":
    user_details = get(
            'https://jsonplaceholder.typicode.com/users').json()
    filename = "todo_all_employees.json"
    todo_all = {}
    for user in user_details:
        user_todos = get(
                'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                    user["id"])).json()
        tasks = []
        for task in user_todos:
            tasks.append({
                'username': user["username"],
                'task': task["title"],
                'completed': task["completed"],
                })
        todo_all[str(user["id"])] = tasks
    with open(filename, "w", encoding="utf-8") as jsonfile:
        json.dump(todo_all, jsonfile)
