import pathlib

FILEPATH = "todo.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list to a text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def check_file():
    if not pathlib.Path(FILEPATH).is_file():
        with open(FILEPATH, 'w') as file:
            pass


if __name__ == "__main__":
    print('Hello')
    print(get_todos())
