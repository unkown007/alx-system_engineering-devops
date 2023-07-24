#!/usr/bin/python3
""" gather data from an API """
from requests import get
from sys import argv


if __name__ == "__main__":
    user_details = get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                argv[1])).json()
    user_todos = get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                argv[1])).json()
    total = len(user_todos)
    total_done = 0
    for task in user_todos:
        if task["completed"]:
            total_done = total_done + 1
    print("Employee {} is done with "
          "tasks({}/{}):".format(
                user_details["name"], total_done, total))
    for task in user_todos:
        if task["completed"]:
            print('\t{}'.format(task["title"]))
