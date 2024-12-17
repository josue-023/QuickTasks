# https://github.com/josue-023/QuickTasks.git

import streamlit as st
import file_handler as fh

FILE_PATH = "tasks.txt"
tasks = fh.get_tasks(FILE_PATH)

def add_task():
    task = st.session_state["task"]

    if task == "":
        return

    tasks.append(task)
    fh.set_tasks(tasks, FILE_PATH)

st.title("Quick Tasks")

for index, task in enumerate(tasks):
    checkbox_key = f"task {index}"
    is_completed = st.checkbox(label=task, key=checkbox_key)

    if is_completed:
        tasks.pop(index)
        fh.set_tasks(tasks, FILE_PATH)

        st.session_state.pop(checkbox_key)
        st.rerun()

st.text_input(label="", key="task", on_change=add_task, placeholder="Add a task")