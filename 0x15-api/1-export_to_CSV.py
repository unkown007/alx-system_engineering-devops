#!/usr/bin/python3
""" gather data from an API """
import csv
from requests import get
from sys import argv


if __name__ == "__main__":
    user_details = get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                argv[1])).json()
    user_todos = get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                argv[1])).json()
    filename = str(user_details["id"]) + ".csv"
    with open(filename, "w", encoding="utf-8") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in user_todos:
            spamwriter.writerow([
                user_details["id"],
                user_details["username"],
                task["completed"],
                task["title"]])
