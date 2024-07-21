import requests


def get_todos():
    url = "https://jsonplaceholder.typicode.com/todos"
    try:
        response = requests.get(url)
        response.raise_for_status()
        todos = response.json()
    except requests.RequestException as e:
        print(f"And error occured : {e}")
        todos = None
    finally:
        return todos


todos = get_todos()
if todos is not None:
    print("Fetched Todos:")
    for todo in todos:
        print(f"ID: {todo['id']}, Title: {
              todo['title']}, Completed: {todo['completed']}")
else:
    print("Failed to fetch Todos;")
