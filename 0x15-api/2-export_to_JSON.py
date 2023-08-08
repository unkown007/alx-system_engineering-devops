#!/usr/bin/python3
""" gather data from an API """
import json
from requests import get
from sys import argv


if __name__ == "__main__":
    user_details = get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                argv[1])).json()
    user_todos = get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                argv[1])).json()
    filename = str(user_details["id"]) + ".json"
    with open(filename, "w", encoding="utf-8") as jsonfile:
        tasks = []
        for task in user_todos:
            tasks.append({
                'task': task["title"],
                'completed': task["completed"],
                'username': user_details["username"],
                })
        json.dump({str(user_details["id"]): tasks}, jsonfile)
