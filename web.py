import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_item"]
    todos.append(new_todo + "\n")
    functions.write_todos(todos)


st.title("My To-Do App")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Add a new item", label_visibility="hidden", placeholder="Add a new to-do item",
              on_change=add_todo, key="new_item")
