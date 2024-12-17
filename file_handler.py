def get_tasks(file_path):
    """
    Read a text file and return a list of tasks.
    """

    with open(file_path, "r") as file:
        tasks = file.readlines()

    return [task.replace("\n", "") for task in tasks]

def set_tasks(tasks, file_path):
    """
    Write the task list in a text file.
    """

    tasks = [task + "\n" for task in tasks]

    with open(file_path, "w") as file:
        file.writelines(tasks)

# if __name__ == "__main__":
#     FILE_PATH = "tasks.txt"
#
#     for t in get_tasks(FILE_PATH):
#         print(t)
#
#     ts = ["Task 1", "Task 2", "Task 3"]
#
#     set_tasks(ts, FILE_PATH)