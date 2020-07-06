#!/usr/bin/python3
"""
information
"""


import json
import requests


def get_user_info():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get("{}".format(url), verify=False)
    if response.status_code == 200:
        file_name = 'todo_all_employees.json'
        data = {}
        content = response.json()
        for user in content:
            user_id = user.get('id', 1)
            data[str(user_id)] = []
            for task in requests.get(
                    "{}/{}/todos".format(url, user_id), verify=False
            ).json():
                data[str(user_id)].append(
                    {
                        "task": task.get('title', ''),
                        "completed": task.get('completed', False),
                        "username": user.get('username', '')
                    }
                )
        with open(file_name, 'w', newline='') as file:
            json.dump(data, file)


if __name__ == "__main__":
    get_user_info()
